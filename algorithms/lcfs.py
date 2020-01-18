class lcfs:
    """LCFS algorithm definition"""

    def __init__(self, process_list):
        self.process_list = process_list
        self.finished_queue = []

    def exec_lcfs_list(self):
        for process_set in self.process_list:
            self.lcfs_alg(process_set)

    def lcfs_alg(self, process_waiting):
        cpu_clock = 0
        local_finished_queue = []
        while len(process_waiting) is not 0:
            proc = process_waiting[-1]
            cpu_clock += 1

            if proc.exec_start is None:
                proc.exec_start = cpu_clock

            proc.remain -= 1

            if proc.remain is 0:
                proc.exec_stop = cpu_clock
                local_finished_queue.append(proc)
                del process_waiting[-1]
        self.finished_queue.append(local_finished_queue)

    def get_finished_queue(self):
        return self.finished_queue
