import tkinter
from tkinter import *
from PIL import Image, ImageTk


window = Tk()
window.geometry("1280x800")
window.title("DSL")
window.configure(bg="#969696")

background_intro = tkinter.PhotoImage(file="Pics\main_screen.png")
background_label = tkinter.Label(window, image=background_intro)
background_label.PhotoImage = background_intro
background_label.place(x=0, y=0)
background_label.pack()

bck = Image.open("Pics/agt_back.ico")
bckBut = ImageTk.PhotoImage(bck)
# but1 = Button(image=bckBut)

hom = Image.open("Pics/Hopstarter-Sleek-Xp-Basic-Home.ico")
homBut = ImageTk.PhotoImage(hom)
# but2 = Button(image=homBut)

# cam = Image.open("Pics/Martz90-Circle-Video-camera.ico")
# camBut = ImageTk.PhotoImage(cam)
# but3 = Button(image=camBut)

ext = Image.open("Pics/Hopstarter-Sleek-Xp-Basic-Close-2.ico")
extBut = ImageTk.PhotoImage(ext)
# but4 = Button(image=extBut)


def back():
    print("back button pressed")


def home():
    print("home button pressed")


# def camera():
  #  print("camera button pressed")


def exit1():
    exit()


button1 = Button(window, image=bckBut, bg="white", width=70, height=70, relief=FLAT, command=back)
button1.place(x=341, y=291)

button2 = Button(window, image=homBut, bg="white", width=70, height=70, relief=FLAT, command=home)
button2.place(x=341, y=455)

# button3 = Button(window, image=camBut, bg="white", width=70, height=70, relief=FLAT, command=camera)
# button3.place(x=565, y=600)

button4 = Button(window, image=extBut, bg="#73c3ff", width=70, height=70, relief=FLAT, command=exit1)
button4.place(x=1170, y=20)

window.mainloop()
