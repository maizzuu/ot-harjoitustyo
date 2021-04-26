import unittest
from entities.user import User
from entities.month import Month
from repositories.month_repository import month_repository


class TestMonthRepository(unittest.TestCase):
    def setUp(self):
        month_repository.delete_all()
        self.user = User('Daniel', 'salasana')
        self.june = Month('Daniel', 'June', '2011', 0, 0, 0, 0, 0, 0)
        self.may = Month('Dan', 'May', '2020', 0, 0, 0, 0, 0, 0)

    def test_create(self):
        month_repository.create(self.june)
        months = month_repository.find_all()
        self.assertEqual(len(months), 1)
        self.assertEqual(months[0].month, self.june.month)

    def test_find_all(self):
        month_repository.create(self.june)
        month_repository.create(self.may)
        months = month_repository.find_all()
        self.assertEqual(len(months), 2)
        self.assertEqual(months[1].month, self.may.month)

    def test_find_by_username(self):
        month_repository.create(self.june)
        month_repository.create(self.may)
        months = month_repository.find_by_username('Dan')
        self.assertEqual(len(months), 1)
        self.assertEqual(months[0].month, self.may.month)

    def test_find_by_username_month_year(self):
        month_repository.create(self.june)
        month = month_repository.find_by_username_month_year('Daniel', 'June', '2011')
        self.assertEqual(month.month, self.june.month)

    def test_spend(self):
        month_repository.create(self.june)
        month_repository.spend(self.june, "food", "200")
        month_repository.spend(self.june, "living", "400")
        month_repository.spend(self.june, "hobbies", "50")
        month_repository.spend(self.june, "transportation", "30")
        month_repository.spend(self.june, "culture", "20")
        month_repository.spend(self.june, "other", "45")
        month = month_repository.find_by_username_month_year('Daniel', 'June', '2011')
        self.assertEqual(month.food, 200)
        self.assertEqual(month.living, 400)
        self.assertEqual(month.hobbies, 50)
        self.assertEqual(month.transportation, 30)
        self.assertEqual(month.culture, 20)
        self.assertEqual(month.other, 45)