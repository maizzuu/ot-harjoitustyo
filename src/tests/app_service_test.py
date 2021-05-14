import unittest
from entities.month import Month
from entities.user import User
from services.app_service import AppService, UsernameExistsError, InvalidInputError

class FakeMonthRepo:
    def __init__(self, months=None):
        self.months = months or []

    def find_all(self):
        return self.months

    def find_by_username(self, username):
        return list(filter(lambda month: month.username == username, self.months))

    def find_by_username_month_year(self, username, month, year):
        months = filter(lambda m: m.username==username and m.month==month and m.year==year, self.months)

        return list(months)

    def create(self, month):
        self.months.append(month)

        return month

    def spend(self, month, category, amount):
        for m in self._months:
            if m.username==month.username and m.month==month and m.year==year:
                m.category += int(amount)
                break
        
    def delete_all(self):
        self.months = []

class FakeUserRepo:
    def __init__(self, users=None):
        self.users = users or []

    def find_all(self):
        return self.users
    
    def find_by_username(self, username):
        users = list(filter(lambda u: u.username==username, self.users))
        return users[0]

    def create(self, user):
        self.users.append(user)
        return user

    def delete_all(self):
        self.users = []

class TestAppService(unittest.TestCase):
    def setUp(self):
        self.app_service = AppService(FakeMonthRepo(), FakeUserRepo())

        self.mikko = User("Mikko", "salis")
        self.may = Month("Mikko", "May", "2021", 10, 0, 0, 0, 0, 0)

        self.app_service.create(self.mikko.username, self.mikko.password)

    def test_login_user_valid(self):
        user = self.app_service.login(self.mikko.username, self.mikko.password)
        
        self.assertEqual(user.username, self.mikko.username)

    def test_login_user_invalid(self):
        self.assertRaises(InvalidInputError, lambda: self.app_service.login("invalid", "password"))

    def test_get_months(self):
        self.app_service.login(self.mikko.username, self.mikko.password)

        self.app_service.log(self.may.month, self.may.year, "", 0)

        months = self.app_service.get_months()

        self.assertEqual(len(months), 1)
        self.assertEqual(months[1].food, self.may.food)