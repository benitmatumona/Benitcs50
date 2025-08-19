import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    match = re.search(
        r'<iframe .* src\s?=\s?"https?://(www\.)?youtube\.com/embed/([\w\d]+)" .* >.*</iframe>',
        s,
        re.IGNORECASE
    )
    return f"http://youtu.be/{match.group(2)}" if match else None

if __name__ == "__main__":
    main()
