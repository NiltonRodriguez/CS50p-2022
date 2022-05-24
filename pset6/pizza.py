import sys
from tabulate import tabulate


def main():
    if is_valid_command_line_argument(sys.argv):
        lines = get_lines(sys.argv[1])
        headers = lines[0]
        table = lines[1::]
        print(tabulate(table, headers, tablefmt="grid"))


def is_valid_command_line_argument(argv):
    if len(argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(argv) > 2:
        sys.exit("Too many command-line arguments")

    if ".csv" not in argv[1]:
        sys.exit("Not a CSV file")

    return True


def get_lines(csv_file):
    lines = []
    try:
        with open(csv_file) as file:
            for line in file:
                lines.append(line.strip().split(","))
    except FileNotFoundError:
        sys.exit("File does not exist")

    return lines


if __name__ == "__main__":
    main()
