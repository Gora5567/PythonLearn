# Check here --> README.md to see the assignment
from helper import *
from helpers.helper import *

def k1(a):
    sum_even = 0

    for num in range(10, 31, 2):
        sum_even += num

    print("Sum of even numbers from 10 to 30:", sum_even)


runner(k1)
