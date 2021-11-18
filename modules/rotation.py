from tkinter import *
from PIL import Image

def rotate(input_image_path, output_image_path, degree):
    img = Image.open(input_image_path)
    filter = img.rotate(int(degree))
    filter.save(output_image_path)
    return output_image_path