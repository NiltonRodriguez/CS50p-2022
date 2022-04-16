import string


def main():
    greeting()


def greeting():
    user_input = input("Greeting:").translate(str.maketrans("", "", string.punctuation))
    greeting = user_input.lower().replace("","").split()
    if greeting[0] == "hello":
        print("$0")
    elif greeting[0][0] == "h":
        print("$20")
    else:
        print("$100")


if __name__ == "__main__":
    main()