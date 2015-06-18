import sys
import time

import client_handler
import subprocess_handler
from daemon import Daemon


class Watchdog(Daemon):
    def run(self):
        self.subprocess = subprocess_handler.Subprocess()
        self.client = client_handler.Client(self.subprocess)

        self.subprocess.start()
        self.client.start()
        while True:
            f = open('./../file.txt', 'w')
            f.write("a")
            f.close()
            time.sleep(1)


if __name__ == '__main__':
    watchdog = Watchdog('/home/ivankarpa/GitProjects/watchdog/dev/wd/daemon-example.pid')

    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            watchdog.start()
        elif 'stop' == sys.argv[1]:
            watchdog.stop()
        elif 'restart' == sys.argv[1]:
            watchdog.restart()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print("usage: %s start|stop|restart" % sys.argv[0])
        sys.exit(2)
