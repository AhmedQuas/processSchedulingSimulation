class RoundRobin:
    """
        Round Robin (FCFS) algorithm definition
        Methods: \n
        exec_rr_list(): split process_list to single queues and pass it to rr_alg()\n
        rr_alg(): this method is queue scheduler and executer \n
        get_finished_queue(): return list of finished process \n
        Attributes: \n
        process_list(list): list of process queues to be executed \n
        finished_queue(list): list of finished process queues \n
    """

    def __init__(self, process_list, quant):
        """
            Create a Round Robin (FCFS) algorithm object \n
            Parameters: \n
            process_list(list): list of queues of process to be executed \n
            quant(int/float): quant number used in Round Robin algorithm
        """
        self.process_list = process_list
        self.finished_queue = []
        self.quant = quant

    def exec_rr_list(self):
        for process_set in self.process_list:
            self.rr_alg(process_set)

    def rr_alg(self, process_waiting):
        """
            This method is queue scheduler and executer \n
            Parameters: \n
            process_waiting(list): list of process to be scheduled and executed\n
        """
        cpu_clock = 0
        index = 0
        local_finished_queue = []
        while len(process_waiting) is not 0:
            quant = self.quant
            # detect list overflow & start from 0
            if len(process_waiting) - index <= 0:
                index = 0

            proc = process_waiting[index]

            if proc.exec_start is None:
                proc.exec_start = cpu_clock

            if proc.remain - quant <= 0:
                cpu_clock += proc.remain
                proc.remain = 0
                proc.exec_stop = cpu_clock
                local_finished_queue.append(proc)
                del process_waiting[index]
                continue

            cpu_clock += quant
            proc.remain -= quant
            index += 1
        self.finished_queue.append(local_finished_queue)

    def get_finished_queue(self):
        return self.finished_queue
