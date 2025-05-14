from helpers.helper import *
from lesson13_chatgpt_tasks import task1, task2, task3, task4


input_data = int(input("Enter number which indicates square size:\n"))
runner(task1.print_square, input_data)

input_data1 = int(input("Enter number which indicates what number will the multiplication"
                        " table go up to\n"))
runner(task2.multiplication_table, input_data1)

input_data2 = int(input("Enter number which indicates what number will the number stairs go up to\n"))
runner(task3.number_stairs, input_data2)

input_data3 = int(input("Enter number which indicates what number will the number pyramide go up to\n"))
runner(task4.draw_pyramid, input_data3)