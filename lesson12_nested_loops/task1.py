def chess():
    size = 8  # размер доски 8x8

    for row in range(size):

        for col in range(size):

            if (row + col) % 2 == 0:
                print('#', end='')

            else:
                print(' ', end='')

        print()