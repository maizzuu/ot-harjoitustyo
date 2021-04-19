from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
    ''')

    cursor.execute('''
        drop table if exists months;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table users (
            id integer primary key,
            username text UNIQUE,
            password text
        );
    ''')

    cursor.execute('''
        create table months (
            id integer primary key,
            username text,
            month text,
            year text,
            food integer,
            living integer,
            hobbies integer,
            transportation integer,
            culture integer,
            other integer
        );
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
