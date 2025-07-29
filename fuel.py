def main():
    x = input('Fuel: ')
    print(fuel(x))

def fuel(x):
    while True:
        try:
            x= eval(x) if "." not in x and x.count("/") == 1 else 1000
            if 0.9 <= x <= 1:
                return "F"
            elif 0.1 < x < 0.9:
                return round(x, 1)
            elif 0 <= x <= 1:
                return 'E'
        except (ValueError, ZeroDivisionError, NameError):
            pass
        x = input('Fuel: ')

if __name__ == '__main__':
    main()
