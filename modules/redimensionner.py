from tkinter import *
from PIL import Image

def sizeFunction(input_image_path, output_image_path,lenght, width):
    img = Image.open(input_image_path)
    filter = img.resize((lenght,width),Image.ANTIALIAS)
    filter.save(output_image_path)