__author__ = 'ivankarpa'
import socket

sock = socket.socket()


def connect(sock):
    try:
        sock.connect(('localhost', 9092))
        return True
    except socket.error:
        print("Connection error")
        return False


check = connect(sock)

while check:
    print("\nWhat do you want to do?\n 1 - run subprocess\n 2 - kill subprocess"
          "\n 3 - get subprocess id\n\n 0 - Exit")
    ch = input()
    if int(ch) == 0:
        sock.close()
        break
    sock.send(str(ch))
