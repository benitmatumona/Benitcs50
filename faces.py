def main():
    print(convert(input()))

def convert(string):
    return string.replace(':)', "🙂").replace(":(", "🙁")

if __name__ == "__main__":
    main()

