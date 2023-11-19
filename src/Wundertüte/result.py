from tkinter import *


class Result():
    def showresult():
        root = Tk()
        root.title('Your result is here! - Distributor (Wundertüte)')
        root.geometry('400x300')
        root.resizable(height=False, width=False)
        root.iconbitmap("img\icon.ico")
        root.attributes("-topmost", True)
        message = open("outputs.txt", 'r').read()

        text_box = Text(
            root,
            height=30,
            width=100
        )
        text_box.pack(expand=True)
        text_box.insert('end', message)
        text_box.config(state='disabled')
        # exit button

        root.mainloop()
