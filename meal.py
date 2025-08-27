def main():
    decimal = convert(input("what time is it? "))
    print(time(decimal))

def convert(time :str) -> float:
    hours, minutes = time.replace("a.m.","").replace("p.m.","").split(":")
    if time.endswith("p.m.") and int(hours) < 12:
        return 12+int(hours)+int(minutes)/60
    elif hours == "12" and time.endswith("a.m."):
        return int(minutes)/60
    return int(hours)+ int(minutes)/60

def time(number : int) -> str:
    return "breakfast time" if 7<= number <= 8 else "lunch time" if 12 <= number <= 13 else "dinner time" if 18 <= number <= 19 else ""

if __name__ == "__main__":
    main()
