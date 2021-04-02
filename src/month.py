class Month:
    def __init__(self, month, year):
        self.month = month
        self.year = year
        self.spending = {
            "food": 0,
            "living": 0,
            "hobbies": 0,
            "transportation": 0,
            "culture": 0,
            "other": 0
        }
        

    def __str__(self):
        return f"{self.month} {self.year}"

    def __repr__(self):
        return f"Month({repr(self.month)}, {int(self.year)})"