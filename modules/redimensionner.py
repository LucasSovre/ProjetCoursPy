from tkinter import *

def newSize(display, lenght, width):
    return display.geometry("'" + lenght.get() + "x" + width.get() + "'")