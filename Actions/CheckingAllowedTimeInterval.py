import os.path
import importlib.util


path_to_scripts = os.path.dirname(os.path.realpath(__file__))
path_to_scripts = os.path.join(path_to_scripts, 'BanAction.py')
spec1 = importlib.util.spec_from_file_location("BanAction.BanAction", path_to_scripts)
ban_action = importlib.util.module_from_spec(spec1)
spec1.loader.exec_module(ban_action)


class CheckingAllowedTimeInterval(ban_action.BanAction):

    def __init__(self, db):
        """

        """
        super().__init__(db)

        path_to_common_scripts = os.path.dirname(os.path.realpath(__file__))
        path_to_common_scripts = path_to_common_scripts + os.sep + ".." + os.sep
        path_to_common_scripts = os.path.join(path_to_common_scripts, 'Common')
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
        seconds_delay = 7200
        start_time = self.data_base_handle.get_start_time()
        if current_time > start_time + seconds_delay:
            return True





