import helper


helper.start_task(1)

numbers = [
    1.23456, 12.1, 123.4567, 0.98765,
    1234.5678, 56.789, 0.1, 3.14159
]

print("{:>15.4f} {:>15.4f} {:>15.4f} {:>15.4f}".format(numbers[0], numbers[1], numbers[2], numbers[3]))
print("{:>15.4f} {:>15.4f} {:>15.4f} {:>15.4f}".format(numbers[4], numbers[5], numbers[6], numbers[7]))

helper.end_task(1)
helper.end_task(1)
helper.end_task(1)