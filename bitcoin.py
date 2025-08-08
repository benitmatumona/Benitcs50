import requests, sys

try:
    command = sys.argv
    if len(command) == 1:
        sys.exit("Missing command-line argumenting")
    number = float(command[1])
    info = requests.get("http://rest.coincap.io/v3/assets?apiKey=5f899cb2a98fce4172b5a7636ad6346d67adce853b44c11dce1ca57e7bd15f6e")
    dict = info.json()
except requests.RequestException :
    sys.exit(0)
except ValueError:
    sys.exit("Command-line argument is not a number")
else:
    print(f"${float(dict["data"][0]["priceUsd"])*number:,.4f}")


