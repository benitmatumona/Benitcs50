from validator_collection import validators

def main():
    print(validate_email(input('Email: ')))

def validate_email(s:str) -> str:
    try:
        if validators.email(s):
            return 'Valid'
    except (validators.errors.InvalidEmailError, validators.errors.EmptyValueError):
        return 'Invalid'

if __name__ == "__main__":
    main()
