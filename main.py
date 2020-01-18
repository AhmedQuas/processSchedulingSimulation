from copy import deepcopy
from process.get_process import *
from algorithms.fcfs import *
from algorithms.lcfs import *
from algorithms.sjf import *
from algorithms.round_robin_fcfs import *
from statistic.statistic import *

#generate_process('process_file.txt', 1, 20)

all_process = read_process('process_file.txt')

fcfs_alg = fcfs(deepcopy(all_process))
fcfs_alg.exec_fcfs_list()
fcfs_statistic = AlgorithmStatistic(fcfs_alg.get_finished_queue(), 'fcfs.txt')
fcfs_statistic.generate_stats()

lcfs_alg = lcfs(deepcopy(all_process))
lcfs_alg.exec_lcfs_list()
lcfs_statistic = AlgorithmStatistic(lcfs_alg.get_finished_queue(), 'lcfs.txt')
lcfs_statistic.generate_stats()

sjf_alg = sjf(deepcopy(all_process))
sjf_alg.exec_sjf_list()
sjf_statistic = AlgorithmStatistic(sjf_alg.get_finished_queue(), 'sjf.txt')
sjf_statistic.generate_stats()

rr_alg_05 = RoundRobin(deepcopy(all_process), 0.5)
rr_alg_05.exec_rr_list()
rr_alg_05_statistic = AlgorithmStatistic(rr_alg_05.get_finished_queue(), 'rr_05.txt')
rr_alg_05_statistic.generate_stats()

rr_alg_10 = RoundRobin(deepcopy(all_process), 1)
rr_alg_10.exec_rr_list()
rr_alg_10_statistic = AlgorithmStatistic(rr_alg_10.get_finished_queue(), 'rr_10.txt')
rr_alg_10_statistic.generate_stats()

rr_alg_15 = RoundRobin(deepcopy(all_process), 1.5)
rr_alg_15.exec_rr_list()
rr_alg_15_statistic = AlgorithmStatistic(rr_alg_15.get_finished_queue(), 'rr_15.txt')
rr_alg_15_statistic.generate_stats()
print('done')
