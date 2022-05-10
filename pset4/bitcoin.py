import sys, requests


def main():
    print(f"${get_bitcoin_rate_float() * get_amount(sys.argv):,.4f}")


def get_amount(argv):
    amount = 0
    if len(argv) == 1:
        sys.exit("Missing command-line argument")
    elif len(argv) > 2:
        sys.exit("Invalid Usage")
    else:
        try:
            amount = float(argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")
    return amount


def get_bitcoin_rate_float():
    rate_float = 0
    try:
        request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response = request.json()
        rate_float = response["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit("An error has occurred with the request")
    return rate_float


if __name__ == "__main__":
    main()
