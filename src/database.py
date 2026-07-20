import os
from src.storage import *
from typing import Literal


def create_table(table_name, columns):
    # функция создает таблицу с заданными в список columns аргументами
    if is_table_exists(table_name):
        print('Таблица уже существует')
        return

    save_table(table_name, [columns])


def insert_into_table(table_name, values):
    table = load_table(table_name)

    if len(values) != len(table[0]):
        print("Неверное количество значений")
        return

    append_row(table_name, values)


def check_where(row, where_indexes):
    for index, value in where_indexes.items():
        if row[index] != value:
            return False
    return True


def select_from_table(table_name: str,
                      columns: list[str] | Literal["*"] | None = None,
                      where: dict[str,str] | None = None):

    table = load_table(table_name)
    if table is None:
        return None

    headers = table[0]    # берем только заголовки из table

    if columns is None or columns == "*":    # создаем список из индексов заголовков таблицы table
        column_indexes = list(range(len(headers)))
    else:
        column_indexes = []
        for column in columns:
            if column not in headers:
                print('Нет такого столбца')
                return None

            column_indexes.append(headers.index(column))

    where_indexes = {}

    if where is not None:
        for column, value in where.items():
            if column not in headers:
                print("Нет такого столбца")
                return None

            where_indexes[headers.index(column)] = str(value)

    result = []


    result.append([headers[i] for i in column_indexes])    # добавляем заголовки

    for row in table[1:]:
        if check_where(row, where_indexes):
            result.append([row[i] for i in column_indexes])

    return result




def delete_from_table(table_name: str,
                      where: dict[str, str] | None = None):
    table = load_table(table_name)

    if table is None:
        return

    headers = table[0]

    where_indexes = {}

    if where is not None:
        for column, value in where.items():
            if column not in headers:
                print("Нет такого столбца")
                return

            where_indexes[headers.index(column)] = str(value)

    new_table = [headers]

    for row in table[1:]:
        if not check_where(row, where_indexes):
            new_table.append(row)

    save_table(table_name, new_table)



