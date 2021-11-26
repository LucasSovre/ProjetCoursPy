import sys
sys.path
sys.path.append('../')
from modules.b_and_w import *
from modules.redimensionner import sizeFunction
from modules.rotation import *
import os

class Preset : 
    def __init__ (self,black_and_white,contrast,sharpness,saturation,redimension,rotation):
        #premièrement nous récupérons toutes les valeurs nécéssaires pour le traitement d'image
        self.black_and_white = black_and_white
        self.contrast = contrast
        self.sharpness =sharpness
        self.saturation = saturation
        self.redimension = redimension
        self.rotation = rotation
    
    def apply (self,abs_file_path):
        if(self.black_and_white == True): #le filtre noir est blanc dois dabord être appliqué seul
            black_and_white(abs_file_path,abs_file_path)
        #puis nous appliquons toutes les fonctions de manière récursives à l'image choisie
        contrastFunction(abs_file_path,abs_file_path,self.contrast)
        sharpnessFunction(abs_file_path,abs_file_path,self.sharpness)
        saturationFunction(abs_file_path,abs_file_path,self.saturation)
        rotate(abs_file_path,abs_file_path,self.rotation)
        if self.redimension[0] != "" and self.redimension[1] != "" :
            sizeFunction(abs_file_path,abs_file_path,int(self.redimension[0]),int(self.redimension[1]))