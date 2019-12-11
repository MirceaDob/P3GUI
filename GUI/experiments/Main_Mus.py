import tkinter
from tkinter import *
import pygame
pygame.init()


def main_mus():

    window = Tk()
    window.geometry("1280x800")
    window.title("DSL")
    window.configure(bg="#969696")

    background_intro = tkinter.PhotoImage(file="Pics\main_screen.png")
    background_label = tkinter.Label(window, image=background_intro)
    background_label.PhotoImage = background_intro
    background_label.pack()

    if pygame.event.get() == pygame.MOUSEBUTTONDOWN:
        (x, y) = pygame.mouse.get_pos()
        # if (0, 0) < (x, y) < (500, 500):
        print(x, y)
        print("back button pressed")

    window.mainloop()
