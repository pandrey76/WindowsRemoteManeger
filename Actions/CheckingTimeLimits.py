import os.path
import importlib.util
import time

path_to_scripts = os.path.dirname(os.path.realpath(__file__))
spec = importlib.util.spec_from_file_location("BanAction.BanAction", path_to_scripts)
ban_action = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ban_action)


class CheckingTimeLimits(ban_action):

    def __init__(self, db):
        """

        """
        super().__init__(db)
        path_to_common_scripts = os.path.dirname(os.path.realpath(__file__))
        path_to_common_scripts = os.path.join(path_to_common_scripts, 'TimePerformance.py')
        spec = importlib.util.spec_from_file_location("TimePerformance.TimePerformance", path_to_common_scripts)
        self.__time_performance = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.__time_performance)

    def is_worked(self):
        """

        :return:
        """
        tp = self.__time_performance.TimePerformance()
        current_time = tp.get_utc()
        lst = time.localtime(current_time)
        if (0 <= lst.tm_hour) & (lst.tm_hour <= 8):
            return True




