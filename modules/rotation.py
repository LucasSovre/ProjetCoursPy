from tkinter import *

def rotate(display, lien, degree):
    img = Image.open(display)
    filter = img.rotate(degree)
    filter.save(lien)