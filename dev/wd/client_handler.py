import socket
import threading
import sys
sys.path.append('./../config_parser/')
import config

class Client(threading.Thread):
    def __init__(self, subprocess):
        threading.Thread.__init__(self)
        self.sock = socket.socket()
        self.config = config.Config('watchdog.cfg')
        self.subprocess = subprocess

    def run(self):
        try:
            host_found, host = self.config.get_option('connect', 'host')
            if not host_found:
                return "Host not set in config"
            _, port = self.config.get_option('connect', 'port')
            self.sock.bind((host, int(port)))
            self.sock.listen(1)
            while True:
                self.connection, self.address = self.sock.accept()
                command = self.receive_message()
                response = self.subprocess.execute_command(command)
                self.send_message(response)

        except ConnectionRefusedError:
            return "Connection to {0}:{1} refused".format(host, port)
        except socket.error as msg:
            return "Exception! errcode: {0}, message: {1}. Server: {2}:{3}".format(msg[0], msg[1], host, port)

    def send_message(self, message):
        self.connection.send(str(message).encode())

    def receive_message(self):
        return str(self.connection.recv(1024).decode())
