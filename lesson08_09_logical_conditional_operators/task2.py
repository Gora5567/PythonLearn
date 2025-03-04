# Check here --> README.md to see the assignment

from helper import *

start_task(2)

number = input("Enter an integer number: ")
checker = int(number)
if checker % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

end_task(2)