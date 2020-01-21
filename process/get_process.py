from random import uniform
from os import path
from process.process_class import *


def generate_process(file_name, start_scope=1, end_scope=20, repeat=100, process_number=100):

    # ask if user wants to override file
    if path.isfile(file_name):
        print("Given file already exist, do you want to override it? y/n")
        ans = input()
        if ans is not 'y':
            return False

    file = open(file_name, 'w')
    # final process generation
    for line in range(repeat):
        items = []
        for item in range(process_number):
            items.append(round(uniform(start_scope, end_scope), 0))
        file.write(' '.join([str(el) for el in items]) + '\n')

    file.close()
    return True


def read_process(file_name):
    """
        Read process executing time form file \n
        Parameters:

        file_name : name of file with exec time data

        Returns:

        list: list of Process

       """

    # ask if user wants to override file
    if not path.isfile(file_name):
        print("Given file don`t exist, I will create it")
        generate_process(file_name)

    file = open(file_name, 'r')
    process_exec_time = []
    process_list = []

    for line in file:
        process_line = line.split(' ')
        # list comprehension to transform str to int by float[generated in generate_process()]
        process_line = [int(float(x)) for x in process_line]
        process_exec_time.append(process_line)

    # create Process object list
    for exec_row in process_exec_time:
        process_row = []
        for exec_time in exec_row:
            process_row.append(Process(exec_time))
        process_list.append(process_row)

    return process_list
