import sys, csv
from tabulate import tabulate

def main():
    print(menu())

def menu():
    info = sys.argv
    try:
        if len(info) > 2:
            sys.exit("Too many command-line arguments")
        elif len(info) < 2:
            sys.exit("Too few command-line arguments")
        elif info[1].endswith(".csv") == False:
            sys.exit("Not a CSV file")
        with open(info[1], "r") as file:
            reader = list(csv.DictReader(file))
            print(reader)
            return tabulate(reader, headers="keys", tablefmt = "grid")
    except FileNotFoundError:
        sys.exit("File doesn not exits")

if __name__ == '__main__':
    main()
