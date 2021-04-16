from copies.month_copy import Month
from copies.database_connection_copy import get_database_connection

def get_month_by_row(row):
    return Month(row['username'],
                row['month'], 
                row['year'], 
                row['food'], 
                row['living'], 
                row['hobbies'], 
                row['transportation'], 
                row['culture'], 
                row['other'])

class MonthRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()

        cursor.execute('select * from months')

        rows = cursor.fetchall()

        return list(map(get_month_by_row, rows))

    def find_by_username(self, username):
        cursor = self._connection.cursor()

        cursor.execute('select * from months where username = ?', (username,))

        rows = cursor.fetchall()

        return list(map(get_month_by_row, rows))

    def find_by_username_and_month_and_year(self, username, month, year):
        cursor = self._connection.cursor()

        cursor.execute('select * from months where username = ? and month = ? and year = ?', (username, month, year))

        row = cursor.fetchone()

        return get_month_by_row(row)

    def create(self, month):
        cursor = self._connection.cursor()

        cursor.execute(
            'insert into months (username, month, year, food, living, hobbies, transportation, culture, other) values (?, ?, ?, ?, ?, ?, ?, ?, ?)',
            (month.username, month.month, month.year, month.food, month.living, month.hobbies, month.transportation, month.culture, month.other)
        )

        self._connection.commit()

        return month

    def spend(self, month, category, amount):
        cursor = self._connection.cursor()

        if category == "food":
            cursor.execute('update months set food = ? + ? where username = ? and month = ? and year = ?', (category, amount, month.username, month.month, month.year))
        elif category == "living":
            cursor.execute('update months set living = ? + ? where username = ? and month = ? and year = ?', (category, amount, month.username, month.month, month.year))
        elif category == "hobbies":
            cursor.execute('update months set hobbies = ? + ? where username = ? and month = ? and year = ?', (category, amount, month.username, month.month, month.year))
        elif category == "transportation":
            cursor.execute('update months set transportation = ? + ? where username = ? and month = ? and year = ?', (category, amount, month.username, month.month, month.year))
        elif category == "culture":
            cursor.execute('update months set culture = ? + ? where username = ? and month = ? and year = ?', (category, amount, month.username, month.month, month.year))
        else:
            cursor.execute('update months set other = ? + ? where username = ? and month = ? and year = ?', (category, amount, month.username, month.month, month.year))

        self._connection.commit()

    def delete_all(self):
        cursor = self._connection.cursor()

        cursor.execute('delete from months')

        self._connection.commit()

month_repository = MonthRepository(get_database_connection())