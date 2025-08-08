import random

def main():
    level = get_level()
    print(generate_integer(level))

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if not (0 < level < 4):
                raise ValueError()
        except ValueError:
            pass
        else:
            return level

def generate_integer(level):
    begin = 10**(level - 1) if level != 1 else 0
    end = 9 * int("1"*level)
    score = 0

    for question_number in range(10):
        first = random.randrange(begin, end + 1)
        second = random.randrange(begin, end + 1)
        for chances in range(3):
            try:
                result = first + second
                answer = int(input(f"{first} + {second} = "))
                if answer == result:
                    score += 1
                    break
                elif answer != result:
                    raise ValueError()
            except ValueError:
                print("EEE")
                if chances == 2:
                    print(f"{first} + {second} = {result}")

    return f"Score: {score}"


if __name__ == "__main__":
    main()
