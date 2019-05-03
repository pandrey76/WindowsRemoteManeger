import os.path
import importlib.util
import time


class TimePerformance:
    """

    """

    def __init__(self):
        """

        """
        path_to_common_scripts = os.path.dirname(os.path.realpath(__file__))
        path_to_common_scripts = os.path.join(path_to_common_scripts, 'NTP_Performance.py')
        spec = importlib.util.spec_from_file_location("NTP_Performance.NTPPerformance", path_to_common_scripts)
        self.__ntp_performance_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.__ntp_performance_module)
        self.__ntp_performance = self.__ntp_performance_module.NTPPerformance()

    def get_utc(self):
        """

        :return:
        """

        current_utc = self.__ntp_performance.get_utc()
        if current_utc is None:
            current_utc = time.time()
        return current_utc
