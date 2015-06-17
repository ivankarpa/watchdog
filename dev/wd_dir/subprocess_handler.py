import os
import subprocess
import sys
import signal
import threading


class Subprocess(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def start_subprocess(self):
        if not self.is_started():
            self.lock_file = open('.lock', 'w')
            self.file = "./../subprocess_dir/subprocess.py"
            self.pipe = subprocess.Popen([sys.executable, self.file])
            return "Subprocess successfully started"
        else:
            return "Subprocess is already working"

    def is_started(self):
        if os.path.exists('.lock'):
            return True
        else:
            return False

    def kill_subprocess(self):
        if self.is_started():
            os.kill(self.pipe.pid, signal.SIGKILL)
            os.remove('.lock')
            return "Subprocess killed"
        else:
            return "Subprocess does not work"


    def execute_command(self, command):
        if command == "start":
            return self.start_subprocess()
        elif command == "kill":
            return self.kill_subprocess()
        elif command == "status":
            return "Subprocess is already working" if self.is_started() else "Subprocess does not work"
