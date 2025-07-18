def main():
    user_input = input('Input: ')
    print(twttr(user_input))

def twttr(string):
    return ''.join([i if i not in "aeiouAEIOU" else "" for i in string])

if __name__ == "__main__":
    main()
