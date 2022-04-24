def main():
    change_calc()


def change_calc():
    amount_due = 50
    accepted_coins = [25, 10, 5]
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        user_coin = int(input("Insert Coin: "))
        if user_coin in accepted_coins:
            amount_due -= user_coin
        if amount_due <= 0:
            print(f"Change Owed: {amount_due * -1}")


if __name__ == "__main__":
    main()