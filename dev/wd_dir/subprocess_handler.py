import os
import subprocess
import sys
import signal
import threading

class Subprocess(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run_subprocess(self):
        self.file = "/home/ivankarpa/GitProjects/watchdog/dev/subprocess_dir/subprocess.py"
        self.pipe = subprocess.Popen([sys.executable, self.file])
        return "Subprocess started"

    def status(self):
        try:
            os.kill(self.pipe.pid, 0)
            return "Subprocess is already running"
        except:
            return "Subprocess does not work"

    def kill_subprocess(self):
        os.kill(self.pipe.pid, signal.SIGKILL)
        return "Subprocess killed"

    def execute_command(self, command):
        if command == "run":
            return self.run_subprocess()
        elif command == "kill":
            return self.kill_subprocess()
        elif command == "status":
            return self.status()
