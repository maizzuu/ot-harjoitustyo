import unittest
from users import Users

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.u = Users()

    def test_check_name_and_password_works(self):
        self.assertFalse(self.u.check_name("abc"))
        self.assertFalse(self.u.check_name("abc!"))
        self.assertTrue(self.u.check_name("abc1"))
        self.assertFalse(self.u.check_password("abc"))
        self.assertFalse(self.u.check_password("abc!"))
        self.assertFalse(self.u.check_password("abcd"))
        self.assertTrue(self.u.check_password("abc1"))

    def test_create_user_works(self):
        self.u.create_user("abcd1", "abcd2")
        self.assertEqual(len(self.u.user_list), 1)