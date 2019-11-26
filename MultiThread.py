from threading import *
from time import sleep


class Hello(Thread):
    def run(self):
        for i in range(6):
            print("Hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(6):
            print("Hi")
            sleep(1)


t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)
t2.start()

# Join is used to ask Main Thread to wait for t1 Thread to finish their tasks
t1.join()
t2.join()

print("Bye")
