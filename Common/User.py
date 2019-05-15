import sqlite3


class User:
    """

    """

    def __init__(self, name, blocked_state, offline_permission, work_seconds_delay, start_session_time, current_time):
        """

        :param name:
        :param blocked_state:
        :param offline_permission:
        :param work_seconds_delay:
        :param start_session_time:
        :param current_time:
        """
        self.__Name = name
        if isinstance(name, str) is False:
            raise TypeError()

        self.__BlockedState = blocked_state
        self.__OnlinePermission = offline_permission
        self.__WorkSecondsDelay = work_seconds_delay
        self.__StartSessionTime = start_session_time
        self.__CurrentTime = current_time

    name = property(lambda self: self.__Name)
    """
    """

    @property
    def blocked_state(self):
        """

        :return:
        """
        if self.__BlockedState == 0:
            return False
        else:
            return True

    @blocked_state.setter
    def blocked_state(self, param):
        """

        :param param:
        :return:
        """
        self.__BlockedState = param

    @property
    def offline_permission(self):
        """

        :return:
        """
        if self.__OnlinePermission == 0:
            return False
        else:
            return True

    @offline_permission.setter
    def offline_permission(self, param):
        """

        :param param:
        :return:
        """
        self.__OnlinePermission = param

    @property
    def work_seconds_delay(self):
        """

        :return:
        """
        return self.__WorkSecondsDelay

    @work_seconds_delay.setter
    def work_seconds_delay(self, param):
        """

        :param param:
        :return:
        """
        self.__WorkSecondsDelay = param

    @property
    def start_session_time(self):
        """

        :return:
        """
        return self.__StartSessionTime

    @start_session_time.setter
    def start_session_time(self, param):
        """

        :param param:
        :return:
        """
        self.__StartSessionTime = param

    @property
    def current_time(self):
        """

        :return:
        """
        return self.__CurrentTime

    @current_time.setter
    def current_time(self, param):
        """

        :param param:
        :return:
        """
        self.__CurrentTime = param

    @staticmethod
    def create_user(db_instance, user):
        """

        :param db_instance:
        :param user:
        :return:
        """
        try:
            db_instance.cursor.execute("""
                                        CREATE TABLE IF NOT EXISTS 
                                        users (
                                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                                             user_name TEXT,
                                             isBlocked INTEGER, 
                                             workOnline INTEGER,
                                             sessionSecondsDelay INTEGER,
                                             startTime REAL,
                                             currentTime REAL
                                             )
                                  """)
            db_instance.connection.commit()
        except sqlite3.Error as ex:
            pass  # print(ex)
        db_instance.cursor.execute("""
                                        SELECT count(*) FROM 
                                        users 
                                        WHERE user_name = ?""",
                                   (user.name,))
        data = db_instance.cursor.fetchone()[0]
        if data == 0:
            try:
                db_instance.cursor.execute("""INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?)""", (
                                                                                              None,
                                                                                              user.name,
                                                                                              user.blocked_state,
                                                                                              user.offline_permission,
                                                                                              user.work_seconds_delay,
                                                                                              user.start_session_time,
                                                                                              user.current_time))
                db_instance.connection.commit()
            except sqlite3.Error as ex:
                pass  # print(ex)

    @staticmethod
    def get_user(db_instance, user_name):
        """

        :param user_name:
        :param db_instance:
        :return:
        """
        try:
            db_instance.cursor.execute("""SELECT 
                                                user_name,
                                                isBlocked,
                                                workOnline,
                                                sessionSecondsDelay,
                                                startTime,
                                                currentTime
                                                FROM users WHERE user_name=:UserName""", {"UserName": user_name})

            db_instance.connection.commit()
            row = db_instance.cursor.fetchone()
            getting_user = User(row[0], row[1], row[2], row[3], row[4], row[5])
            return getting_user
        except sqlite3.Error as ex:
            pass  # print(ex)

    @staticmethod
    def update_user(db_instance, user):
        """

        :param user:
        :param db_instance:
        :return:
        """
        try:
            db_instance.cursor.execute("""UPDATE users SET
                                                isBlocked = ?,
                                                workOnline = ?,
                                                sessionSecondsDelay = ?,
                                                startTime = ?,
                                                currentTime = ?
                                                WHERE user_name = ?""", (
                                                                            user.blocked_state,
                                                                            user.work_seconds_delay,
                                                                            user.work_seconds_delay,
                                                                            user.start_session_time,
                                                                            user.current_time,
                                                                            user.name
                                                                         ))

            db_instance.connection.commit()
        except sqlite3.Error as ex:
            pass  # print(ex)
