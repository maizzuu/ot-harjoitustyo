import unittest
from entities.month import Month

class TestMonth(unittest.TestCase):
    def setUp(self):
        self.month = Month('Daniel', 'June', '2011', 0, 0, 0, 0, 0, 0)

    def test_create_month(self):
        self.assertEqual(self.month.username, "Daniel")
        self.assertEqual(self.month.month, "June")
        self.assertEqual(self.month.year, "2011")
        self.assertEqual(self.month.food, 0)
        self.assertEqual(self.month.living, 0)
        self.assertEqual(self.month.hobbies, 0)
        self.assertEqual(self.month.transportation, 0)
        self.assertEqual(self.month.culture, 0)
        self.assertEqual(self.month.other, 0)
