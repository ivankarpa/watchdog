import os
import subprocess
import signal
import threading
import time
import sys


class Subprocess(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.process_id = None

    def run(self):
        while True:
            if self.process_id:
                if self.pipe.poll() is not None:
                    self.process_id = None
                    self.start_subprocess()
            time.sleep(1)

    def start_subprocess(self):
        if self.process_id is not None:
            return "Subprocess is already started. PID: {0}".format(self.process_id)
        else:
            self.file = "./../subprocess/subprocess.py"
            self.pipe = subprocess.Popen([sys.executable, self.file])
            self.process_id = self.pipe.pid
            return "Subprocess successfully started. PID: {0}".format(self.process_id)

    def stop_subprocess(self):
        if self.process_id:
            try:
                os.kill(self.process_id, signal.SIGTERM)
                self.pipe.wait(3)
            except subprocess.TimeoutExpired:
                os.kill(self.process_id, signal.SIGKILL)
            self.process_id = None
            return "Subprocess stopped"
        else:
            return "Subprocess not started"

    def subprocess_status(self):
        if self.process_id:
            return "Subprocess is started. PID: {0}".format(self.process_id)
        else:
            return "Subprocess does not work"

    def execute_command(self, command):
        if command == "start":
            return self.start_subprocess()
        elif command == "stop":
            return self.stop_subprocess()
        elif command == "status":
            return self.subprocess_status()
