import os.path
import importlib.util


class LimitingUser:
    """

    """

    def __init__(self ):
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

        # self.__User = user
        # self.__DB = db

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

        # self.__DB.blocked(True)

    def recover_user(self, user):
        """

        :param user:
        :param st_time:
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

        # user.blocked_state = False
        # self.__DB.blocked(False)
        # user.start_session_time = st_time
        # user.current_time = st_time

    def logoff_all_users(self):
        """
            :param user:
            :param st_time:
            :return:
        """
        ps_logoff_all_users_path = self.__ps_dir
        ps_logoff_all_users_path = os.path.join(ps_logoff_all_users_path, "Logoff-AllUsers.ps1")
        run_ps_scripts = self.__windows_ps_user_operation.RunPowerShellScript()
        run_ps_scripts.run_script(ps_logoff_all_users_path)

        # user.blocked_state = False
        # self.__DB.blocked(False)
        # user.start_session_time = st_time
        # user.current_time = st_time

if __name__ == "__main__":
    limit_user = LimitingUser()
    # limit_user.recover_user("Ogurchuk")
    #limit_user.baning_user("Ogurchuk")
    limit_user.logoff_all_users()

