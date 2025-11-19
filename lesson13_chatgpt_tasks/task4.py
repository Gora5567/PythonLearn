def draw_pyramid(n):
    width = n + n - 1
    value_part = 1

    for i in range(1, n + 1):
        emptySide = int((width - value_part) / 2)
        # empty cell count in the row

        print(" " * emptySide + "*" * value_part + " " * emptySide)
        value_part += 2
