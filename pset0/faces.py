def main():
    faces()


def faces():
    emoji = {
        ":)": "🙂",
        ":(": "🙁"
    }
    output = ""
    user_input = input().split()
    for word in user_input:
        output += emoji.get(word, word) + " "
    print(output.strip())


if __name__ == "__main__":
    main()