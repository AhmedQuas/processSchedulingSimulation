class fcfs:
    """
        FCFS algorithm definition
        Methods: \n
        exec_fcfs_list(): split process_list to single queues and pass it to fcfs_alg()\n
        fcfs_alg(): this method is queue scheduler and executer \n
        get_finished_queue(): return list of finished process \n
        Attributes: \n
        process_list(list): list of process queues to be executed \n
        finished_queue(list): list of finished process queues \n
    """

    def __init__(self, process_list):
        """
            Create a fcfs algorithm object \n
            Parameters: \n
            process_list(list): list of queues of process to be executed\n
        """
        self.process_list = process_list
        self.finished_queue = []

    def exec_fcfs_list(self):
        for process_set in self.process_list:
            self.fcfs_alg(process_set)

    def fcfs_alg(self, process_waiting):
        """
            This method is queue scheduler and executer \n
            Parameters: \n
            process_waiting(list): list of process to be scheduled and executed\n
        """
        cpu_clock = 0
        local_finished_queue = []
        while len(process_waiting) is not 0:
            proc = process_waiting[0]
            cpu_clock += 1

            if proc.exec_start is None:
                proc.exec_start = cpu_clock

            proc.remain -= 1

            if proc.remain is 0:
                proc.exec_stop = cpu_clock
                local_finished_queue.append(proc)
                del process_waiting[0]
        self.finished_queue.append(local_finished_queue)

    def get_finished_queue(self):
        return self.finished_queue
