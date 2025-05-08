from helpers.helper import *
from lesson13_chatgpt_tasks import task1, task2


input_data = int(input("Enter number which indicates square size"))
input_data1 = int(input("Enter number which indicates what number will the multiplication"
                        " table go up to"))

runner(task1, input_data)
runner(task2, input_data1)