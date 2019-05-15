import os.path
import importlib.util


path_to_scripts = os.path.dirname(os.path.realpath(__file__))
path_to_scripts = os.path.join(path_to_scripts, 'BanAction.py')
spec1 = importlib.util.spec_from_file_location("BanAction.BanAction", path_to_scripts)
ban_action = importlib.util.module_from_spec(spec1)
spec1.loader.exec_module(ban_action)


class CheckingAllowedTimeInterval(ban_action.BanAction):

    def __init__(self, user, current_time):
        """
        """
        super().__init__(user)
        self.__CurrentTime = current_time

    def is_triggered(self):
        """

        :return:
        """
        if self.__CurrentTime > (self.user.start_session_time + self.user.work_seconds_delay):
            return True
        else:
            return False





