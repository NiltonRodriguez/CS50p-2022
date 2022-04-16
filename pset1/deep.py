def main():
    deep_thought()


def deep_thought():
    user_input = input("What is the Answer to the Great Question of Life, the Universe and Everything? ").lower().strip()
    answers = ["42", "forty two", "forty-two"]
    if user_input in answers:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()