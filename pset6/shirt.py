import sys
from os.path import splitext
from PIL import Image, ImageOps


def main():
    if is_valid_command_line_argument(sys.argv):
        overlay_images(sys.argv[1], sys.argv[2])


def is_valid_command_line_argument(argv):
    if len(argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(argv) > 3:
        sys.exit("Too many command-line arguments")

    supported_files = [".jpeg", ".jpg", ".png"]
    input_file = splitext(argv[1])
    output_file = splitext(argv[2])

    if input_file[1].lower() not in supported_files:
        sys.exit("Invalid input")

    if output_file[1].lower() not in supported_files:
        sys.exit("Invalid output")

    if input_file[1].lower() != output_file[1].lower():
        sys.exit("Input and output have different extensions")

    return True


def overlay_images(input_image, output_image):
    try:
        with Image.open("shirt.png") as shirt:
            with Image.open(input_image) as base_image:
                base_image = ImageOps.fit(base_image, shirt.size)
                base_image.paste(shirt, shirt)
                base_image.save(output_image)


    except FileNotFoundError:
        sys.exit("Input does not exist")
    except OSError:
        sys.exit(f"Can not convert {input_image}")


if __name__ == "__main__":
    main()
