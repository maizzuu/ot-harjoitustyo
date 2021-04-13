from string import ascii_letters
from user import User

class Users:
    def __init__(self):
        self.user_list = []

    

    

    def create_user(self, username, password):
        if not self.check_name(username):
            return "Username does not meet the requirements"
        if not self.check_password(password):
            return "Password does not meet the requirements"
        self.user_list.append(User(username,password))
        return "User created succesfully!"