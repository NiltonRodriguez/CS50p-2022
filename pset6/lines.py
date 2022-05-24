import sys


def main():
    if is_valid_command_line_argument(sys.argv):
        lines = get_lines(sys.argv[1])
        print(count_lines(lines))


def is_valid_command_line_argument(argv):
    if len(argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(argv) > 2:
        sys.exit("Too many command-line arguments")

    if ".py" not in argv[1]:
        sys.exit("Not a Python file")

    return True


def get_lines(python_file):
    lines = []
    try:
        with open(python_file) as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    return lines


def count_lines(lines):
    count = 0
    for line in lines:
        line = line.strip()
        if len(line) > 0:
            if line[0] != "#":
                count += 1

    return count


if __name__ == "__main__":
    main()
