class Month:
    """Class with which the user can keep track of their spending.

    Spending is logged in six different categories.

    Attributes:
        username: Name of the user who the month belongs to.
        month: Month
        year: Year
        Categories:
        food: Food + other essentials
        living: Living
        hobbies: Hobbies
        transportation: Transportation
        culture: Culture + restaurants
        other: Everything else
    """

    def __init__(self, username, month, year, food, living, hobbies, transportation, culture, other):
        """Class constructor that creates a new month.

        Args:
            username: Name of the user who owns this month.
            month: Month
            year: Year
            food: Amount spent on food.
            living: Amount spent on living.
            hobbies: Amount spent on hobbies.
            transportation: Amount spent on transportation.
            culture: Amount spent on culture.
            other: Amount spent on other things.
        """
        self.username = username
        self.month = month
        self.year = year
        self.food = food
        self.living = living
        self.hobbies = hobbies
        self.transportation = transportation
        self.culture = culture
        self.other = other
        