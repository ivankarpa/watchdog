import client_handler
import subprocess_handler


class Watchdog:
    def __init__(self):
        self.subprocess = subprocess_handler.Subprocess()
        self.client = client_handler.Client(self.subprocess)

    def Run(self):
            self.subprocess.start()
            self.client.start()


if __name__ == '__main__':
    watchdog = Watchdog()
    watchdog.Run()
