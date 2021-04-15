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
        return f"{self.month}, {self.year}\nFood: {self.food}\nLiving: {self.living}\nHobbies: {self.hobbies}\nTransportation: {self.transportation}\nCulture: {self.culture}\nOther: {self.other}" 