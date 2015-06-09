__author__ = 'ivankarpa'
import socket
import threading


class Client(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.sock = ""
        self.connection = ""
        self.address = ""

    def open_connect(self):
        self.sock = socket.socket()
        self.sock.bind(('', 9092))
        self.sock.listen(1)
        self.connection, self.address = self.sock.accept()
        print(">>>NEW CONNECTION:", self.address)

    def close_connect(self):
        self.connection.close()
        print(">>>CONNECTION CLOSED")

    def recive_message(self):
        while True:
            data = self.connection.recv(1024)
            if not data:
                self.close_connect()
                return False
            return data

