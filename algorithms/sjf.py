class sjf:
    """
        SJF algorithm definition
        Methods: \n
        sort_sjf_list(): sort process queue from exec_sjf_list(), bubble sort, shortest job is first \n
        exec_sjf_list(): split process_list to single queues and pass it to sjf_alg() \n
        sjf_alg(): this method is queue scheduler and executer \n
        get_finished_queue(): return list of finished process \n
        Attributes: \n
        process_list(list): list of process queues to be executed \n
        finished_queue(list): list of finished process queues \n
    """

    def __init__(self, process_list):
        """
            Create a sjf algorithm object \n
            Parameters: \n
            process_list(list): list of queues of process to be executed\n
        """
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
