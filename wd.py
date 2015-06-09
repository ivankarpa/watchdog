import os
import subprocess
import sys
import socket
import threading


def work_with_server(number):
    if number == 1:
        return "----------START--------"
    elif number == 2:
        return "----------STOP--------"
    elif number == 3:
        return "----------RESTART--------"
    elif number == 4:
        pass


def client_listener():
    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(1)
    connection, address = sock.accept()
    print (">>>NEW CONNECTION:", address)

    while True:
        data = connection.recv(1024)
        if not data:
            break
        print(">>>Input data:", data)
        connection.send(work_with_server(int(data)))

    connection.close()


def run_server():
    server = os.path.join(os.path.dirname(__file__), "./server.py")
    command = [sys.executable, server]
    pipe = subprocess.Popen(command, stdin=subprocess.PIPE)
    file = "./wd.py"
    word = "pipe"
    pipe.stdin.write(word.encode("utf8") + b"\n")
    pipe.stdin.write(file.encode("utf8") + b"\n")
    pipe.stdin.close()
    pipe.wait()




p1 = threading.Thread(target=client_listener)
p2 = threading.Thread(target=run_server)
p1.start()
p2.start()
