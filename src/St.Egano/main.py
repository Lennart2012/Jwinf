# main.py
import sys
from tkinter import Tk, PhotoImage
from tkinter.filedialog import askopenfilename
from PIL import Image
from imagereader import ImageReader
from ascii import ascii_convert
print('All work is copyrighted by GNU GENERAL PUBLIC LICENSE. View the License.exe for more information.')

root = Tk()
root.withdraw()
logo_path = "img/icon.png"
logo = PhotoImage(file=logo_path)
running = True
answer = []
printableanswer = ""


def get_image_path():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        root.tk.call('wm', 'iconphoto', root._w, logo)

        file_path = askopenfilename(title="Bild auswählen", filetypes=[(
            "Images", "*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.tiff;*.tif")])

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
    while running:
        r, g, b = image_reader.get_pixel_values(x, y)

        if b == 0 and g == 0:
            running = False

        answer.append(ascii_convert(r))
        print(f"Found letter {ascii_convert(r)}")

        x = (x + g) % image_width
        y = (y + b) % image_height
    for letter in answer:
        printableanswer += letter
    if answer == "":
        print("Looks like there is no code hidden...")
    print(f"Work done! Answer: {printableanswer}")
    exit()
