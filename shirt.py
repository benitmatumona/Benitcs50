import sys, os, re
from PIL import Image, ImageOps

def main():
    paste()

def paste():
    try:
        files = sys.argv
        if len(files) < 3:
            sys.exit('Too few command-line arguments')
        elif len(files) > 3:
            sys.exit('Too many command-line arguments')
        elif os.path.splitext(files[1])[1] != os.path.splitext(files[2])[1]:
            sys.exit('Input and output have different extentions')
        elif os.path.splitext(files[1])[1].lower() not in ['.jpg','.jpeg','.png']:
            sys.exit('Invalid input')
        with Image.open("shirt.png") as file1, Image.open(files[1]) as file2:
            file2 = ImageOps.fit(file2,file1.size)
            file2.paste(file1,(0, 0), file1.convert("RGBA"))
            file2 = file2.convert("RGB") if re.fullmatch(r'.+\.["jpg""jepg"]', files[2], re.IGNORECASE) else file2
            file2.save(files[2])
    except FileNotFoundError:
        sys.exit(f'{files[1]} not found')

if __name__ == '__main__':
    main()
