from src.database import create_table, insert_into_table

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

        else:
            print("Unknown command")