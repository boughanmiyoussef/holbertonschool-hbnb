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

    def test_place(self):
        user = User(email="host@email.com", password="qwerty")
        place = Place(name="New Place", host=user, description="Good")
        review = Review(user=user, place=place, rating=5, comment="")
        place.reviews.append(review)
        self.assertEqual(len(place.reviews), 1)
        self.assertEqual(place.reviews[0], review)

    def test_review(self):
        user = User(email="reviewer@example.com", password="asdfg")
        place = Place(name="The Best Place", host=user, description="Great")
        review = Review(user=user, place=place, rating=5, comment="Amazing!")
        place.reviews.append(review)
        self.assertEqual(len(place.reviews), 1)
        self.assertEqual(place.reviews[0], review)


    def test_city_country(self):
        country = Country(name="France")
        city = City(name="Paris", country=country)
        self.assertEqual(city.name, "Paris")
        self.assertEqual(city.country, country)


if __name__ == '__main__':
    unittest.main()