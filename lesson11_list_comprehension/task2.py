from helpers.helper import make_int_array


def task2(choice):
    digits = make_int_array(20)

    if choice == 1:
        # without
        odd_digits = []

        for num in digits:
            if num % 2 != 0:
                odd_digits.append(num)

        print("without\n", odd_digits)

    elif choice == 2:
        # with
        odd_digits = [num for num in digits if num % 2 != 0]

        print("with list comprehension\n", odd_digits)

    else:
        print("wrong input")
