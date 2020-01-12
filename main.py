from process.get_process import *
from algorithms.fcfs import *

# generate_process('process_file.txt', 1, 20)

all_process = read_process('process_file.txt')

fcfs_alg = fcfs(all_process)
fcfs_alg.exec_fcfs_list()

