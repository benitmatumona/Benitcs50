import sys

def main():
    print(grocery())

def grocery():
    items = []
    final = []
    while True:
        try:
            user_input = input()
            items.append(user_input.upper())
        except EOFError:
            for i in sorted(list(set(items))):
                final.append(f"{items.count(i)} {i}")
            print("\n".join(final))
            sys.exit(0)

if __name__ == "__main__":
    main()
