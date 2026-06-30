import os
from src.storage import *


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


def select_from_table(table_name):
    #Пока что работает только со всей таблицей целиком
    table = load_table(table_name)

    if table is None:
        return None

    return table