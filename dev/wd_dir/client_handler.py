import socket
import threading

import cfg_parser


class Client(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.sock = socket.socket()
        self.config = cfg_parser.Config()

    def open_connect(self):
        try:

            self.sock.bind((self.config.get_host(), self.config.get_port()))
            self.sock.listen(1)
            return True
        except socket.error as msg:
            return "Exception! errcode: {0}, message: {1}".format(msg[0], msg[1])

    def send_message(self, message):
        print(message)
        self.connection.send(str(message).encode())

    def receive_message(self):
        self.connection, self.address = self.sock.accept()
        return str(self.connection.recv(1024).decode())
