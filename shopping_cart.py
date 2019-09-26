import os

def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    try:
        os.mkdir(os.getcwd()+'/'+username)
    except FileExistsError:
        return "Your username is already registered. Please choose a different username.", True
    else:
        registry = open(os.getcwd()+'/'+username+'/'+'password', 'w')
        registry.write(password)
        registry.close()
    return "You have been successfully registered to ABC supermarket.", True

def login():
    os.system('clear')









while(1):                                                           #register and login. login changes screen
    os.system('clear')
    print("Welcome to ABC Supermarket")
    print("Choose your option: ")
    print("1. Register")
    print("2. Login")
    isRegistered = None
    out = None
    if isRegistered:
        print(out)
    option = input("Enter your option here: ")
    if option == '1':
        out, isRegistered = register()

    elif option == '2':
        login()
        break
    else:
        print("Invalid option")
        continue

