
import socket
import threading
import time

class Client(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def open_connect(self):

        try:
            self.sock = socket.socket()
            self.sock.bind(('', 9090))
            self.sock.listen(1)
            self.connection, self.address = self.sock.accept()
            print(">>>SOCKET OPEN")
            print(">>>NEW CONNECTION:", self.address)
            Client.send_message(self, "WD>>> Connection successful")
        except socket.error:
            print(">>>SOCKET ERROR")


    def close_connect(self):
        self.connection.close()
        print(">>>SOCKED CLOSED")

    def receive_message(self):
        while True:
            data = str(self.connection.recv(1024))
            data = data[2:-1]
            Client.send_message(self, "WD>>> Command received")

            if data == "disconnect":
                Client.close_connect(self)
            return data

    def send_message(self, message):
        self.connection.send(message.encode())

    def check_connection(self):
        try:
            time.sleep(1)
            self.send_message('check')
        except socket.error:
            return False
