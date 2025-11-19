from helpers.helper import runner
from lesson11_list_comprehension.task1 import task1
from lesson11_list_comprehension.task2 import task2

input_data = int(input("Enter number which indicates variant of the"
                       " first task (1 or 2):"))
input_data2 = int(input("Enter number which indicates variant of the"
                        " second task (1 or 2):"))

runner(task1, input_data)
# runner(task1)
runner(task2, input_data2)
