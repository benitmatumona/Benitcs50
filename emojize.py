import emoji

def main():
    user_input = input("Input: ")
    print(emojize(user_input))

def emojize(string):
    string = emoji.emojize(string)
    string = string.replace(":thumbsup:","👍")
    return string.replace(":earth_asia:","🌏")

if __name__ == "__main__":
    main()
