import os
import subprocess
import sys
import signal
import time
import threading



class Subprocess(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run_subprocess(self):

        if not Subprocess.is_subprocess_work(self):

            print("not work")
            self.s_file = "/home/ivankarpa/PycharmProjects/WD2/dev/subprocess_dir/subprocess.py"
            self.pipe = subprocess.Popen([sys.executable, self.s_file])
        else:
            print("work")
            pass


    def is_subprocess_work(self):

        try:
            if self.pipe.pid:
                return True
        except:
            return False

    def status(self):
        try:
            os.kill(self.pipe.pid, 0)
        except:
            print("FALSE1")
        else:
            print("TRUE1")


    def kill_subprocess(self):
        print("__________KILLING__________")
        os.kill(self.pipe.pid, signal.SIGKILL)


    def managing_the_subprocess(self, choise):
        if choise == "run":
            self.run_subprocess()
        elif choise == "kill":
            self.kill_subprocess()
        elif choise == "status":
            self.status()
        elif choise == '':
            pass

