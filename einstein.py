def main():
    user_input = int(input('type an amount of weight in killograms :'))
    print(convert(user_input))
def convert(number):
    return number*300000000**2

if __name__ == "__main__":
    main()
