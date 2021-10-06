from PIL import Image, ImageEnhance

def black_and_white(input_image_path,output_image_path):
   color_image = Image.open(input_image_path)
   bw = color_image.convert('L')
   bw.save(output_image_path)

def saturation(input_image_path,output_image_path,level):
    img = Image.open(input_image_path)
    filter = ImageEnhance.Color(img)
    filter.enhance(level).save(output_image_path)

def sharpness(input_image_path,output_image_path,level):
    img = Image.open(input_image_path)
    filter = ImageEnhance.Sharpness(img)
    filter.enhance(level).save(output_image_path)

def contrast(input_image_path,output_image_path,level):
    img = Image.open(input_image_path)
    filter = ImageEnhance.Contrast(img)
    filter.enhance(level).save(output_image_path)
