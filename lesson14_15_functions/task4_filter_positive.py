x = int(input("please enter a number: "))

def filter_positive(numbers):
    return [num for num in numbers if num > 0]

filter_positive(x)