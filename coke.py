def main():
    print(change())

def change():
    coin = 0
    amount_due = 50
    while amount_due > 0:
        coin = int(input(f"Amount Due: {amount_due}\nInsert Coin: "))
        amount_due -= coin if coin in (5,10,25) else 0
    return f"Change Owed: {0-amount_due}"

if __name__ == "__main__":
    main()
