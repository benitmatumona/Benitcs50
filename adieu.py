import inflect, sys

def main():
    print(adieu())

def adieu():
    new = []
    p = inflect.engine()
    while True:
        try:
            user_input = input("Input: ")
            new.append(user_input)
        except EOFError:
            print(f"Adieu, adieu, to {p.join(new)}")
            sys.exit(0)

if __name__ == "__main__":
    main()
