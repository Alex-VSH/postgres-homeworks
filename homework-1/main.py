"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2
import csv


with psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='12345'
) as conn:
    with conn.cursor() as cur:
        with open("north_data/employees_data.csv", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            for row in file_reader:
                if row[0] == 'employee_id':
                    continue
                cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)',
                            (row[0], row[1], row[2], row[3], row[4], row[5]))
        with open("north_data/customers_data.csv", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            for row in file_reader:
                if row[0] == 'customer_id':
                    continue
                cur.execute('INSERT INTO customers VALUES (%s, %s, %s)',
                            (row[0], row[1], row[2]))
        with open("north_data/orders_data.csv", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            for row in file_reader:
                if row[0] == 'order_id':
                    continue
                cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)',
                            (row[0], row[1], row[2], row[3], row[4]))


conn.close()
