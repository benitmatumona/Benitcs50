import re, sys

def main():
    print(validate(input("IPv4 Addres: ")))

def validate(ip):
    match = re.fullmatch(r"(((1?\d{2})|(2[0-4][\d])|(25[0-5]))\.){3}((1?\d{2})|(2[1-4]\d)|(25[1-5]))", ip)
    return True if match else False

if __name__ == "__main__":
    main()
