# main.py
import sys
import os
from tkinter import Tk, filedialog
from imagereader import ImageReader
from ascii import ascii_convert
from result import Result

print('All work is copyrighted by GNU GENERAL PUBLIC LICENSE. View the License.exe for more information.')

root = Tk()
root.withdraw()
running = True
answer = []
printableanswer = ""


def get_image_path():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        # Ändern Sie dies entsprechend dem tatsächlichen Pfad zu Ihrer Icon-Datei
        root.iconbitmap(os.path.abspath("img/icon.ico"))
        file_path = filedialog.askopenfilename(title="Bild auswählen", filetypes=[
            ("Images", "*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.tiff;*.tif")])
        # Setzen Sie das Icon des Hauptfensters zurück
        root.iconbitmap(default='')

        if not file_path:
            print("Kein Bild ausgewählt. Programm wird beendet.")
            sys.exit()

        return file_path


if __name__ == "__main__":
    image_path = get_image_path()
    image_reader = ImageReader(image_path)
    loaded_image = image_reader.load_image()
    image_width, image_height = image_reader.get_image_dimensions()

    x = 0
    y = 0

    print("\033[93mStarted. Please wait...\033[0m")
    print("\033[93mPress Ctrl+C to cancel.\033[0m")
    while running:
        r, g, b = image_reader.get_pixel_values(x, y)

        if b == 0 and g == 0:
            running = False

        answer.append(ascii_convert(r))

        x = (x + g) % image_width
        y = (y + b) % image_height

    for letter in answer:
        printableanswer += letter
    f = open("output.txt", "w")
    f.write(printableanswer)
    f.close()

    print(f"\033[92mYour result is here! View output.txt\033[0m")
    Result.showresult()
