import os
import subprocess
import signal
import threading
import time
import sys

sys.path.append('../common/')
import watchdog_config


class Subprocess(threading.Thread):
    def __init__(self, logger):
        threading.Thread.__init__(self)

        self.logger = logger
        self.process_id = None
        self.config = watchdog_config.WatchdogConfig('../wd/watchdog.cfg')
        _, self.subprocess_file = self.config.get_option('subprocess', 'subprocess_file')
        self.stop_signal = False
        self.sleepEvent = threading.Event()

    def run(self):
        while not self.stop_signal:
            if self.process_id:
                if self.pipe.poll() is not None:
                    self.process_id = None
                    while self.process_id is None:
                        self.start_subprocess()
            self.sleepEvent.wait(1)

    def stop(self):
        self.stop_signal = True
        self.stop_subprocess()
        self.sleepEvent.set()

    def start_subprocess(self):
        if self.process_id is not None:
            message = "Subprocess is already started. PID: {0}".format(self.process_id)
            self.logger.warning(message)
            return message
        else:
            self.file = "../subprocess/" + self.subprocess_file
            self.pipe = subprocess.Popen([sys.executable, self.file])
            if self.pipe.pid is not None:
                self.process_id = self.pipe.pid
                message = "Subprocess successfully started. PID: {0}".format(self.process_id)
                self.logger.message(message)
                return message
            else:
                message = "Unsuccessful attempt to start subprocess"
                self.logger.error(message)
                return message

    def stop_subprocess(self):
        if self.process_id:
            try:
                os.kill(self.process_id, signal.SIGTERM)
                self.pipe.wait(3)
            except subprocess.TimeoutExpired:
                os.kill(self.process_id, signal.SIGKILL)
            self.process_id = None
            message = "Subprocess stopped"
            self.logger.message(message)
            return message
        elif not self.stop_signal:
            message = "Subprocess not started"
            self.logger.warning(message)
            return message

    def subprocess_status(self):
        if self.process_id:
            message = "Subprocess is started. PID: {0}".format(self.process_id)
            self.logger.message(message)
            return message
        else:
            message = "Subprocess not started"
            self.logger.message(message)
            return message

    def execute_command(self, command):
        if command == "start":
            return self.start_subprocess()
        elif command == "stop":
            return self.stop_subprocess()
        elif command == "status":
            return self.subprocess_status()
