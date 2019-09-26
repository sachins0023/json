import os
import json


class Cart:                                         #has list of items, add to cart, view cart, update cart, delete from cart
    def __init__(self):
        self.list_of_items = []
    def add(self, item, quantity):
        pass
    def view(self):
        for item in self.list_of_items:
            print(item)
    def update(self, item, quantity):
        pass
    def delete(self, item):
        pass

class Item:                                         #has name and price
    def __init__(self, name, price):
        self.name = name
        self.price = price

class User:
    def __init__(self):
        self.username = None
        self.password = None
    def register(self, username, password):
        self.username = username
        self.password = password
        registry = open(os.getcwd() + '/credentials.json', 'a+')
        registry.seek(0,0)
        creds = registry.read()
        if creds == '':
            creds_dict = {'users':[]}
            creds_dict['users'].append({'name': self.username, 'password':self.password})
            json.dump(creds_dict, registry)
            registry.close()
            return "You have been successfully registered to ABC supermarket.", True
        else:
            creds_dict = json.loads(creds)
        if {'name': self.username, 'password' : self.password} in creds_dict['users']:
            return "The given username is taken. Please enter a new username.", False
        creds_dict['users'].append({'name': self.username, 'password': self.password})
        json.dump(creds_dict, registry)
        registry.close()
        return "You have been successfully registered to ABC supermarket.", True

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        try:
            registry = open(os.getcwd() + '/credentials.txt', 'r')
        except FileNotFoundError:
            return "User with given credentials doesn't exist. Please register yourself.", False
        else:
            creds = registry.read()
            creds_dict = json.load(creds)
            if username in creds_dict.keys():
                if password == creds_dict[username]:
                    return "You have successfully logged in.", True
            return "Invalid credentials. Login again", False


user = User()
print("Welcome to ABC Supermarket")
print("Choose your option: ")
print("1. Register")
print("2. Login")
option = int(input("Enter your choice here: "))
if option == 1:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    out, isRegistered = user.register(username, password)
    print(out)


