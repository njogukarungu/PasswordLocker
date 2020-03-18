#!/usr/bin/env python3.6
from user import User
def createUser(username, password):
    myUser = User(username, password)
    return myUser
def saveUser(user):
    user.saveUser()
def displayUsers():
    User.displayUsers()
def main():
    print("Welcome to your pass word locker, create account")
    print("\n")
    while True: 
        shortcodes= input("Use the following: cu to create user : du to display user").lower()
        if shortcodes == "cu":
            username = input("Enter your preffered username:")
            password = input("Enter your preffered  password:")
            saveUser(createUser(username, password))
            print(f"Hello {username} thank you for creating your password locker account, you can now proceed")
        elif shortcodes == "du":
            for user in User.users:
                print(f"{user.username}")
        else: print("Kindly check your entry again")   

main()

    
