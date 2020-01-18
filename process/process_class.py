class Process:
    """Process class definition """

    def __init__(self, exec_time):
        self.exec_time = exec_time
        self.remain = exec_time
        self.exec_start = None
        self.exec_stop = None
    
    def is_finished(self):
        return self.remain is 0

    def get_waiting_time(self):
        return self.exec_start

    def get_processing_time(self):
        return self.exec_stop
