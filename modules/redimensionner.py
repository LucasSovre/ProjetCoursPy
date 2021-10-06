from tkinter import *

def newSize(input_image_path, output_image_path, lenght, width):
    img = Image.open(input_image_path)
    filter = img.geometry("'" + lenght.get() + "x" + width.get() + "'")
    filter.save(output_image_path)