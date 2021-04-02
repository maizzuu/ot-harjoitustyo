from month import Month

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.months = []

    def add_month(self, month, year):
        self.months.append(Month(month, year))

    def spend(self, month, year, amount, category):
        for item in self.months:
            if str(item) == f"{month} {year}":
                m = item
                break
        for item in m.spending:
            if item == category:
                m.spending[item] += amount
                break
        
    def __repr__(self):
        return f"User({str(username)})"