import unittest
import os
import sys
import time

sys.path.append('./../wd/')


class WatchDogTest(unittest.TestCase):
    START_WATCHDOG = "cd ../wd && ./wd start"
    STOP_WATCHDOG = "cd ../wd && ./wd start"
    RESTART_WATCHDOG = "cd ../wd && ./wd start"

    def setUp(self):
        os.system(self.START_WATCHDOG)

    def tearDown(self):
        if self.get_pid():
            os.system(self.STOP_WATCHDOG)

    def get_pid(self):
        try:
            time.sleep(0.5)
            pid_file = open('../wd/daemon_pid_file.pid', 'r')
            pid = pid_file.read()
            pid_file.close()
            return int(pid)
        except FileNotFoundError:
            pass

    def test_check_successfully_start(self):
        try:
            os.kill(self.get_pid(), 0)
        except OSError:
            self.fail()

    def test_check_successfully_stop(self):
        temporary_pid = self.get_pid()
        os.system(self.STOP_WATCHDOG)
        try:
            os.kill(temporary_pid, 0)
        except OSError:
            return True
        else:
            self.fail()

    def test_check_successfully_restart(self):
        pid_before_restart = self.get_pid()
        os.system(self.RESTART_WATCHDOG)
        pid_after_restart = self.get_pid()
        self.assertNotEqual(pid_before_restart, pid_after_restart)


if __name__ == '__main__':
    unittest.main()
