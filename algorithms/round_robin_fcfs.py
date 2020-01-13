class RoundRobin:
    """Round Robin (FCFS) algorithm definition"""

    def __init__(self, process_list, quant):
        self.process_list = process_list
        self.finished_queue = []
        self.quant = quant

    def exec_rr_list(self):
        for process_set in self.process_list:
            self.rr_alg(process_set)

    def rr_alg(self, process_waiting):
        cpu_clock = 0
        index = 0
        while len(process_waiting) is not 0:
            quant = self.quant
            if len(process_waiting) - index <= 0:
                index = 0

            proc = process_waiting[index]

            if proc.exec_start is -1:
                proc.exec_start = cpu_clock

            cpu_clock += quant

            if proc.remain - quant <= 0:
                quant = quant-proc.remain
                proc.remain = 0
                proc.exec_stop = cpu_clock - quant
                self.finished_queue.append(proc)
                del process_waiting[index]

                #get new process & execute the rest of quant
                if len(process_waiting) is not 0:
                    proc = process_waiting[0]
                    proc.exec_start = cpu_clock - quant
                else:
                    return

            proc.remain -= quant
            index += 1
