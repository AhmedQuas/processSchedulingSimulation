class AlgorithmStatistic:

    def __init__(self, finished_process, stat_filename):
        self.finished_process = finished_process
        self.filename = stat_filename
        self.process_stats = []
        self.whole_stats = {}

    def save_results(self):
        return "Not implemented method"

    def generate_stats(self):
        self.get_queue_stats()
        self.get_all_stats()
        # self.save_results()

    def get_all_stats(self):
        n = len(self.process_stats)
        for stat_type in ["waiting_aver", "processing_aver"]:
            sum_stat_type = 0
            for proc in self.process_stats:
                sum_stat_type += proc[stat_type]
            self.whole_stats[stat_type] = sum_stat_type/n

    def get_queue_stats(self):
        for process_set in self.finished_process:
            stat = {}
            stat['waiting_aver'] = self.get_waiting_stat(process_set)
            stat['processing_aver'] = self.get_processing_stat(process_set)
            self.process_stats.append(stat)

    def get_waiting_stat(self, process_set):
        n = len(process_set)
        waiting_sum = 0
        for process in process_set:
            waiting_sum += process.get_waiting_time()
        average = waiting_sum/n
        return average

    def get_processing_stat(self, process_set):
        n = len(process_set)
        waiting_sum = 0
        for process in process_set:
            waiting_sum += process.get_processing_time()
        average = waiting_sum / n
        return average
