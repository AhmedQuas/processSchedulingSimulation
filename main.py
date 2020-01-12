from process.get_process import *
from algorithms.fcfs import *
from algorithms.lcfs import *
from algorithms.sjf import *

# generate_process('process_file.txt', 1, 20)

all_process = read_process('process_file.txt')

#fcfs_alg = fcfs(all_process)
#fcfs_alg.exec_fcfs_list()

#lcfs_alg = lcfs(all_process)
#lcfs_alg.exec_lcfs_list()

sjf_alg = sjf(all_process)
sjf_alg.exec_sjf_list()
