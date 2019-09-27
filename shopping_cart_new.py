import os
import json

class User:
    def __init__(self, username, password, name=None):
        self.name = name
        self.username = username
        self.password = password

    def register(self):
        try:
            registry = open(os.getcwd()+'/registry.json', 'r')
        except FileNotFoundError:
            registry = open(os.getcwd()+'/registry.json', 'w')
            dictionary = {"users":[{'name':self.name, 'username':self.username, 'password':self.password}]}
            json.dump(dictionary, registry)
            registry.close()
            return True
        else:
            read_json = registry.read()
            registry.close()
            json_dictionary = json.loads(read_json)
            if any(x for x in json_dictionary["users"] if x['username'] == self.username):
                return False
            registry = open(os.getcwd()+'/registry.json', 'w')
            json_dictionary["users"].append({'name':self.name, 'username':self.username, 'password':self.password})
            json.dump(json_dictionary,registry)
            registry.close()
            return True

    def login(self, username, password):
        try:
            register = open(os.getcwd()+'/registry.json', 'r')
        except FileNotFoundError:
            print("No such user registered. Please register yourself.")
            return False
        else:
            all_credentials_json = register.read()
            all_credentials_dictionary = json.loads(all_credentials_json)
            if any(x for x in all_credentials_dictionary["users"] if x['username'] == username and x['password'] == password):
                return True
            else:
                return False

isLogged = False
while True:
    print("Welcome to ABC Supermarket")
    print("Choose your option: ")
    print("1. Register")
    print("2. Login")
    option = int(input("Enter your choice here: "))

    if option == 1:
        name = input("Enter your name: ")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        user = User(username, password, name)
        if user.register():
            print("You have successfully registered in ABC supermarket.")
        else:
             print("Registration failed. Register again!")
        continue

    elif option == 2:
        username_login = input("Enter your username: ")
        password_login = input("Enter your password: ")
        user = User(username_login, password_login)
        if user.login(username_login, password_login):
            print("You have successfully logged in")
            break
        else:
            print("Login failed. Incorrect username or password!")
        continue

os.system('clear')
print("You are successfully logged in.")
print("Your Cart options: ")
print("1. Add to Cart")
print("2. Display the cart")
print("3. Update your cart")
print("4. Remove from cart")
