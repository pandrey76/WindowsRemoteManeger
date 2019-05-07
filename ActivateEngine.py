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

        path_to_common_scripts = os.path.dirname(os.path.realpath(__file__))
        path_to_common_scripts = os.path.join(path_to_common_scripts, 'Common')
        path_to_common_scripts = os.path.join(path_to_common_scripts, 'SQLighte_Performance.py')
        spec = importlib.util.spec_from_file_location("SQLighte_Performance.DBPerformance", path_to_common_scripts)
        self.__db_performance = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.__db_performance)

        path_to_common_scripts = os.path.dirname(os.path.realpath(__file__))
        path_to_common_scripts = os.path.join(path_to_common_scripts, 'Common')
        path_to_common_scripts = os.path.join(path_to_common_scripts, 'TimePerformance.py')
        spec = importlib.util.spec_from_file_location("TimePerformance.TimePerformance", path_to_common_scripts)
        self.__time_performance = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.__time_performance)

        path_to_common_scripts = os.path.dirname(os.path.realpath(__file__))
        path_to_common_scripts = os.path.join(path_to_common_scripts, 'Actions')
        path_to_common_scripts = os.path.join(path_to_common_scripts, 'MainBanInspector.py')
        spec = importlib.util.spec_from_file_location("MainBanInspector.MainBanInspector", path_to_common_scripts)
        self.__main_ban_inspector = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.__main_ban_inspector)

        self.__DB_Path = os.path.join(os.path.expanduser(os.getenv('USERPROFILE')), "my_sqlite_3.db")

    def remove_ban_file(self):
        """

        :return:
        """
        os.remove(self.__ban_file_path)

    def run(self):
        """

        :return:
        """
        user = "Ogurchuk"
        lim_user = self.__limiting_user.LimitingUser()
        mail = self.__reeading_from_gmail.Mailing()
        tp = self.__time_performance.TimePerformance()
        newest_current_time = tp.get_utc()

        db = self.__db_performance.DBPerformance(self.__DB_Path)
        db.crete_tables()
        if db.get_blocked() is 0:
            if mail.is_online() is False:
                db.close()
                self.do_ban()
                return

            main_ban_inspec = self.__main_ban_inspector.MainBanInspector(db, newest_current_time)
            if main_ban_inspec.is_triggered():
                lim_user.baning_user(user)

            # Check time limits
            # seconds_delay = 100
            # new_ct_time = ntp.get_utc()
            # st_time, cr_time = db.get_all_times()
            #
            # if st_time is None or cr_time is None or int(st_time) is 0:
            #     if new_ct_time is None:
            #         new_ct_time = time.time()
            #     db.start_time(new_ct_time)
            #     db.cur_time(new_ct_time)
            #     db.close()
            #     return
            # if new_ct_time is None:
            #     cr_time += 70
            #     db.cur_time(cr_time)
            #     if cr_time > st_time + seconds_delay:
            #         db.close()
            #         lim_user.baning_user(user)
            #         return
            # else:
            #     if new_ct_time > st_time + seconds_delay:
            #         db.close()
            #         lim_user.baning_user(user)
            #         return
        mail.read_unseen_mail()
        body = mail.mail_body
        if body is None:
            return
        else:
            if str(body).find("BAN") != -1:
                lim_user.baning_user(user)
            elif str(body).find("RECOVER") != -1:
                lim_user.recover_user(user, newest_current_time)
            else:
                # db.close()
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
