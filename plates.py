def main():
    plate = input('Plate: ')
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if is_alpha_numeric(s):
        if digits_2_to_6(s):
            if starts_with_alpha(s):
                if ends_with_digits(s):
                    if number_begins_not_zero(s):
                        return True
    return False

def starts_with_alpha(s):
    return all(i.isalpha() for i in s[:2])

def digits_2_to_6(s):
    return 2 <= len(s) <= 6

def ends_with_digits(s):
    for i,j in list(enumerate(s))[:-1]:
        if j.isnumeric() and s[i + 1].isalpha():
            return False
    return True

def number_begins_not_zero(s):
    numbers = [i for i in s if i.isnumeric()]
    return numbers[0] != "0" if len(numbers) > 0 else True

def is_alpha_numeric(s):
    return all(i.isalnum() for i in s)

main()
