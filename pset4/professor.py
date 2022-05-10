import random


def main():
    selected_level = get_level()
    print(calc_result(selected_level))


def get_level():
    level = 0
    while True:
        try:
            level = int(input("Level: "))
            if 0 >= level or level > 3:
                raise ValueError
            break
        except ValueError:
            continue
    return level


def generate_integer(level):
    base = level - 1
    start = [0, 10, 100]
    stop = [9, 99, 999]
    return random.randint(start[base], stop[base])


def calc_result(level):
    score = 10
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y
        first_try = True
        error = 3
        while True:
            try:
                answer = int(input(f"{x} + {y} = "))
                break
            except ValueError:
                if first_try:
                    score -= 1
                    first_try = False
                error -= 1
                if error == 0:
                        print(z)
                        break
                print("EEE")
                continue
        if answer != z:
            if first_try:
                    score -= 1
            while answer != z:
                try:
                    error -= 1
                    if error == 0:
                        break
                    print("EEE")
                    answer = int(input(f"{x} + {y} = "))
                except ValueError:
                    error -= 1
                    print("EEE")
                    continue
            print(z)

    return f"Score: {score}"


def check_errors(error, answer):
    if error == 0:
        print(answer)
        return True


if __name__ == "__main__":
    main()
