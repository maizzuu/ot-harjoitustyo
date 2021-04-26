from entities.month import Month
from database_connection import get_database_connection


def get_month_by_row(row):
    return Month(
        row['username'],
        row['month'],
        row['year'],
        row['food'],
        row['living'],
        row['hobbies'],
        row['transportation'],
        row['culture'],
        row['other']
    ) if row else None


class MonthRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()

        cursor.execute('select * from months')

        rows = cursor.fetchall()

        return list(map(get_month_by_row, rows))

    def find_by_username(self, username:str):
        cursor = self._connection.cursor()

        cursor.execute('select * from months where username = ?', (username,))

        rows = cursor.fetchall()

        return list(map(get_month_by_row, rows))

    def find_by_username_month_year(self, username:str, month:str, year:str):
        cursor = self._connection.cursor()

        sql = 'select * from months where username = ? and month = ? and year = ?'
        cursor.execute(sql, (username, month, year))

        row = cursor.fetchone()

        return get_month_by_row(row)

    def create(self, month:Month):
        cursor = self._connection.cursor()

        sql = '''insert into months (username, month, year, food, living,
                hobbies, transportation, culture, other) values 
                (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        cursor.execute(
            sql,
            (
                month.username,
                month.month,
                month.year,
                month.food,
                month.living,
                month.hobbies,
                month.transportation,
                month.culture,
                month.other
            )
        )

        self._connection.commit()

        return month

    def spend(self, month:Month, category:str, amount:str):
        cursor = self._connection.cursor()

        if category == "food":
            sql = '''update months set food = food+ ?
                    where username = ? and month = ? and year = ?'''
            cursor.execute(
                sql, (amount, month.username, month.month, month.year))
        elif category == "living":
            sql = '''update months set living = living+ ?
                    where username = ? and month = ? and year = ?'''
            cursor.execute(
                sql, (amount, month.username, month.month, month.year))
        elif category == "hobbies":
            sql = '''update months set hobbies = hobbies+ ?
                    where username = ? and month = ? and year = ?'''
            cursor.execute(
                sql, (amount, month.username, month.month, month.year))
        elif category == "transportation":
            sql = '''update months set transportation = transportation+ ?
                    where username = ? and month = ? and year = ?'''
            cursor.execute(
                sql, (amount, month.username, month.month, month.year))
        elif category == "culture":
            sql = '''update months set culture = culture+ ?
                    where username = ? and month = ? and year = ?'''
            cursor.execute(
                sql, (amount, month.username, month.month, month.year))
        else:
            sql = '''update months set other = other+ ?
                    where username = ? and month = ? and year = ?'''
            cursor.execute(
                sql, (amount, month.username, month.month, month.year))

        self._connection.commit()

    def delete_all(self):
        cursor = self._connection.cursor()

        cursor.execute('delete from months')

        self._connection.commit()


month_repository = MonthRepository(get_database_connection())
