import tkinter
from tkinter import *
from PIL import Image
from Capture import *

def main():

    window = Tk()
    window.geometry("1280x800")
    window.title("DSL")
    window.configure(bg="#969696")

    background_intro = tkinter.PhotoImage(file="Pics\main_screen.png")
    background_label = tkinter.Label(window, image=background_intro)
    background_label.PhotoImage = background_intro
    background_label.place(x=0, y=0)
    background_label.pack()

    start = Image.open("Pics/startButton.png")
    startBut = ImageTk.PhotoImage(start)

    library = Image.open("Pics/libraryButton.png")
    libraryBut = ImageTk.PhotoImage(library)

    ext = Image.open("Pics/Hopstarter-Sleek-Xp-Basic-Close-2.ico")
    extBut = ImageTk.PhotoImage(ext)

    def start():
        print("start button pressed")
        window.destroy()
        capture()

    def library():
        print("library button pressed")

    def exit1():
        exit()

    buttonStart = Button(window, image=startBut, bg="white", width=500, height=115, relief=FLAT, command=start)
    buttonStart.place(x=389, y=299)

    buttonLibrary = Button(window, image=libraryBut, bg="white", width=500, height=120, relief=FLAT, command=library)
    buttonLibrary.place(x=389, y=460)

    buttonExit = Button(window, image=extBut, bg="#73c3ff", width=70, height=70, relief=FLAT, command=exit1)
    buttonExit.place(x=1170, y=20)

    window.mainloop()
