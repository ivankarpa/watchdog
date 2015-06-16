import time


class Subprocess:
    def run_subprocess(self):
        while True:
            f = open('/home/ivankarpa/PycharmProjects/WD2/dev/subprocess_dir/file.txt', 'w')
            f.write("a")
            f.close()
            time.sleep(1)
            print("sp1")


if __name__ == '__main__':
    Subprocess().run_subprocess()
