import os
import subprocess
import signal
import threading
import time
import sys


class Subprocess(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.pipe_id = 0;
        if os.path.exists('.lock'):
            os.remove('.lock')

    def run(self):
        while True:
            if os.path.exists('.lock'):
                if not str(self.pipe.poll()) == "None":
                    os.remove('.lock')
                    self.start_subprocess()
            time.sleep(1)

    def start_subprocess(self):
        if os.path.exists('.lock'):
            return "Subprocess is already started. PID: {0}".format(self.pipe_id)
        else:
            self.file = "./../subprocess/subprocess.py"
            self.pipe = subprocess.Popen([sys.executable, self.file])
            self.pipe_id = self.pipe.pid
            self.lock_file = open('.lock', 'w')
            return "Subprocess successfully started. PID: {0}".format(self.pipe_id)

    def stop_subprocess(self):
        if os.path.exists('.lock'):
            try:
                os.kill(self.pipe_id, signal.SIGTERM)
                self.pipe.wait(3)
            except subprocess.TimeoutExpired:
                os.kill(self.pipe_id, signal.SIGKILL)
            os.remove('.lock')
            return "Subprocess stopped"
        else:
            return "Subprocess not started"

    def about_subprocess(self):
        if os.path.exists('.lock'):
            return "Subprocess is started. PID: {0}".format(self.pipe_id)
        else:
            return "Subprocess does not work"

    def execute_command(self, command):
        if command == "start":
            return self.start_subprocess()
        elif command == "stop":
            return self.stop_subprocess()
        elif command == "about":
            return self.about_subprocess()
