def main():
    user_input = input('Input: ')
    print(twttr(user_input))

def twttr(string):
    return ''.join([i for i in string if i not in "aeiouAEIOU"])

if __name__ == "__main__":
    main()
