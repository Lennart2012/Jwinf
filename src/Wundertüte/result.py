from tkinter import *


class Result():
    @staticmethod
    def showresult():
        root = Tk()
        root.title('Your result is here! - Distributor (Wundertüte)')
        root.geometry('600x400')
        root.iconbitmap("img\icon.ico")
        root.attributes("-topmost", True)
        message = open("output.txt", 'r').read()

        def on_closing():
            root.quit()  # Verwende root.quit(), um die Tkinter-Hauptschleife zu beenden

        root.protocol("WM_DELETE_WINDOW", on_closing)

        text_box = Text(
            root,
            height=30,
            width=100
        )
        text_box.pack(expand=True)
        text_box.insert('end', message)
        text_box.config(state='disabled')
        root.mainloop()
