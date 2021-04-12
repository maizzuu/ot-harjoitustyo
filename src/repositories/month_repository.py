from entities.month import Month
from database_connection import get_database_connection

def get_month_by_row(row):
    username = row['username']
    user = user_repository.find_by_username(username) if username else None
    month = row['month']
    year = row['year']
    food = row['food']
    living = row['living']
    return Month(user, 
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

        rows = curor.fetchall()

        return list(map(get_month_by_row, rows))

    def create(self, month):
        cursor = self._connection.cursor()

        cursor.execute(
            'insert into months (username, month, year, food, living, hobbies, transportation, culture, other) values (?, ?, ?, ?, ?, ?, ?, ?, ?)',
            (month.username, month.month, month.year, month.food, month.living, month.hobbies, month.transportation, month.culture, month.other)
        )

        self._connection.commit()

        return month

    def delete_all(self):
        cursor = self._connection.cursor()

        cursor.execute('delete from months')

        self._connection.commit()