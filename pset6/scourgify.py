import sys, csv


def main():
    if is_valid_command_line_argument(sys.argv):
        create_new_csv(sys.argv[1], sys.argv[2])


def is_valid_command_line_argument(argv):
    if len(argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(argv) > 3:
        sys.exit("Too many command-line arguments")

    if ".csv" not in argv[1]:
        sys.exit(f"Could not read {argv[1]}")

    return True


def create_new_csv(csv_input, csv_output):
    try:
        with open(csv_input) as csvfile:
            reader = csv.DictReader(csvfile)
            with open(csv_output, "w", newline="") as new_file:
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(new_file, fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    name = row["name"].replace("\"", "").split(",")
                    writer.writerow({"first": name[1].strip(), "last": name[0].strip(), "house": row["house"].strip()})
    except FileNotFoundError:
        sys.exit(f"Could not read {argv[1]}")


if __name__ == "__main__":
    main()
