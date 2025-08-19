def main():
    percent = convert(input('Fuel: '))
    print(gauge(percent))

def convert(fraction):
    while True:
        try:
            fraction = fraction.split("/")
            if len(fraction) != 2 or not all(i.isnumeric() for i in fraction):
                raise ValueError("ValueError")
            elif int(fraction[1]) == 0:
                raise ZeroDivisionError("ZeroDivisionError")
            elif int(fraction[0]) > int(fraction[1]):
                raise ValueError("ValueError")
            return round(eval(f"{fraction[0]}/{fraction[1]}*{100}"))
        except:
            fraction = input("Fuel: ")

def gauge(percentage):
    if 90 <= percentage <= 100:
        return "F"
    elif 10 < percentage < 90:
        return f"{percentage}%"
    elif 0 <= percentage <= 10:
        return "E"

if __name__ == '__main__':
    main()
