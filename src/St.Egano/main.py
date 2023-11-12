# main.py
import sys
from tkinter import Tk, PhotoImage
from tkinter.filedialog import askopenfilename
from PIL import Image
from imagereader import ImageReader


root = Tk()
root.withdraw()
logo_path = "img/icon.png"
logo = PhotoImage(file=logo_path)

def get_image_path():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        
        root.tk.call('wm', 'iconphoto', root._w, logo)

        file_path = askopenfilename(title="Bild auswählen", filetypes=[("Images", "*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.tiff;*.tif")])

        if not file_path:
            print("Kein Bild ausgewählt. Programm wird beendet.")
            sys.exit()

        return file_path



if __name__ == "__main__":
    x=0
    y=0
    
    image_path = get_image_path()
    image_reader = ImageReader(image_path)
    loaded_image = image_reader.load_image()
    
    r, g, b = image_reader.get_pixel_values(x, y)

    print(f"R: {r}, G: {g}, B: {b}")
