import sys
from signal import signal, pause, SIGINT, SIGTERM, SIG_IGN, SIGHUP

import client_handler
import subprocess_handler
from daemon import Daemon

sys.path.append('../common/')
import watchdog_config

sys.path.append('../shared/')
import logger


class Watchdog(Daemon):
    def __init__(self, pid_file, log_file):
        Daemon.__init__(self, pid_file)
        self.log_file = log_file
        self.logger = logger.Logger()
        self.subprocess = subprocess_handler.Subprocess(self.logger)
        self.client = client_handler.Client(self.subprocess, self.logger)

    def run(self):
        self.setSignalHandlers()
        self.logger.initialize(self.log_file)
        self.logger.message("Watchdog started")
        self.subprocess.start()
        self.client.start()

        pause()

        self.client.stop()
        self.subprocess.stop()
        self.logger.message("Watchdog stopped")
        self.logger.finalize()

    def signalHandler(self, signum, frame):
        pass

    def setSignalHandlers(self):
        signal(SIGTERM, self.signalHandler)
        signal(SIGINT, self.signalHandler)
        # ignore next signals to prevent stopping of daemon
        for sig in (SIGHUP,):
            signal(sig, SIG_IGN)


if __name__ == '__main__':
    config = watchdog_config.WatchdogConfig('watchdog.cfg')
    pid_file_found, pid_file = config.get_option('daemon', 'pid_file')
    if not pid_file_found:
        sys.exit("pid file not set in config")

    _, log_file = config.get_option('log', 'log_file')
    watchdog = Watchdog(pid_file, log_file)

    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            watchdog.start()
        elif 'stop' == sys.argv[1]:
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
        print("usage: %s start|stop|restart|status" % sys.argv[0])
        sys.exit(2)
