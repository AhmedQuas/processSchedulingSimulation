from statistic.hist_plot_req import *


class AlgorithmStatistic:
    """
        AlgorithmStatistic definition
        Methods: \n
        save_results(): split process_list to single queues and pass it to fcfs_alg()\n
        generate_stats(): this method is queue scheduler and executer \n
        get_all_stats(): return list of finished process \n
        get_queue_stats(): \n
        get_waiting_stat(): \n
        get_processing_stat(): \n
        print_summary(): \n
        generate_histplot(): \n
        Attributes: \n
        finished_process(list): list of process finished queues \n
        filename(str):  \n
    """

    def __init__(self, finished_process, stat_filename, algorithm_name):
        """
            Create a algorithm statistic object \n
            Parameters: \n
            finished_process(list): list of finished process queues from algoritm objects(ex. fcfs, sjf) \n
            stat_filename(str): name of file where results will be saved \n
            algorithm_name(str): name displayed in result file and in histogram \n
        """
        self.finished_process = finished_process
        self.filename = stat_filename
        self.process_stats = []
        self.whole_stats = {}
        self.alg_name = algorithm_name

    def save_results(self):
        """
            Save statistics results to file \n
            Parameters: \n
            None
        """
        file = open(self.filename, 'w')
        set_counter = 1
        for stat_result in self.process_stats:
            file.write('{}.\n-Average process waiting time: {}\n-Average process processing time: {}\n'
                       .format(set_counter,
                               stat_result['waiting_aver'],
                               stat_result['processing_aver']))
            set_counter += 1

        file.write('\n\t+===============+\n\t| Total results |\n\t+===============+\n')
        file.write(self.alg_name + '\n')
        file.write('Average process waiting time: {}\nAverage process processing time: {}\n'.format(
                    self.whole_stats['waiting_aver'],
                    self.whole_stats['processing_aver']))
        file.close()

    def generate_stats(self):
        """
            Call this method to generate, save & print results \n
            Parameters: \n
            None
        """
        self.get_queue_stats()
        self.get_all_stats()
        self.save_results()
        self.print_summary()

    def get_all_stats(self):
        """
            Calc final results. Displayed at last lines in file & displayed on console \n
            Parameters: \n
            None
        """
        n = len(self.process_stats)
        for stat_type in ["waiting_aver", "processing_aver"]:
            sum_stat_type = 0
            for proc in self.process_stats:
                sum_stat_type += proc[stat_type]
            self.whole_stats[stat_type] = round(sum_stat_type/n, 2)

    def get_queue_stats(self):
        """
            Calc final queue results. Displayed at last lines in file & displayed on console \n
            Parameters: \n
            None
        """
        for process_set in self.finished_process:
            stat = {}
            stat['waiting_aver'] = self.get_waiting_stat(process_set)
            stat['processing_aver'] = self.get_processing_stat(process_set)
            self.process_stats.append(stat)

    def get_waiting_stat(self, process_set):
        """
            Calc final waiting results per queue \n
            Parameters: \n
            process_set(list): queue of process to calculation of the process waiting average
        """
        n = len(process_set)
        waiting_sum = 0
        for process in process_set:
            waiting_sum += process.get_waiting_time()
        average = waiting_sum/n
        return round(average, 2)

    def get_processing_stat(self, process_set):
        """
            Calc final processing results per queue \n
            Parameters: \n
            process_set(list): queue of process to calculation of the process waiting average
        """
        n = len(process_set)
        waiting_sum = 0
        for process in process_set:
            waiting_sum += process.get_processing_time()
        average = waiting_sum / n
        return round(average, 2)

    def print_summary(self):
        """
            Print summary in console \n
            Parameters: \n
            None
        """
        print('Summary of ' + self.alg_name + ' algorithm')
        print('Average process waiting time: {}\nAverage process processing time: {}'.format(
            self.whole_stats['waiting_aver'],
            self.whole_stats['processing_aver']))
        print('----------------------\n')

    def generate_histplot(self):
        """
            Generate histogram using matplotlib & pandas packages \n
            Parameters: \n
            None
        """
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

        histogram.plot.hist(bins=5, rwidth=0.85, color=color)
        plt.title('Histogram of 100 average process waiting time queues in \n' + self.alg_name)
        plt.xlabel('Average waiting time')
        plt.ylabel('Count')
        plt.grid(axis='y', alpha=0.75)
        plt.show()
        print(self.alg_name + ' histogram generated')
