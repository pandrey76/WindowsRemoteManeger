import sqlite3


class DBPerformance:

    def __init__(self, db_path):
        """
        :param db_path:
        """
        self.__DB_Path = db_path
        self.__Connection = sqlite3.connect(db_path)
        self.__Cursor = self.__Connection.cursor()

    connection = property(lambda self: self.__Connection)
    """
    """
    cursor = property(lambda self: self.__Cursor)
    """
    """
    db_path = property(lambda self: self.__DB_Path)
    """
    """

    def close(self):
        if self.__Connection:
            self.__Connection.close()

    def crete_tables(self):
        try:
            self.__Cursor.execute("""
                                        CREATE TABLE users (
                                            id INTEGER PRIMARY KEY,
                                             name TEXT,
                                             isBlocked INTEGER, 
                                             workOnline INTEGER,
                                             sessionSecondsDelay INTEGER,
                                             startTime REAL,
                                             currentTime REAL
                                             )
                                  """)
            self.__Connection.commit()
        except sqlite3.Error as ex:
            pass  # print(ex)

        try:
            self.__Cursor.execute("""INSERT INTO blocked VALUES(?, ?)""", (1, 0))
            self.__Connection.commit()
        except sqlite3.Error as ex:
            pass  # print(ex)

        try:
            self.__Cursor.execute("""CREATE TABLE blocked (id INTEGER PRIMARY KEY, isBlocked INTEGER)""")
            self.__Cursor.execute("""INSERT INTO blocked VALUES(?, ?)""", (1, 0))
            self.__Connection.commit()
        except sqlite3.Error as ex:
            pass  # print(ex)
        try:
            self.__Cursor.execute("""CREATE TABLE timer (id INTEGER PRIMARY KEY, start_time REAL, cur_time REAL)""")
            self.__Cursor.execute("""INSERT INTO timer VALUES(?, ?, ?)""", (1, 0, 0))
            self.__Connection.commit()
        except sqlite3.Error as ex:
            pass  # print(ex)

    def get_user(self, name):
        """

        :param name:
        :return:
        """


    def blocked(self, flag):
        param = int(flag)
        self.__Cursor.execute("""UPDATE blocked SET isBlocked=? WHERE id=?""", (param, 1))
        self.__Connection.commit()

    def get_blocked(self):
        self.__Cursor.execute("SELECT isBlocked FROM blocked WHERE id=:Id", {"Id": 1})
        row = self.__Cursor.fetchone()
        if row[0] == 0:
            return False
        else:
            return True

    def start_time(self, st):
        self.__Cursor.execute("""UPDATE timer SET start_time=? WHERE id=?""", (st, 1))
        self.__Connection.commit()

    def get_start_time(self):
        self.__Cursor.execute("SELECT start_time FROM timer WHERE id=:Id", {"Id": 1})
        row = self.__Cursor.fetchone()
        return row[0]

    def cur_time(self, cur_time):
        self.__Cursor.execute("""UPDATE timer SET cur_time=? WHERE id=?""", (cur_time, 1))
        self.__Connection.commit()

    def get_cur_time(self):
        self.__Cursor.execute("SELECT cur_time FROM timer WHERE id=:Id", {"Id": 1})
        row = self.__Cursor.fetchone()
        return row[0]

    def get_all_times(self):
        self.__Cursor.execute("SELECT start_time, cur_time FROM timer WHERE id=:Id", {"Id": 1})
        row = self.__Cursor.fetchone()
        return row[0], row[1]


if __name__ == '__main__':

    db = DBPerformance("my_sql_db6.db")
    db.crete_tables()
    db.blocked(True)
    block_status = db.get_blocked()
    print(block_status, type(block_status))

    db.start_time(47553.53753)
    st = db.get_start_time()
    print(st, type(st))

    db.cur_time(790.125353)
    ct = db.get_cur_time()
    print(ct, type(ct))

    st1, ct1 = db.get_all_times()
    print(st1, type(st1), ct1, type(ct1))
    db.close()


