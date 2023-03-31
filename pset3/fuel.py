def main():
    print(fuel_lvl())


def fuel_lvl():
    level = ""
    while True:
        values = check_values()
        try:
            fuel = (values[0] / values[1]) * 100
            if fuel <= 1:
                level = "E"
            elif 1 < fuel < 99:
                level = f"{round(fuel)}%"
            elif 99 <= fuel <= 100:
                level = "F"
            else:
                continue
            break
        except ZeroDivisionError:
            continue
    return level


def check_values():
    while True:
        user_input = input("Fraction: ").split("/")
        try:
            user_input[0], user_input[1] = int(user_input[0]), int(user_input[1])
            break
        except ValueError:
            continue
    return user_input


if __name__ == "__main__":
    main()
