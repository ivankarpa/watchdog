import socket
import threading
import sys

sys.path.append('../common/')
import watchdog_config


class Client(threading.Thread):
    def __init__(self, subprocess, logger):
        threading.Thread.__init__(self)

        self.logger = logger
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.config = watchdog_config.WatchdogConfig('watchdog.cfg')
        self.subprocess = subprocess
        self.stop_signal = False
        self.host = ''
        self.port = 0

    def run(self):
        try:
            host_found, self.host = self.config.get_option('connect', 'host')
            if not host_found:
                message = "Host not set in config"
                self.logger.error(message)
            _, self.port = self.config.get_option('connect', 'port')
            self.sock.bind((self.host, int(self.port)))
            self.sock.listen(1)
            while not self.stop_signal:
                self.connection, self.address = self.sock.accept()
                command = self.receive_message()
                response = self.subprocess.execute_command(command)
                self.send_message(response)
        except OSError as err:
            message = "Exception! {0} ({1})".format(err.strerror, err.errno)
            self.logger.error(message)
        except ConnectionRefusedError:
            message = "Connection to {0}:{1} refused".format(self.host, self.port)
            self.logger.error(message)
        except socket.error as msg:
            message = "Exception! errcode: {0}, message: {1}. Server: {2}:{3}".format(msg[0], msg[1], self.host, self.port)
            self.logger.error(message)

    def stop(self):
        self.stop_signal = True
        close_sock = socket.socket()
        close_sock.connect((self.host, int(self.port)))
        close_sock.close()

    def send_message(self, message):
        self.connection.send(str(message).encode())

    def receive_message(self):
        return str(self.connection.recv(1024).decode())
