import os.path
import importlib.util
import time

path_to_scripts = os.path.dirname(os.path.realpath(__file__))
path_to_scripts = os.path.join(path_to_scripts, 'BanAction.py')
spec1 = importlib.util.spec_from_file_location("BanAction.BanAction", path_to_scripts)
ban_action = importlib.util.module_from_spec(spec1)
spec1.loader.exec_module(ban_action)


class CheckingTimeLimits(ban_action.BanAction):

    def __init__(self, user, current_time):
        """

        """
        super().__init__(user)
        self.__CurrentTime = current_time

    def is_triggered(self):
        """

        :return:
        """
        # tp = self.__time_performance.TimePerformance()
        # current_time = tp.get_utc()
        # lst = time.localtime(current_time)

        lst = time.localtime(self.__CurrentTime)
        if (0 <= lst.tm_hour) & (lst.tm_hour <= 8):
            return True
        else:
            return False




