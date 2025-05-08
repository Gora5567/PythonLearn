from helpers.helper import *
from lesson13_chatgpt_tasks import task1, task2


# input_data = int(input("Enter number which indicates square size:\n"))
# runner(task1.print_square, input_data)

input_data1 = int(input("Enter number which indicates what number will the multiplication"
                        " table go up to\n"))
runner(task2.multiplication_table, input_data1)