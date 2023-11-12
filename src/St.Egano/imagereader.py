# imagereader.py
from PIL import Image
import os

class ImageReader:
    def __init__(self, image_path):
        if not os.path.exists(image_path):
            print(f"Fehler: Das Bild unter dem Pfad '{image_path}' wurde nicht gefunden.")
            exit()

        self.image = Image.open(image_path)
        self.width, self.height = self.image.size

    def load_image(self):
        return self.image

    def get_pixel_rgb(self, x, y):
        # Überprüfen, ob die Koordinaten innerhalb der Grenzen des Bildes liegen
        if 0 <= x < self.width and 0 <= y < self.height:
            rgb = self.image.convert("RGB").getpixel((x, y))
            return rgb
        else:
            raise ValueError("Ungültige Koordinaten")
    
    def get_pixel_values(self, x, y):
        # Holen Sie sich die RGB-Werte
        rgb = self.get_pixel_rgb(x, y)
        
        # Aufteilen in R, G, B
        r, g, b = rgb
        return r, g, b
