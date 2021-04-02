import unittest
from month import Month

class TestMonth(unittest.TestCase):
    def setUp(self):
        self.m = Month("June", "2020")

    def test_creating_month_works(self):
        self.assertEqual(self.m.month, "June")
        self.assertEqual(self.m.year, "2020")
        self.assertEqual(self.m.spending, {
            "food": 0,
            "living": 0,
            "hobbies": 0,
            "transportation": 0,
            "culture": 0,
            "other": 0
        })