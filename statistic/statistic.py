from statistic.hist_plot_req import *


class AlgorithmStatistic:

    def __init__(self, finished_process, stat_filename, algorith_name):
        self.finished_process = finished_process
        self.filename = stat_filename
        self.process_stats = []
        self.whole_stats = {}
        self.alg_name = algorith_name

    def save_results(self):
        file = open(self.filename, 'w')
        set_counter = 1
        for stat_result in self.process_stats:
            file.write('{}.\n-Average process waiting time: {}\n-Average process processing time: {}\n'
                       .format(set_counter,
                               stat_result['waiting_aver'],
                               stat_result['processing_aver']))
            set_counter += 1

        file.write('\n\t+===============+\n\t| Total results |\n\t+===============+\n\n')
        file.write(self.alg_name)
        file.write('Average process waiting time: {}\nAverage process processing time: {}\n'.format(
                    self.whole_stats['waiting_aver'],
                    self.whole_stats['processing_aver']))
        file.close()

    def generate_stats(self):
        self.get_queue_stats()
        self.get_all_stats()
        self.save_results()
        self.print_summary()

    def get_all_stats(self):
        n = len(self.process_stats)
        for stat_type in ["waiting_aver", "processing_aver"]:
            sum_stat_type = 0
            for proc in self.process_stats:
                sum_stat_type += proc[stat_type]
            self.whole_stats[stat_type] = round(sum_stat_type/n, 2)

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
        return round(average, 2)

    def get_processing_stat(self, process_set):
        n = len(process_set)
        waiting_sum = 0
        for process in process_set:
            waiting_sum += process.get_processing_time()
        average = waiting_sum / n
        return round(average, 2)

    def print_summary(self):
        print('Summary of ' + self.alg_name + ' algorithm')
        print('Average process waiting time: {}\nAverage process processing time: {}'.format(
            self.whole_stats['waiting_aver'],
            self.whole_stats['processing_aver']))
        print('----------------------\n')

    def generate_histplot(self):
        if not check_requirements():
            print('Not this time, another check')
            return False
        # Now i can import required packages without error
        import matplotlib.pyplot as plt
        import pandas as pd

        hist_data = []
        colors_dist = {
                'FCFS': '#0A1747',
                'LCFS': '#0029FA',
                'SJF': '#8D07F6'
        }

        #default color for undefined in dictionary color
        color = '#D4DBF5'
        if self.alg_name in colors_dist:
            color = colors_dist[self.alg_name]

        for stat in self.process_stats:
            hist_data.append(stat['waiting_aver'])

        histogram = pd.Series(hist_data)

        histogram.plot.hist(grid=False, bins=5, rwidth=0.85, color=color)
        plt.title('Histogram of 100 average process waiting time queues in \n' + self.alg_name)
        plt.xlabel('Average waiting time')
        plt.ylabel('Count')
        plt.grid(axis='y', alpha=0.75)
        plt.show()
        print(self.alg_name + ' histogram generated')
