#!/usr/bin/python3

import unittest
from models.user import User
from models.place import Place
from models.review import Review
from models.city import City
from models.country import Country

class TestModels(unittest.TestCase):
    def test_user(self):
        user = User(email="abc@email.com", password="123456789")
        self.assertEqual(user.email, "abc@email.com")
        self.assertEqual(user.password, "password")


if __name__ == '__main__':
    unittest.main()