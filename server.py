__author__ = 'ivankarpa'
import sys
import time

def turn_off():
    pass

def turn_on():
    pass

def restart():
    turn_off()
    time.sleep(3)
    turn_on()

word = sys.stdin.readline().rstrip()
filename = sys.stdin.readline().rstrip()

try:
    with open(filename, "rb") as fh:
        while True:
            current = fh.readline()
            if not current:
                break
            if (word in current):
                print("find: {0} {1}".format(filename, word))
except:
    pass
