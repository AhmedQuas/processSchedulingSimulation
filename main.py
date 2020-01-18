from copy import deepcopy
from process.get_process import *
from algorithms.fcfs import *
from algorithms.lcfs import *
from algorithms.sjf import *
from algorithms.round_robin_fcfs import *

generate_process('process_file.txt', 1, 20)

all_process = read_process('process_file.txt')

fcfs_alg = fcfs(deepcopy(all_process))
fcfs_alg.exec_fcfs_list()

lcfs_alg = lcfs(deepcopy(all_process))
lcfs_alg.exec_lcfs_list()

sjf_alg = sjf(deepcopy(all_process))
sjf_alg.exec_sjf_list()

rr_alg = RoundRobin(deepcopy(all_process), 5)
rr_alg.exec_rr_list()
print('done')
