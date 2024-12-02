import multiprocessing as mp
from multiprocessing import Queue

from random import randint
from time import sleep
import math

tick = 0.1

def create1(q):
    while True:
        q.put(randint(0, 1))
        sleep(tick)

def create2(q):
    while True:
        q.put(randint(0, 1))
        sleep(tick)

def create3(q):
    while True:
        q.put(randint(0, 1))
        sleep(tick)


def read(q, q2):
    boolstr = ""
    loc_string = ""
    while True:
        if not q.empty():
            x = q.get()
            boolstr += str(x)
            if len(boolstr) == 7:
                letter = chr(int(boolstr, 2))
                print(letter+"\n")
                print(boolstr+"\n\n")
                q2.put(letter)
                boolstr = ""
                if q2.qsize() > 20:
                    while not q2.empty():
                        loc_string += q2.get()
                    print(loc_string+"\n\n")
                    loc_string = ""
                    sleep(3)

        sleep(tick/10)


def main():
    q = Queue()
    q2 = Queue()

    p1 = mp.Process(target=create1, args=(q,))
    p2 = mp.Process(target=create2, args=(q,))
    p3 = mp.Process(target=create3, args=(q,))

    p4 = mp.Process(target=read, args=(q,q2))

    p1.start()
    p2.start()
    p3.start()
    p4.start()


if __name__ == '__main__':
    main()



