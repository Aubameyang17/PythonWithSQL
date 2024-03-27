import psycopg2
from Config import host, user, password, db_name
import random

def version():
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version: {cursor.fetchone()}")

def create_table():
    with connection.cursor() as cursor:
        cre_fun = """
                CREATE TABLE if not exists users(
                id serial PRIMARY KEY,
                first_name varchar(50) NOT NULL,
                nick_name varchar(50) NOT NULL,
                age integer);
                """
        cursor.execute(cre_fun)
        print("Table created")

def insert_data(record):
    with connection.cursor() as cursor:
        inser_el = """
            INSERT INTO users (first_name, nick_name, age) VALUES
            (%s, %s, %s);
            """
        cursor.execute(inser_el, record)
        print("Data Inserted")

def find_on_name():
    with connection.cursor() as cursor:
        s = input("Введите имя чтобы посмотреть nick_name: ")
        data_search = """
            SELECT nick_name FROM users WHERE first_name = %s;
            """
        cursor.execute(data_search, (s, ))
        print(cursor.fetchall())

def find_on_id():
    with connection.cursor() as cursor:
        s = int(input("Введите id чтобы посмотреть nick_name и first_name: "))
        data_search = """
            SELECT nick_name, first_name FROM users WHERE id = %s;
            """
        cursor.execute(data_search, (s, ))
        print(cursor.fetchall())

def view_all():
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT AVG(age) FROM users;
            """
        )
        print(cursor.fetchall())

def myself_fun(fun):
    with connection.cursor() as cursor:
        cursor.execute(fun)
        print(cursor.fetchall())

def delete_table():
    with connection.cursor() as cursor:
        cursor.execute(
            """
            DROP TABLE users;
            """
        )
        print("Table deleted")

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    version()
    i = 1
    while i != 0:
        vibor = int(input("1) Создать таблицу\n2) Вставить значение\n3) Найти данные в таблице по id\n4) Найти данные в таблице по Имени\n5) Показать средний возраст\n6) Написать собственный запрос\n7) Удалить таблицу\n"))
        if vibor == 1:
            create_table()
        elif vibor == 2:
            age = int(input("Введите возраст человека"))
            first = input("Введите имя человека")
            second = input("Введите никнейм человека")
            record = (first, second, age)
            insert_data(record)
        elif vibor == 3:
            find_on_id()
        elif vibor == 4:
            find_on_name()
        elif vibor == 5:
            view_all()
        elif vibor == 6:
            function1 = input("Введите запрос: ")
            myself_fun(function1)
        elif vibor == 7:
            delete_table()
        elif vibor == 0:
            i = 0

except Exception as ex:
    print("Error - ", ex)
finally:
    if connection:
        connection.close()
        print("Closed")