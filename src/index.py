from repositories.user_repository import user_repository
from repositories.month_repository import month_repository
from entities.user import User
from entities.month import Month
from months_list import months
from print_month import print_month

LOGIN_COMMANDS = {"0": "exit", "1": "log in", "2": "create account"}
COMMANDS = {"0": "exit", "1": "log expenses", "2": "view previous spending"}


class TrackApp:
    def __init__(self):
        self.user_repo = user_repository
        self.month_repo = month_repository
        self.username = None

    def start(self):
        print()
        print("Welcome to TrackApp!")
        print()
        while True:
            self.login_instructions()
            login_return = self.login()
            if login_return == "EXIT":
                return
            if login_return:
                break

        while True:
            self.instructions()
            if not self.read_commands():
                return

    def read_commands(self):
        command = self.ask_for_command()
        if command not in COMMANDS:
            print("Unknown command")
            self.instructions()
            return True
        if command == "0":
            return False
        if command == "1":  # log spending
            self.log_expenses()
            return True
        if command == "2": # view
            self.view()
            return True

    def ask_for_command(self):
        return input("command:")

    def login(self):
        command = self.ask_for_command()

        if command not in LOGIN_COMMANDS:
            print("Unknown command, try again")
            return False

        if command == "1":  # log in
            username = input("username:")
            user = self.user_repo.find_by_username(username)
            if user is None:
                print("User does not exist")
                return False

            password = input("password:")
            if password != user.password:
                print("Wrong password")
                return False

        elif command == "2":  # create account
            while True:
                print("Username must contain at least 4 characters.")
                print("The username can consist of letters a-z uppercase and lowercase and numbers 0-9.")  # pylint: disable=line-too-long
                username = input("username:")
                if self.check_username(username):
                    break
                print("Username does not meet the requirements")

            while True:
                print("Password must contain at least 4 characters, at least one of which must be a number.")  # pylint: disable=line-too-long
                print("The password can consist of letters a-z (uppercase and lowercase) and numbers 0-9.")  # pylint: disable=line-too-long
                password = input("password:")
                if self.check_password(password):
                    break
                print("Password does not meet the requirements")

            self.user_repo.create(User(username, password))

        elif command == "0":
            return "EXIT"

        print()
        print("Login successful!")
        print(f"You are logged in as {username}")
        print()
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
        if len(name) < 4:
            return False
        for character in name:
            if character not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                if character not in "0123456789":
                    return False
        return True

    def check_password(self, password):
        if len(password) < 4:
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
        print()
        print("Log expenses")
        print()
        while True:
            print("To log to a preexisting month, insert 1")
            print("To add new month, insert 2")
            command = self.ask_for_command()
            if command == "1":
                break
            if command == "2":
                break
            print("Wrong command.")

        if command == "1": # log
            while True:
                month, year = self.ask_for_month_and_year()
                add = self.month_repo.find_by_username_month_year(
                    self.username, month, year)
                if not add:
                    print("Month not found.")
                    print(
                        "If you would like to add a new month, insert 1. Else, insert 0.")
                    command = self.ask_for_command()
                    if command == "1":
                        add = self.add_month(month, year)
                        break
                    if command == "0":
                        continue
                break
            self.log(add)

        if command == "2": # add
            month, year = self.ask_for_month_and_year()
            added_month = self.add_month(month, year)
            print("If you would like to log expenses for this month, insert 1")
            print("Else, insert 0")
            com = self.ask_for_command()
            print()
            if com  == "1":
                self.log(added_month)
            return

    def ask_for_month_and_year(self):
        while True:
            year = input("Year:")
            month = input("Month (written):")
            month = month[0].upper()+month[1:]
            for number in year:
                if number not in "0123456789":
                    print("Invalid year.")
            if not 1900 < int(year) < 2100:
                print("Wrong year.")
                continue

            if not month in months:
                print("Wrong month.")
                continue
            break
        return month, year

    def add_month(self, month, year):
        self.month_repo.create(
            Month(self.username, month, year, 0, 0, 0, 0, 0, 0))
        add = self.month_repo.find_by_username_month_year(
            self.username, month, year)
        print("Month created:")
        print()
        print_month(add)
        return add

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
        month = self.month_repo.find_by_username_month_year(
            self.username, month.month, month.year)
        print_month(month)
        print("If you would like to log more expenses for this month, insert 1")
        print("Else, insert 0")
        com = self.ask_for_command()
        if com == "1":
            self.log(month)

    def view(self):
        print()
        print("View previous spending")
        print()
        while True:
            print("Insert 1 to search and 0 to quit")
            command = self.ask_for_command()
            if command == "0":
                break
            month, year = self.ask_for_month_and_year()
            viewed = self.month_repo.find_by_username_month_year(
                self.username, month, year)
            if not viewed:
                print("Month not found.")
        if command == "1":
            print_month(viewed)
        else:
            return



if __name__ == "__main__":
    TA = TrackApp()
    TA.start()
