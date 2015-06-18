import os
import subprocess
import sys
import signal
import threading
import time


class Subprocess(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True

    def run(self):
        while True:
            time.sleep(1)
            if os.path.exists('.lock'):
                self.pipe.wait()
                os.remove('.lock')

    def start_subprocess(self):
        if os.path.exists('.lock'):
            return "Subprocess is already started. PID: {0}".format(self.pipe.pid)
        else:
            self.file = "./../subprocess/subprocess.py"
            self.pipe = subprocess.Popen([sys.executable, self.file])
            self.lock_file = open('.lock', 'w')
            return "Subprocess successfully started. PID: {0}".format(self.pipe.pid)

    def stop_subprocess(self):
        if os.path.exists('.lock'):
            try:
                os.kill(self.pipe.pid, signal.SIGTERM)
                self.pipe.wait(3)
            except subprocess.TimeoutExpired:
                os.kill(self.pipe.pid, signal.SIGKILL)
            return "Subprocess stopped"
        else:
            return "Subprocess not started"

    def execute_command(self, command):
        if command == "start":
            return self.start_subprocess()
        elif command == "stop":
            return self.stop_subprocess()
        elif command == "status":
            return "Subprocess is started" if os.path.exists('.lock') else "Subprocess does not work"
