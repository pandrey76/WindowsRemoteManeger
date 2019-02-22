import os.path
import importlib.util

path_to_run_ps_script = os.getcwd()
path_to_run_ps_script = os.path.join(path_to_run_ps_script, 'PS')

ps_dir = path_to_run_ps_script

path_to_run_ps_script = os.path.join(path_to_run_ps_script, 'Windows_PS_User_Operation.py')

spec = importlib.util.spec_from_file_location("Windows_PS_User_Operation.RunPowerShellScript", path_to_run_ps_script)
windows_ps_user_operation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(windows_ps_user_operation)


class LimitingUser:
    """

    """

    def baning_user(self, user):
        """

        :param user_name:
        :return:
        """
        ps_ban_user_path = ps_dir
        ps_ban_user_path = os.path.join(ps_ban_user_path, "BanUser.ps1")
        run_ps_scripts = windows_ps_user_operation.RunPowerShellScript()
        run_ps_scripts.run_script(ps_ban_user_path)

        ps_logoff_user_path = ps_dir
        ps_logoff_user_path = os.path.join(ps_logoff_user_path, "LogoffUser.ps1")
        run_ps_scripts = windows_ps_user_operation.RunPowerShellScript()
        run_ps_scripts.run_script(ps_logoff_user_path)


    def recover_user(self, user):
        """

        :param user:
        :return:
        """
        ps_ban_user_path = ps_dir
        ps_ban_user_path = os.path.join(ps_ban_user_path, "RecoverUserFromBan.ps1")
        run_ps_scripts = windows_ps_user_operation.RunPowerShellScript()
        run_ps_scripts.run_script(ps_ban_user_path)

        ps_logoff_user_path = ps_dir
        ps_logoff_user_path = os.path.join(ps_logoff_user_path, "LogoffUser.ps1")
        run_ps_scripts = windows_ps_user_operation.RunPowerShellScript()
        run_ps_scripts.run_script(ps_logoff_user_path)


if __name__ == "__main__":
    limit_user = LimitingUser()
    limit_user.recover_user("Ogurchuk")
    # limit_user.baning_user("Ogurchuk")

