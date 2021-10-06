from tkinter import *

def rotate(input_image_path, output_image_path, degree):
    img = Image.open(input_image_path)
    filter = img.rotate(degree)
    filter.save(output_image_path)