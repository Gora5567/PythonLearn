# Check here --> README.md to see the assignment
from helper import start_task, end_task

start_task(2)

number = input("Enter an integer number: ")
# Проверяем, является ли вод целым числом
if number.isdigit() or (number[0] == '-' and number[1:].isdigit()):
    checker = int(number)

    if checker % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("It is not an integer")

end_task(2)


def main():
    return None
