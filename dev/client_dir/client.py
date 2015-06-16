import socket
import sys
import string

class Client:
    def __init__(self):
        self.sock = socket.socket()

    def execute_command(self, command):
        try:
            self.sock.connect(('localhost', 9090))
            self.sock.send(command.encode())
            response = self.sock.recv(1024).decode()
            print(response)
            self.sock.close()
            return response
        except socket.error as msg:
            return "Exception! errcode: {0}, message: {1}".format(msg[0], msg[1])

    def run(self):
        return self.execute_command('run')

    def kill(self):
        return self.execute_command('kill')

    def status(self):
        return self.execute_command('status')


def help():
    print("\nPlease use following commands as an example\npython client.py -r \n or \npython client.py kill\n")
    print(string.ljust(str(run_list), 25) + '- Run subprocess')
    print(string.ljust(str(kill_list), 25) + '- Kill subprocess')
    print(string.ljust(str(status_list), 25) + '- Status of subprocess')


if __name__ == '__main__':
    run_list = ['run', '-r']
    kill_list = ['kill', '-k']
    status_list = ['status', '-s']
    help_list = ['\help', '-h', 'help']

    client = Client()

    if len(sys.argv) > 1:
        inp = sys.argv[1]
        if inp in run_list:
            client.run()
        elif inp in kill_list:
            client.kill()
        elif inp in status_list:
            client.status()
        else:
            help()
    else:
        help()
