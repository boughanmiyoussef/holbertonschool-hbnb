#!/usr/bin/python3

from data_manager import DataManager
from models.user import User
from models.place import Place


data_manager = DataManager()


user = User(email="youssef@gmail.com", password="iamyoussef")
data_manager.save(user)

retrieved_user = data_manager.get(user.id, 'User')
print(retrieved_user.email)

user.password = "boughanmi"
data_manager.user(user)

data_manager.delete(user.id, 'User')
print(retrieved_user)