

class BanAction:
    """
    """
    def __init__(self, user):
        """

        :param user:
        """
        self.__User = user

    user = property(lambda self: self.__User)
    """
    """
    def is_triggered(self):
        """
        """
        raise Exception("No implement")

