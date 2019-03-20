import os.path
import importlib.util


class Engine:
    """

    """
    def __init__(self):
        """

        """
        path_to_run_script = os.path.dirname(os.path.realpath(__file__))
        path_to_run_script = os.path.join(path_to_run_script, 'Mailing')

        path_to_run_script = os.path.join(path_to_run_script, 'Reading_from_Gmail.py')

        spec = importlib.util.spec_from_file_location("Reading_from_Gmail.Mailing", path_to_run_script)
        self.__reeading_from_gmail = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.__reeading_from_gmail)

        path_to_run_script = os.path.dirname(os.path.realpath(__file__))
        path_to_run_script = os.path.join(path_to_run_script, 'Engines')

        path_to_run_script = os.path.join(path_to_run_script, 'LimitingUser.py')

        spec = importlib.util.spec_from_file_location("LimitingUser.LimitingUser", path_to_run_script)
        self.__limiting_user = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.__limiting_user)

        self.__ban_file_path = os.path.join(os.path.expanduser(os.getenv('USERPROFILE')), "ban_timeot.txt")

        self.__ban_timeout = 10

    def remove_ban_file(self):
        """

        :return:
        """
        os.remove(self.__ban_file_path)

    def run(self):
        """

        :return:
        """
        mail = self.__reeading_from_gmail.Mailing()
        if mail.is_online() is False:
            self.do_ban()
            return
        mail.read_unseen_mail()
        body = mail.mail_body
        if body is None:
            return
        else:
            lim_user = self.__limiting_user.LimitingUser()
            if str(body).find("BAN") != -1:
                lim_user.baning_user("Ogurchuk")
            elif str(body).find("RECOVER") != -1:
                lim_user.recover_user("Ogurchuk")
            else:
                return

    def do_ban(self):
        """

        :return:
        """
        num = 0
        try:
            with open(self.__ban_file_path, 'rt') as fh:
                num = int(fh.read())
            if num > self.__ban_timeout:
                limit_user = self.__limiting_user.LimitingUser()
                limit_user.baning_user("Ogurchuk")
                self.remove_ban_file()
                return
        except IOError:
            with open(self.__ban_file_path, 'wt') as fh:
                fh.write('1')
                return
        num += 1
        with open(self.__ban_file_path, 'wt') as fh:
            fh.write(str(num))
            return


if __name__ == "__main__":
    limit_user = Engine()
    limit_user.run()
