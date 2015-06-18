import socket
import sys

import config


class Client:
    def __init__(self):
        self.sock = socket.socket()
        self.config = config.Config()

    def execute_command(self, command):
        try:
            host_found, host = self.config.get_option('connect', 'host')
            if not host_found:
                return "Host not set in config"
            _, port = self.config.get_option('connect', 'port')
            self.sock.connect((host, int(port)))
            self.sock.send(command.encode())
            response = self.sock.recv(1024).decode()
            self.sock.close()
            return response
        except ConnectionRefusedError:
            return "Connection to {0}:{1} refused".format(host, port)
        except socket.error as msg:
            return "Exception! errcode: {0}, message: {1}. Server: {2}:{3}".format(msg[0], msg[1], host, port)

    def start(self):
        return self.execute_command('start')

    def stop(self):
        return self.execute_command('stop')

    def about(self):
        return self.execute_command('about')


def help():
    print("\nPlease use following commands as an example\npython client.py -r \n or \npython client.py kill\n")
    print('{:18}{}'.format(str(start_list), "- Start subprocess"))
    print('{:18}{}'.format(str(stop_list), "- Stop subprocess"))
    print('{:18}{}'.format(str(about_list), "- About subprocess"))


if __name__ == '__main__':
    start_list = ['start', '-r']
    stop_list = ['stop', '-s']
    about_list = ['about', '-a']

    client = Client()

    if len(sys.argv) > 1:
        inp = sys.argv[1]
        if inp in start_list:
            print(client.start())
        elif inp in stop_list:
            print(client.stop())
        elif inp in about_list:
            print(client.about())
        else:
            help()
    else:
        help()
