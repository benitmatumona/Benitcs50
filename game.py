import random, sys

def main():
    game("Level: ")

def level_choice(prompt):
    while True:
        try:
            level = int(input(prompt))
            if level< 1:
                raise ValueError()
        except ValueError:
            pass
        else:
            return level
        
def guess(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input < 1:
                raise(ValueError)
        except ValueError:
            pass
        else:
            return user_input

def game(prompt):
    level = level_choice(prompt)
    answer = random.randint(1, level)
    while True:
        guessed = guess("Guess: ")
        if guessed < answer:
            print("Too small!")
        elif guessed > answer:
            print("Too large!")
        else:
            sys.exit("Just right!")

if __name__ == "__main__":
    main()

