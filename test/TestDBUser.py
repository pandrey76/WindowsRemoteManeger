import unittest
import os.path
import importlib.util
import time


class TestDBUser(unittest.TestCase):

    def setUp(self) :
        """

        """
        path_to_scripts = os.path.dirname(os.path.realpath(__file__))
        path_to_scripts = path_to_scripts + os.sep + ".." + os.sep
        path_to_scripts = os.path.abspath(path_to_scripts)
        path_to_scripts = os.path.join(path_to_scripts, 'Common')
        path_to_scripts = os.path.join(path_to_scripts, 'User.py')
        spec1 = importlib.util.spec_from_file_location("User.User", path_to_scripts)
        self.__UserModule = importlib.util.module_from_spec(spec1)
        spec1.loader.exec_module(self.__UserModule)
        self.__UserName = "Admin3"

        path_to_scripts = os.path.dirname(os.path.realpath(__file__))
        path_to_scripts = path_to_scripts + os.sep + ".." + os.sep
        path_to_scripts = os.path.abspath(path_to_scripts)
        path_to_common_scripts = os.path.join(path_to_scripts, 'Common')
        path_to_common_scripts = os.path.join(path_to_common_scripts, 'SQLighte_Performance.py')
        spec2 = importlib.util.spec_from_file_location("SQLighte_Performance.DBPerformance", path_to_common_scripts)
        db_module = importlib.util.module_from_spec(spec2)
        spec2.loader.exec_module(db_module)
        self.__DB = db_module.DBPerformance(os.path.join(os.path.expanduser(os.getenv('USERPROFILE')),
                                                         "my_sqlite_0.db"))

    def test_create_and_read_user(self):
        """

        :return:
        """

        user1 = self.__UserModule.User(self.__UserName,
                                       True,         # blocked_state
                                       False,        # offline_permission
                                       7200,         # work_seconds_delay
                                       time.time(),  # start_session_time
                                       time.time() + 200     # current_time
                                       )
        self.__UserModule.User.create_user(self.__DB, user1)

        self.assertTrue('FOO'.isupper())
        # self.assertFalse('Foo'.isupper())

    def test_read_user_from_db(self):
        """

        :return:
        """
        user_name = "Admin1"
        user = self.__UserModule.User.get_user(self.__DB, user_name)
        self.assertEqual(user.name, user_name)
        self.assertEqual(user.blocked_state, True)
        self.assertEqual(user.offline_permission, False)
        self.assertEqual(user.work_seconds_delay, 7200)
        # self.assertTrue(user.name, user_name)

    def test_update_user_from_db(self):
        """

        :return:
        """
        user_name = "Admin1"
        user = self.__UserModule.User.get_user(self.__DB, user_name)
        user.blocked_state = False
        user.offline_permission = True
        user.work_seconds_delay = 3600
        self.__UserModule.User.update_user(self.__DB, user
                                           )
        user = self.__UserModule.User.get_user(self.__DB, user_name)
        self.assertEqual(user.name, user_name)
        self.assertEqual(user.blocked_state, False)
        self.assertEqual(user.offline_permission, True)
        self.assertEqual(user.work_seconds_delay, 3600)

if __name__ == '__main__':
    unittest.main()

