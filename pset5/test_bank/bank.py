import string


def main():
    user_input = input("Greeting:")
    print(value(user_input))


def value(user_greeting):
    user_greeting = user_greeting.translate(str.maketrans("", "", string.punctuation))
    greeting = user_greeting.lower().replace("","").split()
    print(greeting)
    penalty = 1
    if greeting[0] == "hello":
        penalty = 0
    elif greeting[0][0] == "h":
        penalty = 20
    else:
        penalty = 100
    return penalty


if __name__ == "__main__":
    main()