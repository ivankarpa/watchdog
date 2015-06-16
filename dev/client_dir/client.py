import socket
import sys
import string


class Client:
    def send_request(self, request):
        Client.connect(self)
        self.sock.send(str(request))
        Client.wait_for_response(self)

    def wait_for_response(self):
        data = self.sock.recv(1024)
        print(data)

    def run(self):
        print("\nClient: Send request to run subprocess")
        c.send_request('run')

    def kill(self):
        print("\nClient: Send request to kill subprocess")
        c.send_request('kill')

    def connect(self):
        self.sock = socket.socket()
        print("Client: Try to connect")
        try:
            self.sock.connect(('localhost', 9090))
            Client.wait_for_response(self)
        except socket.error:
            print("Client: Warning! Connection error")

    def disconnect(self):
        print("\nClient: Try to turn off server")
        c.send_request('disconnect')

    def status(self):
        print("\nClient: Send request to get process status")
        c.send_request('status')

    def help(self):
        print("\nPlease use following commands as an example\npython client.py -r \n or \npython client.py kill\n")

        print(string.ljust(str(run_list), 25) + '- Run subprocess')
        print(string.ljust(str(kill_list), 25) + '- Kill subprocess')
        print(string.ljust(str(connect_list), 25) + '- Connect to server')
        print(string.ljust(str(disconnect_list), 25) + '- Disconnect from server')
        print(string.ljust(str(status_list), 25) + '- Status of subprocess')


if __name__ == '__main__':
    run_list = ['run', '-r']
    kill_list = ['kill', '-k']
    connect_list = ['connect', '-c']
    disconnect_list = ['disconnect', '-d']
    status_list = ['status', '-s']
    help_list = ['\help', '-h', 'help']
    menu = [run_list, kill_list, connect_list, disconnect_list, status_list, help_list]

    c = Client()

    if len(sys.argv) > 1:
        inp = sys.argv[1]
        if inp in run_list:
            c.run()
        elif inp in kill_list:
            c.kill()
        elif inp in connect_list:
            c.connect()
        elif inp in disconnect_list:
            c.disconnect()
        elif inp in status_list:
            c.status()
        else:
            c.help()
    else:
        c.help()
