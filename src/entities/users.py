from string import ascii_letters
from user import User

class Users:
    def __init__(self):
        self.user_list = []

    def check_name(self, name):
        if len(name)<4:
            return False
        for character in name: 
            if character not in ascii_letters:
                if character not in "0123456789":
                    return False
        return True

    def check_password(self, password):
        if len(password)<4:
            return False
        num = False
        for character in password:
            if character not in ascii_letters:
                if character not in "0123456789":
                    return False
            if character in "0123456789":
                num = True
        if not num:
            return False
        return True

    def create_user(self, username, password):
        if not self.check_name(username):
            return "Username does not meet the requirements"
        if not self.check_password(password):
            return "Password does not meet the requirements"
        self.user_list.append(User(username,password))
        return "User created succesfully!"