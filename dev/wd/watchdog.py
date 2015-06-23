import sys

import client_handler
import subprocess_handler
from daemon import Daemon
import config


class Watchdog(Daemon):
    def __init__(self, pid_file):
        Daemon.__init__(self, pid_file)
        self.subprocess = subprocess_handler.Subprocess()
        self.client = client_handler.Client(self.subprocess)

    def run(self):
        self.subprocess.start()
        self.client.start()

    def stop_subprocess(self):
        self.subprocess.stop_subprocess()


if __name__ == '__main__':
    try:
        config = config.Config('watchdog.cfg')
    except ValueError:
        sys.exit(1)

    _, pid_file = config.get_option('daemon', 'pid_file')

    watchdog = Watchdog('./' + pid_file)

    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            watchdog.start()
        elif 'stop' == sys.argv[1]:
            watchdog.stop_subprocess()
            watchdog.stop()

        elif 'restart' == sys.argv[1]:
            watchdog.restart()
        elif 'status' == sys.argv[1]:
            pid = watchdog.get_pid()
            if pid:
                print('Watchdog is running [{0}]'.format(pid))
            else:
                print('Watchdog is stopped')
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print("usage: %s start|stop|restart" % sys.argv[0])
        sys.exit(2)
