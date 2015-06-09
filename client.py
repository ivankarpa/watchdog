__author__ = 'ivankarpa'
import socket

sock = socket.socket()


def connect(sock):
    try:
        sock.connect(('localhost', 9090))
        return True
    except socket.error:
        print("Connection error")
        return False


check = connect(sock)

while check:
    print("\nWhat do you want to do?\n 1 - start server\n 2 - stop server"
          "\n 3 - restart server\n 4 - Info\n\n 0 - Exit")
    ch = input()
    if int(ch) == 0:
        break
    sock.send(str(ch))
    data = sock.recv(1024)
    print(str(data)[2:-1])

sock.close()
