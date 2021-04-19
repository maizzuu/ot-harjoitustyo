class Month:
    def __init__(self, username, month, year, food, living, hobbies, transportation, culture, other):
        self.username = username
        self.month = month
        self.year = year
        self.food = food
        self.living = living
        self.hobbies = hobbies
        self.transportation = transportation
        self.culture = culture
        self.other = other

    def __str__(self):
        if self.username[-1] == "s":
            return f"""{self.username}' {self.month}, {self.year}\n
                    Food: {self.food}\n
                    Living: {self.living}\n
                    Hobbies: {self.hobbies}\n
                    Transportation: {self.transportation}\n
                    Culture: {self.culture}\n
                    Other: {self.other}"""
        return f"""{self.username}'s {self.month}, {self.year}\n
                Food: {self.food}\n
                Living: {self.living}\n
                Hobbies: {self.hobbies}\n
                Transportation: {self.transportation}\n
                Culture: {self.culture}\n
                Other: {self.other}"""
