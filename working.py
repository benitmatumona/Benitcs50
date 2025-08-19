import re

def main():
    print(convert(input("Input: ")))

def convert(s):
    match = re.fullmatch(
        r"(0?\d|(1[0-2]))(:[0-5]\d)? (AM|PM) to (0?\d|(1[0-2]))(:[0-5]\d)? (AM|PM)",
        s
    )
    if not match:
        raise ValueError("Invalid Input")
    group = match.groups()
    prefix_1 = int(group[0]) + 12 if group[3] == "PM" and group[0] != "12" else int(group[0])
    prefix_1 = 0 if group[0] == "12" and group[3] == "AM" else prefix_1
    prefix_2 = int(group[4]) + 12 if group[7] == "PM" and group[4] != "12" else int(group[4])
    prefix_2 = 0 if group[4] == "12" and group[7] == "AM" else prefix_2
    return f"{prefix_1:02}{group[2]} to {prefix_2:02}{group[6]}".replace("None",":00")

if __name__ == "__main__":
    main()
