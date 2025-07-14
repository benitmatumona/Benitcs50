def main():
    print(deep())
def deep():
    answer = input("what is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()
    return "yes" if answer in ["forty two", "forty-two", "42"] else "no"
if __name__ == "__main__":
    main()
