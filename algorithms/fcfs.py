class fcfs:
    """FCFS algorithm definition"""

    def __init__(self, process_list):
        self.process_list = process_list
        self.finished_queue = []

    def exec_fcfs_list(self):
        for process_set in self.process_list:
            self.fcfs_alg(process_set)

    def fcfs_alg(self, process_waiting):
        cpu_clock = 0
        while len(process_waiting) is not 0:
            proc = process_waiting[0]
            cpu_clock += 1

            if proc.exec_start is -1:
                proc.exec_start = cpu_clock

            proc.remain -= 1

            if proc.remain is 0:
                proc.exec_stop = cpu_clock
                self.finished_queue.append(proc)
                del process_waiting[0]






