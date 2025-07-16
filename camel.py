def main():
    user_input = input("camelCase: ")
    print(camel(user_input))

def camel(string):
    return "".join([i if i.islower() else f"_{i.lower()}" for i in string])

if __name__ == "__main__":
    main()
