from colorthief import ColorThief
from os import system
from typing import NamedTuple
from exception import CantGetPaletteData

TITLE: str = """
 ___  _   _    ___  ___  ___  ___   __   ___  _   _  _  _  ___ 
| o \/ \ | |  | __||_ _||_ _|| __| [o ) | o \/ \ | || \| ||_ _|
|  _/ o || |_ | _|  | |  | | | _|   /(  |  _/ o || || \\  | | | 
|_| |_n_||___||___| |_|  |_| |___| /__| |_| |_n_||_||_|\_| |_| """

INF: str = """
Palette2paintNet - This program is for creating a palette from a photograph 
(or a ready-made palette in photo format) for paint.net.
After creating the palette, you are given a txt file 
with the main colors in the photo, which can be used in paint.net

gh - github.com/Hindbeer/palette2paintNet
yt - youtube.com/@kuve.
"""


class PaletteInfo(NamedTuple):
    file_path: str
    colors_count: int


def get_file_path() -> str:
    try:
        return str(input("Path to image with palette: "))
    except ValueError:
        raise CantGetPaletteData


def get_colors_count() -> int:
    try:
        return int(input("Number of colors on the palette: "))
    except ValueError:
        raise CantGetPaletteData


def get_image_colors(palette_info: PaletteInfo) -> tuple:
    try:
        image = ColorThief(file=palette_info.file_path)
    except ValueError:
        raise CantGetPaletteData
    print("Loaded successfully! Wait a bit")
    return image.get_palette(quality=1, color_count=palette_info.colors_count)


def get_palette_info() -> PaletteInfo:
    file_path = get_file_path()
    colors_count = get_colors_count()
    return PaletteInfo(file_path=file_path, colors_count=colors_count)


def convert_rgb_to_hex(rgb_color: tuple) -> str:
    hex_color: str = "{:X}{:X}{:X}".format(*rgb_color)
    return "FF" + hex_color


def write_to_file(colors: tuple) -> None:
    file = open("palette.txt", "w")

    for color in colors:
        file.write(convert_rgb_to_hex(color) + "\n")


def main():
    while True:
        system("cls||clear")
        print(TITLE)
        print(INF)

        palette_info = get_palette_info()
        colors = get_image_colors(palette_info=palette_info)
        write_to_file(colors=colors)

        input("Done, press Enter to go back...")


if __name__ == "__main__":
    main()
