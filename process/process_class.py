"""
    Process class declaration
"""


class Process:
    def __init__(self, exec_time):
        self.exec_time = exec_time
        self.remain = exec_time
        self.exec_start = -1
        self.exec_stop = -1
    
    def is_finished(self):
        return self.remain == 0
