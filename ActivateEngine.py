import os.path
import importlib.util

# path_to_run_ps_script = '..'
# path_to_run_ps_script += os.path.sep
path_to_run_ps_script = ""
path_to_run_ps_script = os.path.join(path_to_run_ps_script, 'Mailing')

ps_dir = path_to_run_ps_script

path_to_run_ps_script = os.path.join(path_to_run_ps_script, 'Reading_from_Gmail.py')


spec = importlib.util.spec_from_file_location("Reading_from_Gmail.Mailing", path_to_run_ps_script)
reading_from_gmail = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reading_from_gmail)


# path_to_run_ps_script = '..'
# path_to_run_ps_script += os.path.sep
path_to_run_ps_script = ""
path_to_run_ps_script = os.path.join(path_to_run_ps_script, 'Engines')

ps_dir = path_to_run_ps_script

path_to_run_ps_script = os.path.join(path_to_run_ps_script, 'LimitingUser.py')


spec = importlib.util.spec_from_file_location("LimitingUser.LimitingUser", path_to_run_ps_script)
limiting_user= importlib.util.module_from_spec(spec)
spec.loader.exec_module(limiting_user)


class ActivateEngine:
    """

    """

    def run(self):
        """

        :return:
        """
        mail = reading_from_gmail.Mailing()
        mail.read_unseen_mail()
        body = mail.mail_body
        if body is None:
            return
        else:
            lim_user = limiting_user.LimitingUser()
            if str(body).find("BAN") != -1:
                lim_user.baning_user("Ogurchuk")
            elif str(body).find("RECOVERY") != -1:
                lim_user.recover_user("Ogurchuk")
            else:
                return



if __name__ == "__main__":
    limit_user = ActivateEngine()
    limit_user.run()
