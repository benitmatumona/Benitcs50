def main():
    user_input = input("Expression: ")
    print(interpret(user_input))

def interpret(string):
    return round(float(eval(string)), 1)

if __name__ == "__main__":
    main()
