from repositories.user_repository import user_repository
from repositories.month_repository import month_repository
from entities.user import User
from entities.month import Month
from months_list import months

login_commands = {"0": "exit", "1": "log in", "2": "create account"}
commands = {"0": "exit", "1": "log expenses", "2": "view previous spending"}

class TrackApp:
    def __init__(self):
        self.user_repo = user_repository
        self.month_repo = month_repository
        self.username = None

    def start(self):
        print("TrackApp")
        while True:
            self.login_instructions()
            login_return = self.login()
            if login_return == "EXIT":
                return
            if login_return:
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
        elif command == "1": # log spending
            self.log_expenses()
            return
        elif command == "2":
            # TODO view spending
            return


    def ask_for_command(self):
        return input("command:")

    def login(self):
        command = self.ask_for_command()

        if command not in login_commands:
            print("Unknown command, try again")
            return False

        if command == "1": # log in
            username = input("username:")
            user = self.user_repo.find_by_username(username)
            if user is None:
                print("User does not exist")
                return False

            password = input("password:")
            if password != user.password:
                print("Wrong password")
                return False

        elif command == "2": # create account
            while True:
                print("Username must contain at least 4 characters.")
                print("The username can consist of letters a-z uppercase and lowercase and numbers 0-9.") # pylint: disable=line-too-long
                username = input("username:")
                if self.check_username(username):
                    break
                print("Username does not meet the requirements")

            while True:
                print("Password must contain at least 4 characters, at least one of which must be a number.") # pylint: disable=line-too-long
                print("The password can consist of letters a-z (uppercase and lowercase) and numbers 0-9.") # pylint: disable=line-too-long
                password = input("password:")
                if self.check_password(password):
                    break
                print("Password does not meet the requirements")

            self.user_repo.create(User(username, password))

        elif command == "0":
            return "EXIT"

        print("Login succesfull")
        self.username = username
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
            if character not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                if character not in "0123456789":
                    return False
            if character in "0123456789":
                num = True
        if not num:
            return False
        return True

    def log_expenses(self):
        print("Log expenses:")
        while True:
            print("To log to a preexisting month, insert 1")
            print("To add new month, insert 2")
            command = self.ask_for_command()
            if command == "1":
                break
            elif command == "2":
                break
            print("Wrong command.")

        if command == "1":
            while True:
                month, year = self.ask_for_month_and_year()
                add = self.month_repo.find_by_username_and_month_and_year(self.username, month, year) # pylint: disable=line-too-long
                if not add:
                    print("Month not found.")
                    print("If you would like to add a new month, insert 1. Else, insert 0.") # pylint: disable=line-too-long
                    command = self.ask_for_command()
                    if command == "1":
                        self.add_month(month, year)
                        break
                    if command == "0":
                        continue
                break
            self.log(add)

        if command == "2":
            self.add_month(month, year)

    def ask_for_month_and_year(self):
        while True:
            year = input("Year:")
            month = input("Month (written):")
            month = month[0].upper()+month[1:]
            if not 1900 < int(year) < 2100:
                print("Wrong year.")
                continue
            
            if not month in months:
                print("Wrong month.")
                continue
            break
        return month, year

    def add_month(self, month, year):
        self.month_repo.create(Month(self.username, month, year, 0, 0, 0, 0, 0, 0))
        add = self.month_repo.find_by_username_and_month_and_year(self.username, month, year)
        print("Month created:")
        print(add)

    def log(self, month=Month):
        while True:
            print("Choose one of the following categories:")
            print("food, living, hobbies, transportation, culture, other")
            category = input("Category: ")
            category = category.lower()
            if category not in ["food", "living", "hobbies", "transportation", "culture", "other"]:
                print("Wrong category.")
                continue
            break
        while True:
            all_numbers = True
            amount = input("Amount: ")
            for number in amount:
                if number not in "1234567890":
                    print("Wrong amount.")
                    all_numbers = False
            if not all_numbers:
                continue
            break
        self.month_repo.spend(month, category, amount)
        print()
        print("All done!")
        print()
        print(self.month_repo.find_by_username_and_month_and_year(self.username, month.month, month.year))

# TODO view previous months, fix logging in loops

if __name__ == "__main__":
    ta = TrackApp()
    ta.start()
