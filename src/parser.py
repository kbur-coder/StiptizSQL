from src.database import (
    create_table,
    insert_into_table,
    select_from_table,
    delete_from_table,
    update_table
)


class Parser:

    def parse(self, command):
        parts = command.split()

        if len(parts) == 0:
            return

        if parts[0].upper() == "CREATE":

            if len(parts) < 4:
                print("Usage: CREATE TABLE table_name column1 column2 ...")
                return

            if parts[1].upper() != "TABLE":
                print("Unknown command")
                return

            table_name = parts[2]
            columns = parts[3:]

            create_table(table_name, columns)

        elif parts[0].upper() == "INSERT":

            if len(parts) < 3:
                print("Usage: INSERT table_name value1 value2 ...")
                return

            table_name = parts[1]
            values = parts[2:]

            insert_into_table(table_name, values)

        elif parts[0].upper() == "SELECT":

            if len(parts) == 2:
                table_name = parts[1]

            elif len(parts) >= 4 and parts[1] == "*" and parts[2].upper() == "FROM":
                table_name = parts[3]

            else:
                print("Usage: SELECT table_name")
                print("   or: SELECT * FROM table_name")
                return

            table = select_from_table(table_name)

            if table is None:
                return

            for row in table:
                print(" | ".join(row))

        elif parts[0].upper() == "DELETE":

            if len(parts) != 3:
                print("Usage: DELETE table_name id")
                return

            table_name = parts[1]
            record_id = parts[2]

            delete_from_table(table_name, record_id)

        elif parts[0].upper() == "UPDATE":

            if len(parts) != 5:
                print("Usage: UPDATE table_name id column_name new_value")
                return

            table_name = parts[1]
            record_id = parts[2]
            column_name = parts[3]
            new_value = parts[4]

            update_table(table_name, record_id, column_name, new_value)

        else:
            print("Unknown command")