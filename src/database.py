import os
from src.storage import save_table


def create_table(table_name, columns):
    path = os.path.join("data", f"{table_name}.csv")

    if os.path.exists(path):
        print("Таблица уже существует")
        return

    save_table(table_name, [columns])
