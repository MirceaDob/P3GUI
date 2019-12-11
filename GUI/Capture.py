import tkinter
from tkinter import *
from PIL import Image, ImageTk


def capture():

    window = Tk()
    window.geometry("1280x800")
    window.title("DSL")
    window.configure(bg="#969696")

    background_intro = tkinter.PhotoImage(file="Pics\capture_bckgrnd.png")
    background_label = tkinter.Label(window, image=background_intro)
    background_label.PhotoImage = background_intro
    background_label.place(x=0, y=0)
    background_label.pack()

    ext = Image.open("Pics/Hopstarter-Sleek-Xp-Basic-Close-2.ico")
    extBut = ImageTk.PhotoImage(ext)

    bck = Image.open("Pics/capture_back.png")
    bckBut = ImageTk.PhotoImage(bck)

    def back():
        print("back button pressed")


    def exit1():
        exit()

    bckBut = Button(window, image=bckBut, bg="#73c3ff", width=98, height=102, relief=FLAT, command=back)
    bckBut.place(x=17, y=75)

    buttonExit = Button(window, image=extBut, bg="#73c3ff", width=70, height=70, relief=FLAT, command=exit1)
    buttonExit.place(x=1170, y=20)

    window.mainloop()
