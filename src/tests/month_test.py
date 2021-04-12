import unittest
from month import Month
from user import User

class TestMonth(unittest.TestCase):
    def setUp(self):
        u = User("testname", "password")
        self.m = Month(u, "June", "2021", "")

    def test_creating_month_works(self):
        self.assertEqual(self.m.month, "June")
        self.assertEqual(self.m.year, "2021")
        