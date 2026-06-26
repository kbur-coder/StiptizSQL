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
    path = os.path.join("data", f"{table_name}.csv")

    with open(path, 'w', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)
