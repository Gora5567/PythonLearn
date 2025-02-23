from helper import *


def task1():
    print('Hello Python!'[2])


def task2():
    print('Hello Python!'[2])


def task3():
    print('Hello Python!'[0:2])
    print('Hello Python!'[:2])


def task4():
    print('Hello Python!'[6:7] + 'at' + 'h')

for f in {task1, task2, task3, task4}:
    run(f)