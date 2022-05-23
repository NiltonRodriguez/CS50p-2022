def main():
    user_input = input("Input: ")
    print(shorten(user_input))


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    no_vowels = ""
    for character in word:
        if character.lower() not in vowels:
            no_vowels += character
    return no_vowels


if __name__ == "__main__":
    main()