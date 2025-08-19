import re

def main():
    print(count(input("Text: ")))

def count(s:str):
    count = 0
    for i in s.split():
        if re.fullmatch(r'[\s\:\.\?,]?um[\s\:\.\?,]?',i, re.IGNORECASE):
            count += 1
    return count

if __name__ == '__main__':
    main()
