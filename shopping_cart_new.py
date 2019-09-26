import os
import json

class User:
    def __init__(self, name, username, password):
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

    def login(self):
        pass


user = User(input("name: "), input("username: "), input("password: "))
if  user.register():
    print("Registration successful")
else:
    print("Registration failed.")