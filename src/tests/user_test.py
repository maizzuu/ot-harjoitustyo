import unittest
from user import User
from month import Month

class TestUser(unittest.TestCase):
    def setUp(self):
        self.u = User("Daniel6", "dhk2")
    
    def test_month_added(self):
        self.u.add_month("June", "2020")
        self.assertEqual(len(self.u.months), 1)

    def test_spending_works(self):
        self.u.add_month("June", "2020")
        self.u.spend("June", "2020", 20, "food")
        self.assertEqual(self.u.months[0].spending["food"], 20)