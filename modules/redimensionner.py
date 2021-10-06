from tkinter import *

def newSize(display, lien, lenght, width):
    img = Image.open(display)
    filter = img.geometry("'" + lenght.get() + "x" + width.get() + "'")
    filter.save(lien)