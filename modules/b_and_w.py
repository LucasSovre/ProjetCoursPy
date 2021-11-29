from PIL import Image, ImageEnhance                                 # On import la bibliotheque PIL qui sert de traitement d'images

def black_and_white(input_image_path,output_image_path):            # Il s'agit de la fonction noir et blanc qui prend 2 entrées, une entrée d'image avec spn chemin (celle que l'on souhaite modifier), et une sortie d'image (celle qui sera rendue en noir et blanc)
   color_image = Image.open(input_image_path)                       # L'image d'entrée est selectionnée grâce a la fonction Image.open() que l'on met dans la variable color_image
   bw = color_image.convert('L')                                    # On converti l'image en noir et blanc avec la fontion .convert('L') et on le met dans la variable bw
   bw.convert("RGBA")                                               # On converti également notre image en RGVA afin de pouvoir modifier son opacité si on le souhaite
   bw.save(output_image_path)                                       # on sauvegarde notre modification dans la variable output_image_path avec la fonction .save()
   return output_image_path                                         # On retourne notre nouvelle image après sa modification

def saturationFunction(input_image_path,output_image_path,level):   # Il s'agit de la fonction Saturation pour notre image, et elle reprend les mêmes entrées que pour noir et blanc, mais également une nouvelle entrée nommée "level" pour le niveau d'intensité de la saturation
    img = Image.open(input_image_path)                              # On nomme la variable de notre image "img"
    img = img.convert("RGBA")                                       # On converti notre image en RGVA 
    filter = ImageEnhance.Color(img)                                # On selectionne la saturation pour notre image avec la fonction ImageEnhance.Color() que l'on glisse dans la variable filter
    filter.enhance(int(level)).save(output_image_path)              # On contrôle le niveau de saturation avec la variable entière "level" dans la fonction .ImageEnhance(int()) et que l'on sauvegarde ensuite avec .save()
    return output_image_path                                        # On retourne notre nouvelle image après sa modification

def sharpnessFunction(input_image_path,output_image_path,level):    # Il s'agit de la fonction Dureté pour notre image, elle reprend les mêmes entrées que pour Contraste
    img = Image.open(input_image_path)                              # On nomme la variable de notre image "img"
    img = img.convert("RGBA")                                       # On converti notre image en RGVA 
    filter = ImageEnhance.Sharpness(img)                            # On selectionne la dureté avec la fonction ImageEnhance.Sharpness() que l'on glisse dans la variable filter
    filter.enhance(int(level)).save(output_image_path)              # On contrôle le niveau de dureté avec la variable "level" et que l'on sauvegarde ensuite avec .save()
    return output_image_path                                        # On retourne notre nouvelle image après sa modification

def contrastFunction(input_image_path,output_image_path,level):     # Il s'agit de la fonction Constraste pour notre image, elle reprend les mêmes entrées que pour Contraste
    img = Image.open(input_image_path)                              # On nomme la variable de notre image "img"
    img = img.convert("RGBA")                                       # On converti notre image en RGVA 
    filter = ImageEnhance.Contrast(img)                             # On selectionne la dureté avec la fonction ImageEnhance.Contrast() que l'on glisse dans la variable filter
    filter.enhance(int(level)).save(output_image_path)              # On contrôle le niveau de contraste avec la variable "level" et que l'on sauvegarde ensuite avec .save()
    return output_image_path                                        # On retourne notre nouvelle image après sa modification
