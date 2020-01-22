class Process:
    """
        Process class definition
        Methods: \n
        is_finished(): return True if process is finished \n
        get_waiting_time(): return process waiting time \n
        get_processing_time(): return process processing time \n
        Attributes: \n
        exec_time(int): process total execution time \n
        remain(int): remained execution time
        exec_start(int): time when process start to executing \n
        exec_stop(int): time when process finish to executing
    """

    def __init__(self, exec_time):
        """
            Create a process object \n
            Parameters: \n
            exec_time (int): process total execution time\n
        """
        self.exec_time = exec_time
        self.remain = exec_time
        self.exec_start = None
        self.exec_stop = None
    
    def is_finished(self):
        return self.remain is 0

    def get_waiting_time(self):
        return self.exec_stop - self.exec_time + 1

    def get_processing_time(self):
        return self.exec_stop
