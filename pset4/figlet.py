import sys, random
from pyfiglet import Figlet

figlet = Figlet()


def main(argv):
    if set_figlet_font(argv):
        render_message()
    else:
        sys.exit("Invalid usage")



def set_figlet_font(argv):
    font_list = figlet.getFonts()
    is_font_set = False
    if len(argv) == 1:
        figlet.setFont(font = font_list[random.randint(0, 424)])
        is_font_set = True
    elif len(argv) == 3:
        if argv[1] == "-f" or argv[1] == "--font":
            if argv[2] in font_list:
                figlet.setFont(font = argv[2])
                is_font_set = True

    return is_font_set


def render_message():
    message = input("Input: ")
    print("Output:", figlet.renderText(message), sep="\n")


if __name__ == "__main__":
    main(sys.argv)
