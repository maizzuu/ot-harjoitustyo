import unittest
from user_copy import User
from user_repository_copy import user_repository

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_kalevi = User('Kalevi', 'salis')
        self.user_marja = User('Marja', 'salis')
        user_repository.create(self.user_kalevi)

    def test_create(self):
        users = user_repository.find_all()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, self.user_kalevi.username)

    def test_find_all(self):
        user_repository.create(self.user_marja)
        users = user_repository.find_all()
        self.assertEqual(len(users), 2)
        self.assertEqual(users[1].username, self.user_marja.username)

    def test_find_by_username(self):
        user = user_repository.find_by_username(self.user_kalevi.username)
        self.assertEqual(user.username, self.user_kalevi.username)