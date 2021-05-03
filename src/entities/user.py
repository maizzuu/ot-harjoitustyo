class User:
    """Class that depicts a User.

    Attributes:
        username: String that represents the users username.
        password: String that represents the users password.
    """
    def __init__(self, username:str, password:str):
        """Class constructor that creates a new user.

        Args:
            username (str): String that represents the users username.
            password (str): String that represents the users password.
        """
        self.username = username
        self.password = password
