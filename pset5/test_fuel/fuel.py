def main():
    while True:
        try:
            fraction = input("Fraction: ")
            print (gauge(convert(fraction)))
            break
        except (ValueError, ZeroDivisionError):
            continue



def gauge(percentage):
    level = ""
    while True:
        if percentage <= 1:
            level = "E"
        elif 1 < percentage < 99:
            level = f"{round(percentage)}%"
        elif 99 <= percentage <= 100:
            level = ("F")
        else:
            raise ValueError
        break
    return level


def convert(fraction):
    user_input = fraction.split("/")
    user_input[0], user_input[1] = int(user_input[0]), int(user_input[1])
    percentage = (user_input[0] / user_input[1]) * 100

    return percentage


if __name__ == "__main__":
    main()
