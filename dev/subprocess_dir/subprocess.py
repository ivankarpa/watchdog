__author__ = 'ivankarpa'
import time


while True:
    f = open ('/home/ivankarpa/PycharmProjects/WD2/dev/subprocess_dir/file.txt','w')
    f.write("a")
    time.sleep(1)
    f.close()
    print("d1")