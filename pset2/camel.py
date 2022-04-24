def main():
    userInput = input("camelCase: ")
    to_snake(userInput)


def to_snake(camel_string):
    snake_string = ""
    for i in range(len(camel_string)):
        if i != 0:
            if camel_string[i].isupper():
                snake_string += f"_{camel_string[i].lower()}"
                continue
        snake_string += camel_string[i]
    print("snake_case:", snake_string)


if __name__ == "__main__":
    main()