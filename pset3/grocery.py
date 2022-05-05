def main():
    display_list()


def display_list():
    grocery_list = {}
    while True:
        try:
            item = input().upper()
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
        except EOFError:
            for k, v in sorted(grocery_list.items()):
                        print(v, k)
            break


if __name__ == "__main__":
    main()