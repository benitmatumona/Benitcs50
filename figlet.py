import random
import sys
from pyfiglet import Figlet

def main():
    print(figlet())

def figlet():
    figlet = Figlet()
    fonts = figlet.getFonts()
    while True:
        style = sys.argv
        try:
            if len(style) not in [1,3]:
                raise ValueError()
            elif len(style) == 3:
                if (style[1] not in ["-f","--font"]) or (style[2] not in fonts):
                    raise ValueError()
        except ValueError:
            sys.exit("invalid usage")
        else:
            text = input("Input: ")
            if text == "":
                continue
            elif len(style) == 1:
                style = random.choice(fonts)
                figlet.setFont(font = style)
            elif len(style) == 3:
                figlet.setFont(font = style[2])

            return figlet.renderText(text)


if __name__ == "__main__":
    main()
