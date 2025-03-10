# Check here --> README.md to see the assignment
from helper import *

start_task(2)

number = input("Enter an integer number: ")

if number.isdigit() or (number[0] == '-' and number[1:].isdigit()):  # Проверяем, является ли ввод целым числом
    checker = int(number)

    if checker % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("It is not an integer")

end_task(2)