class sjf:
    """SJF algorithm definition"""

    def __init__(self, process_list):
        self.process_list = process_list
        self.finished_queue = []

    def sort_sjf_list(self, proc_set):
        n = len(proc_set)
        for i in range(n):
            for j in range(n-i-1):
                if proc_set[j].remain > proc_set[j+1].remain:
                    proc_set[j], proc_set[j+1] = proc_set[j+1], proc_set[j]

        return proc_set

    def exec_sjf_list(self):
        for process_set in self.process_list:
            process_set = self.sort_sjf_list(process_set)
            self.sjf_alg(process_set)

    def sjf_alg(self, process_waiting):
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