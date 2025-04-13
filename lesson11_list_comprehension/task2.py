def task2(a):
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #without
    odd_digits = []
    for num in digits:
        if num % 2 != 0:
            odd_digits.append(num)
    print("without\n", odd_digits)
    #with
    odd_digits = [num for num in digits if num % 2 != 0]
    print("with list comprehension\n", odd_digits)


