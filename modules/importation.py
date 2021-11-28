from tkinter import filedialog as fd
import shutil
import os

def select_files(outputName):
    filetypes = (
        ('image files', '*.png'),
        ('All files', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)


    strFilenames = str(filenames).replace('(','').replace(')','').replace(',','').replace("'",'')   #Chaine de caractère du chemin du ficher
    shutil.copy(strFilenames,'cache/')                                                              #Copier dans le dossier cache
    tupleFile = strFilenames.split("/")                                                             #Liste du chemin du fichier séparer par les /
    fileLenght = len(tupleFile)                                                                     #Taille de la lsite
    file = tupleFile[fileLenght-1]                                                                  #On récupère le dernier élément de la liste qui est le nom du fichier
    os.rename(r'cache/'+file,r'cache/'+outputName+'.png')                                           #on renome le fichier copié
    return('cache/'+outputName+'.png')                                                              #retourne le chemi du fichier
    