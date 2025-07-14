def main():
    user_input = input('Greeting: ')
    print(greeting(user_input))

def greeting(greet):
    if greet.lower().startswith('hello'):
        return "$0"
    elif greet.lower().startswith('h'):
        return "$20"
    return "$100"

if __name__ == "__main__":
    main()
