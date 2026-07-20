import csv
import os

def load_table(table_name):
    path = os.path.join("data", f"{table_name}.csv")

    if not os.path.exists(path):
        print('Таблицы не существует')
        return None

    with open(path, 'r', newline='', encoding='UTF-8') as file:
        reader = csv.reader(file)
        return list(reader)


def save_table(table_name, data):
    # функция изменяет и сохраняет информацию, data ожидает матрицу на вход, полностью перезаписывает таблицу
    path = os.path.join("data", f"{table_name}.csv")

    with open(path, 'w', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def append_row(table_name, row):
    path = os.path.join("data", f"{table_name}.csv")
    with open(path, 'a', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file)
        writer.writerow(row)


def is_table_exists(table_name):
    path = os.path.join("data", f"{table_name}.csv")
    if os.path.exists(path):
        return True

    return False


