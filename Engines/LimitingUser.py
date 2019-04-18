import os.path
import importlib.util


class LimitingUser:
    """

    """

    def __init__(self):
        """

        """
        path_to_run_ps_script = os.path.dirname(os.path.realpath(__file__))
        path_to_run_ps_script = path_to_run_ps_script + os.sep + ".." + os.sep
        path_to_run_ps_script = os.path.abspath(path_to_run_ps_script)
        path_to_run_ps_script = os.path.join(path_to_run_ps_script, 'PS')

        self.__ps_dir = path_to_run_ps_script

        path_to_run_ps_script = os.path.join(path_to_run_ps_script, 'Windows_PS_User_Operation.py')

        spec = importlib.util.spec_from_file_location("Windows_PS_User_Operation.RunPowerShellScript",
                                                      path_to_run_ps_script)
        self.__windows_ps_user_operation = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.__windows_ps_user_operation)

        path_to_common_scripts = os.path.dirname(os.path.realpath(__file__))
        path_to_common_scripts = path_to_common_scripts + os.sep + ".." + os.sep
        path_to_common_scripts = os.path.join(path_to_common_scripts, 'Common')
        path_to_common_scripts = os.path.join(path_to_common_scripts, 'SQLighte_Performance.py')
        spec = importlib.util.spec_from_file_location("SQLighte_Performance.DBPerformance", path_to_common_scripts)
        self.__db_performance = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.__db_performance)

        self.__db_path = os.path.join(os.path.expanduser(os.getenv('USERPROFILE')), "my_sqlite_3.db")
        # self.__db_path = "my_sqlite.db"

    def db_path(self):
        return self.__db_path

    def baning_user(self, user):
        """

        :param user_name:
        :return:
        """
        ps_ban_user_path = self.__ps_dir
        ps_ban_user_path = os.path.join(ps_ban_user_path, "BanUser.ps1")
        run_ps_scripts = self.__windows_ps_user_operation.RunPowerShellScript()
        run_ps_scripts.run_script(ps_ban_user_path)

        ps_logoff_user_path = self.__ps_dir
        ps_logoff_user_path = os.path.join(ps_logoff_user_path, "LogoffUser.ps1")
        run_ps_scripts = self.__windows_ps_user_operation.RunPowerShellScript()
        run_ps_scripts.run_script(ps_logoff_user_path)

        db = self.__db_performance.DBPerformance(self.__db_path)
        db.crete_tables()
        db.blocked(True)
        db.close()

    def recover_user(self, user, st_time):
        """

        :param user:
        :return:
        """
        ps_ban_user_path = self.__ps_dir
        ps_ban_user_path = os.path.join(ps_ban_user_path, "RecoverUserFromBan.ps1")
        run_ps_scripts = self.__windows_ps_user_operation.RunPowerShellScript()
        run_ps_scripts.run_script(ps_ban_user_path)

        ps_logoff_user_path = self.__ps_dir
        ps_logoff_user_path = os.path.join(ps_logoff_user_path, "LogoffUser.ps1")
        run_ps_scripts = self.__windows_ps_user_operation.RunPowerShellScript()
        run_ps_scripts.run_script(ps_logoff_user_path)

        db = self.__db_performance.DBPerformance(self.__db_path)
        db.crete_tables()
        db.blocked(False)
        db.start_time(st_time)
        db.cur_time(st_time)
        db.close()

if __name__ == "__main__":
    limit_user = LimitingUser()
    # limit_user.recover_user("Ogurchuk")
    limit_user.baning_user("Ogurchuk")

