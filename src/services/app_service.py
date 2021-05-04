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
