def main():
    energy_calc()


def energy_calc():
    user_mass = int(input())
    c = 300000000
    print("E:", user_mass * pow(c, 2))


if __name__ == "__main__":
    main()