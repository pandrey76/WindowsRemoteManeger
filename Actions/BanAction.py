

class BanAction:
    """
    """
    def __init__(self, db):
        """

        :param db:
        """
        self.__DB = db

    data_base_handle = property(lambda self: self.__DB)
    """
    """
    def is_triggered(self):
        """
        """
        raise Exception("No implement")

