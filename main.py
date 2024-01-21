from colorthief import ColorThief
from os import system


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


def get_image_colors(file: str = "path", color_count: int = 5):
    try:
        image = ColorThief(file=file)
        print("Loaded successfully! Wait a bit")

        result = image.get_palette(quality=1, color_count= color_count)

        return result
    except:
        print("No such image!")

def convert_rgb_to_hex(rgb_color: tuple):
    hex_color: str = '{:X}{:X}{:X}'.format(*rgb_color)
    result: str = "FF"+hex_color

    return result

def main():
    while True:
        system('cls||clear')
        print(TITLE)
        print(INF)

        try:
            image_uri = str(input("Path to image with palette: "))
            color_count: int = int(input("Number of colors on the palette: "))
        except ValueError:
            print("An error has occurred!")
            
        colors = get_image_colors(file=image_uri, color_count=color_count)
        file = open("palette.txt", "w")
        try:
            for color in colors:
                file.write(convert_rgb_to_hex(color) + "\n")
        except: 
            pass
        
        input("Done, press Enter to go back...")


if __name__ == "__main__":
    main()