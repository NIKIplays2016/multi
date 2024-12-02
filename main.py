import multiprocessing as mp
from multiprocessing import Queue
from random import randint
from time import sleep

tick = 0.01

def a(q):
    while True:
        q.put(randint(0, 100))
        sleep(tick * 10)
        a(q)


def b(q):
    while True:
        if not q.empty():
            print(q.get())
        sleep(tick * 1)


def main():
    q = Queue()

    p1 = mp.Process(target=a, args=(q,))
    p2 = mp.Process(target=b, args=(q,))

    p1.start()
    p2.start()


if __name__ == '__main__':
    main()



