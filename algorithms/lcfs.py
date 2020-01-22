class lcfs:
    """
        LCFS algorithm definition
        Methods: \n
        exec_lcfs_list(): split process_list to single queues and pass it to lcfs_alg()\n
        lcfs_alg(): this method is queue scheduler and executer \n
        get_finished_queue(): return list of finished process \n
        Attributes: \n
        process_list(list): list of process queues to be executed \n
        finished_queue(list): list of finished process queues \n
    """

    def __init__(self, process_list):
        """
            Create a lcfs algorithm object \n
            Parameters: \n
            process_list(list): list of queues of process to be executed\n
        """
        self.process_list = process_list
        self.finished_queue = []

    def exec_lcfs_list(self):
        for process_set in self.process_list:
            self.lcfs_alg(process_set)

    def lcfs_alg(self, process_waiting):
        """
            This method is queue scheduler and executer \n
            Parameters: \n
            process_waiting(list): list of process to be scheduled and executed\n
        """
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
