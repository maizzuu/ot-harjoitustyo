from repositories.user_repository import UserRepository
from repositories.month_repository import MonthRepository
from database_connection_copy import get_database_connection
from user_copy import User

login_commands = {"0": "exit", "1": "log in", "2": "create account"}
commands = {"0": "exit", "1": "log expenses", "2": "view previous spending"}
        
class TrackApp:
    def __init__(self):
        self.user_repo = UserRepository(get_database_connection())
        self.month_repo = MonthRepository(get_database_connection())

    def start(self):
        print("TrackApp")
        while True:
            self.login_instructions()
            l = self.login()
            if l == "EXIT":
                return
            elif l:
                break

        self.instructions()
        while True:
            if not self.read_commands():
                return 

    def read_commands(self):
        command = self.ask_for_command()
        if command not in commands:
            print("Unknown command")
            self.instructions()
        elif command == "0":
            return False
        elif command == "1":
            # TODO log expenses
            pass
        elif command == "2":
            # TODO view spending
            pass


    def ask_for_command(self):
        return input("command:")

    def login(self):
        command = self.ask_for_command()

        if command not in login_commands:
            print("Unknown command, try again")
            return False

        if command == "1": # log in
            username = input("username:")
            u = self.user_repo.find_by_username(username)
            if u is None:
                print("User does not exist")
                return False
            
            password = input("password:")
            if password != u.password:
                print("Wrong password")
                return False

        elif command == "2": # create account
            while True:
                print("Username must contain at least 4 characters. The username can consist of letters a-z (uppercase and lowercase) and numbers 0-9.")
                username = input("username:")
                if self.check_username(username):
                    break
                print("Username does not meet the requirements")

            while True:
                print("Password must contain at least 4 characters, at least one of which must be a number. The password can consist of letters a-z (uppercase and lowercase) and numbers 0-9.")
                password = input("password:")
                if self.check_password(password):
                    break
                print("Password does not meet the requirements")

            self.user_repo.create(User(username, password))
        
        elif command == "0":
            return "EXIT"

        print("Login succesfull")
        return True

    def login_instructions(self):
        print("To exit, insert 0")
        print("If you already have an account, insert 1")
        print("If you don't have an account yet, insert 2")

    def instructions(self):
        print("To exit, insert 0")
        print("To log expenses, insert 1")
        print("To view previous months' expenses, insert 2")

    def check_username(self, name):
        if len(name)<4:
            return False
        for character in name: 
            if character not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
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

if __name__ == "__main__":
    ta = TrackApp()
    ta.start()