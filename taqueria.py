import sys

def main():
    print(taqueria())

def taqueria():
    while True:
        try:
            menu = {
                "Baja Taco": 4.25,
                "Burrito": 7.50,
                "Bowl": 8.50,
                "Nachos": 11.00,
                "Quesadilla": 8.50,
                "Super Burrito": 8.50,
                "Super Quesadilla": 9.50,
                "Taco": 3.00,
                "Tortilla Salad": 8.00
                }
            count = 0
            item = input("Item: ").title()
            count+= menu[item]
            print(f"Total: ${count :.2f}")
        except KeyError:
            pass
        except EOFError:
            sys.exit()


if __name__ == "__main__":
    main()
