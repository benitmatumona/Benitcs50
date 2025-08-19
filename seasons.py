import sys, inflect
from datetime import date, datetime

def main():
    print(age(input("Date of birth: ")))

def validate_date(s:str) -> str:
    try:
        if datetime.strptime(s, "%Y-%m-%d"):
            return "Valid"
    except ValueError:
        return "Invalid"

def age(birth:str) -> str:
    if validate_date(birth) == "Invalid":
        sys.exit("Invalid date")
    birth = birth.split("-")
    days = date.today() - date(int(birth[0]), int(birth[1]), int(birth[2]))
    age = int(str(days).split()[0])*24*60
    return inflect.engine().number_to_words(age).capitalize().replace(" and","") + " minutes"

if __name__ == "__main__":
    main()
