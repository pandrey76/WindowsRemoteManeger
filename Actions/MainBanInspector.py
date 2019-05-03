import os.path
import importlib.util
import types

path_to_scripts = os.path.dirname(os.path.realpath(__file__))
path_to_scripts = os.path.join(path_to_scripts, 'BanAction.py')
spec1 = importlib.util.spec_from_file_location("BanAction.BanAction", path_to_scripts)
ban_action = importlib.util.module_from_spec(spec1)
spec1.loader.exec_module(ban_action)


class MainBanInspector(ban_action.BanAction):
    def __init__(self, db):
        """

        """
        super().__init__(db)
        self.__MainArray = []

        path_to_common_scripts = os.path.dirname(os.path.realpath(__file__))
        path_to_common_scripts = os.path.join(path_to_common_scripts, 'CheckingTimeLimits.py')
        spec = importlib.util.spec_from_file_location("CheckingTimeLimits.CheckingTimeLimits", path_to_common_scripts)
        obj_1 = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(obj_1)

        self.__MainArray.append(obj_1.CheckingTimeLimits(self.data_base_handle))

        path_to_common_scripts = os.path.dirname(os.path.realpath(__file__))
        path_to_common_scripts = os.path.join(path_to_common_scripts, 'CheckingAllowedTimeInterval.py')
        spec = importlib.util.spec_from_file_location("CheckingAllowedTimeInterval.CheckingAllowedTimeInterval",
                                                      path_to_common_scripts)
        obj_2 = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(obj_2)

        self.__MainArray.append(obj_2.CheckingAllowedTimeInterval(self.data_base_handle))

        path_to_common_scripts = os.path.dirname(os.path.realpath(__file__))
        path_to_common_scripts = os.path.join(path_to_common_scripts, 'CheckingSetSystemTimeByUser.py')
        spec = importlib.util.spec_from_file_location("CheckingSetSystemTimeByUser.CheckingSetSystemTimeByUser",
                                                      path_to_common_scripts)
        obj_3 = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(obj_3)

        self.__MainArray.append(obj_3.CheckingSetSystemTimeByUser(self.data_base_handle))

    def is_worked(self):
        """

        :return:
        """
        for obj in self.__MainArray:
            if obj.is_worked():
                return True
        return False




