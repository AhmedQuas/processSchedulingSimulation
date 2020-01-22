from copy import deepcopy
from process.get_process import *
from algorithms.fcfs import *
from algorithms.lcfs import *
from algorithms.sjf import *
from algorithms.round_robin_fcfs import *
from statistic.statistic import *
from statistic.hist_plot_req import *

# generate file with process execution time
#generate_process('process_file.txt', 1, 20)

# read process execution file
all_process = read_process('process_file.txt')

# make a copy of process execution time list & pass to fcfs object constructor
fcfs_alg = fcfs(deepcopy(all_process))
# schedule and execute queues of process
fcfs_alg.exec_fcfs_list()
# make some statistics
fcfs_statistic = AlgorithmStatistic(fcfs_alg.get_finished_queue(), 'fcfs.txt', 'FCFS')
# print final algorithm statistics
fcfs_statistic.generate_stats()

lcfs_alg = lcfs(deepcopy(all_process))
lcfs_alg.exec_lcfs_list()
lcfs_statistic = AlgorithmStatistic(lcfs_alg.get_finished_queue(), 'lcfs.txt', 'LCFS')
lcfs_statistic.generate_stats()

sjf_alg = sjf(deepcopy(all_process))
sjf_alg.exec_sjf_list()
sjf_statistic = AlgorithmStatistic(sjf_alg.get_finished_queue(), 'sjf.txt', 'SJF')
sjf_statistic.generate_stats()

rr_alg_05 = RoundRobin(deepcopy(all_process), 0.5)
rr_alg_05.exec_rr_list()
rr_alg_05_statistic = AlgorithmStatistic(rr_alg_05.get_finished_queue(), 'rr_05.txt', 'Round Robin with q = 0.5')
rr_alg_05_statistic.generate_stats()

rr_alg_10 = RoundRobin(deepcopy(all_process), 1)
rr_alg_10.exec_rr_list()
rr_alg_10_statistic = AlgorithmStatistic(rr_alg_10.get_finished_queue(), 'rr_10.txt', 'Round Robin with q = 1.0')
rr_alg_10_statistic.generate_stats()

rr_alg_15 = RoundRobin(deepcopy(all_process), 1.5)
rr_alg_15.exec_rr_list()
rr_alg_15_statistic = AlgorithmStatistic(rr_alg_15.get_finished_queue(), 'rr_15.txt', 'Round Robin with q = 1.5')
rr_alg_15_statistic.generate_stats()

#Check installed packeges & generate histplot
print("Do you want to generate histogram to each algorithm ? y/n")
ans = input()
if ans is 'y' and check_requirements():
    fcfs_statistic.generate_histplot()
    lcfs_statistic.generate_histplot()
    sjf_statistic.generate_histplot()
    rr_alg_05_statistic.generate_histplot()
    rr_alg_10_statistic.generate_histplot()
    rr_alg_15_statistic.generate_histplot()

print('Done')
