_A='output.txt'
import sys,os
from tkinter import Tk,filedialog
from tkinter import*
from PIL import Image
print('All work is copyrighted by GNU GENERAL PUBLIC LICENSE. View the License (in main directory) for more information.')
root=Tk()
root.withdraw()
running=True
answer=[]
printableanswer=''
def get_image_path():
	if len(sys.argv)>1:return sys.argv[1]
	else:
		root.iconbitmap(os.path.abspath('img/icon.ico'));file_path=filedialog.askopenfilename(title='Bild auswählen',filetypes=[('Images','*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.tiff;*.tif')]);root.iconbitmap(default='')
		if not file_path:print('No image selected. Programm is crashing.');sys.exit()
		return file_path
class ImageReader:
	def __init__(self,image_path):
		if not os.path.exists(image_path):print(f"Fehler: Das Bild unter dem Pfad '{image_path}' wurde nicht gefunden.");exit()
		self.image=Image.open(image_path);self.width,self.height=self.image.size
	def load_image(self):return self.image
	def get_pixel_rgb(self,x,y):
		if 0<=x<self.width and 0<=y<self.height:rgb=self.image.convert('RGB').getpixel((x,y));return rgb
		else:raise ValueError('Ungültige Koordinaten')
	def get_pixel_values(self,x,y):rgb=self.get_pixel_rgb(x,y);r,g,b=rgb;return r,g,b
	def get_image_dimensions(self):return self.width,self.height
def ascii_convert(number):
	try:text=chr(number);return text
	except ValueError as e:return f"Fehler: {e}"
class Result:
	@staticmethod
	def showresult():
		root=Tk();root.title('Your result is here! - Image Secret Text Reader (St.Egano)');root.geometry('600x400');root.iconbitmap('img\\icon.ico');root.attributes('-topmost',True);message=open(_A,'r').read()
		def on_closing():root.quit()
		root.protocol('WM_DELETE_WINDOW',on_closing);text_box=Text(root,height=30,width=100);text_box.pack(expand=True);text_box.insert('end',message);text_box.config(state='disabled');root.mainloop()
if __name__=='__main__':
	image_path=get_image_path();image_reader=ImageReader(image_path);loaded_image=image_reader.load_image();image_width,image_height=image_reader.get_image_dimensions();x=0;y=0;print('\x1b[93mStarted. Please wait...');print('Press Ctrl+C to cancel.\x1b[0m')
	while running:
		r,g,b=image_reader.get_pixel_values(x,y)
		if b==0 and g==0:running=False
		answer.append(ascii_convert(r));x=(x+g)%image_width;y=(y+b)%image_height
	for letter in answer:printableanswer+=letter
	f=open(_A,'w');f.write(printableanswer);f.close();print(f"[92mYour result is here! View output.txt[0m");Result.showresult()