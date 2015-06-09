__author__ = 'ivankarpa'

import os
import subprocess
import sys
import signal
import time
import threading


class Subprocess(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.s_file = ""
        self.pipe = ""

    def run_subprocess(self):
        self.s_file = "/home/ivankarpa/PycharmProjects/WD2/dev/subprocess_dir/subprocess.py"
        self.pipe = subprocess.Popen([sys.executable, self.s_file])
        print(self.pipe.pid)

    def get_subprocess_id(self):
        return self.pipe.pid

    def stop_subprocess(self):
        print("__________STOP__________")
        signal.signal(signal.SIGTERM,)
        print(os.kill(self.pipe.pid, signal.SIGKILL))

    def kill_subprocess(self):
        print("__________KILLING__________")
        time.sleep(4)
        os.kill(self.pipe.pid, signal.SIGKILL)

    def managing_the_subprocess(self, choise):
        if int(choise) == 1:
            self.run_subprocess()
        elif int(choise) == 2:
            self.kill_subprocess()

        elif int(choise) == 3:
            print (self.get_subprocess_id())
        elif int(choise) == 5:
            self.stop_subprocess()
