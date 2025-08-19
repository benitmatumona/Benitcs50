import sys

def main():
    print(count_lines())

def count_lines():
    count = 0
    try:
        info = sys.argv
        if len(info) < 2:
            sys.exit("Too few command-line arguments")
        elif len(info) > 2:
            sys.exit("Too many command-linenarguments")
        elif info[1].endswith(".py") == False:
            sys.exit("Not a python file")
        with open(info[1],"r") as file:
            reader = file.readlines()
            for row in reader:
                if row.lstrip(" ") != "\n" and row.lstrip().startswith("#") == False:
                    count += 1
            return count
    except FileNotFoundError:
        sys.exit("File doesn not exist")

if __name__ == "__main__":
    main()
