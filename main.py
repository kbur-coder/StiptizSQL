from src.parser import Parser

parser = Parser()

print("Welcome to StiptizSQL!")
print("Type 'exit' to quit.")

while True:
    command = input("stiptizsql > ")

    if command.lower() == "exit":
        break

    parser.parse(command)