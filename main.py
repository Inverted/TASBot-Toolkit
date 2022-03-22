import os
import sys

import bcolors as bcolors
import numpy
from PIL import Image


def main(path):
    palette = get_palette_from_image(path)
    write_palette_to_file(palette, path)


def write_palette_to_file(palette, path):
    file_path = get_file_name(f"{os.path.splitext(path)[0]}.tasbotPalette")
    print(f"Write palette to \"{file_path}\"")

    with open(file_path, 'w') as f:
        file = open(file_path, "w")
        for c in palette:  # prefer this, to show what's added rather than writelines()
            print(f"{bcolors.OKMSG}Added #{c} to palette{bcolors.ENDC}")
            file.write(f"{c}\n")


def get_file_name(path):
    filename, extension = os.path.splitext(path)

    counter = 1
    while os.path.exists(path):
        path = f"{filename} ({str(counter)}){extension}"
        counter += 1

    return path


def get_palette_from_image(path):
    image = Image.open(path)
    image = image.convert('RGB')
    pixels = list(image.getdata())

    pixels = numpy.array(pixels).reshape((image.width, image.height, 3))

    raw_palette = []
    for x in range(image.width):
        for y in range(image.height):
            raw_palette.append(rgb_to_hex(pixels[x, y]))

    return list(set(raw_palette))


def rgb_to_hex(rgb_color):
    hex_color = ""
    for i in rgb_color:
        i = int(i)
        hex_color += ("{:02x}".format(i))
    return hex_color


if __name__ == '__main__':
    print(f"{bcolors.HEADER}===because==={bcolors.ENDC}")
    print(f"{bcolors.HEADER}tasBot Eye Color Analyzing Uniquified Search Engine{bcolors.ENDC}")
    print(f"{bcolors.HEADER}============={bcolors.ENDC}")

    if len(sys.argv) > 1:
        image_path = str(sys.argv[1])
        print(f"Read image \" {image_path}\"")
        main(image_path)
    else:
        print(f"{bcolors.ERRMSG}Please provide a path to a image file!{bcolors.ENDC}")
        print("Usage:\n    because <file to image>")
