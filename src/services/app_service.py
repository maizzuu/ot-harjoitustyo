from entities.month import Month
from entities.user import User
from repositories.user_repository import user_repository as default_user_repo
from repositories.month_repository import month_repository as default_month_repo

class InvalidInputError(Exception):
    pass

class UsernameExistsError(Exception):
    pass

class AppService:
    """Sovelluslogiikasta vastaava luokka."""

    def __init__(self, month_repo=default_month_repo, user_repo=default_user_repo):
        """Class constructor. Creates a new AppService.

        Args:
            month_repo (MonthRepository, optional):
                Object with the methods of the UserRepository class. Defaults to default_month_repo.
            user_repo (UserRepository, optional):
                Object with the methods of the MonthRepository class. Defaults to default_user_repo.
        """
        self._user = None
        self._month_repo = month_repo
        self._user_repo = user_repo

    def login(self, username:str, password:str):
        """Method used to log in to the app.

        Args:
            username (str): Username
            password (str): Password

        Raises:
            InvalidInputError: Error for when username and password do not match.

        Returns:
            User: User that logged in.
        """
        user = self._user_repo.find_by_username(username)

        if not user or user.password != password:
            raise InvalidInputError("Invalid username or password")

        self._user = user

        return user

    def logout(self):
        """ Method used to log out of the app.
        """

        self._user = None

    def current_user(self):
        """Return the current user.

        Returns:
            User: The current user.
        """
        return self._user

    def get_months(self):
        """Returns a list of months that belong to the current user.
            If there isn't a current user, returns an empty list.

        Returns:
            list: Months that belong to the current user.
        """
        if not self._user:
            return []

        months = self._month_repo.find_by_username(self._user.username)

        return months

    def log(self, month:str, year:str, category:str, amount:int):
        """Logs expenses for a certain month,
        if the month doesn't exist,
        it will create the new month.

        Args:
            month (str): month
            year (str): year
            category (str): category of the spending
            amount (int): amount spent

        Returns:
            Month: The month in question.
        """
        month = month[0].upper()+month[1:]
        category = category.lower()
        log_month = self._month_repo.find_by_username_month_year(self._user.username, month, year)

        if not log_month:
            log_month = Month(self._user.username, month, year, 0, 0, 0, 0, 0, 0)
            self._month_repo.create(log_month)

        return self._month_repo.spend(log_month, category, amount)

    def create(self, username, password, login=True):
        """Creates a new user and logs them in if needed.

        Args:
            username (str): User's username
            password (str): User's password
            login (bool, optional): Tells whether the user will be logged in. Defaults to True.

        Raises:
            UsernameExistsError: Raised if the username already exists.

        Returns:
            User: The user that has just been created.
        """
        existing = self._user_repo.find_by_username(username)

        if existing:
            raise UsernameExistsError(f'Username {username} already exists')

        user = self._user_repo.create(User(username, password))

        if login:
            self._user = user

        return user

app_service = AppService()
