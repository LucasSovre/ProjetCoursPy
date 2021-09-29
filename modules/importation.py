from tkinter import filedialog as fd
import shutil

def select_files():
    filetypes = (
        ('text files', '*.png'),
        ('All files', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)


    strFilenames = str(filenames).replace('(','').replace(')','').replace(',','').replace("'",'')
    shutil.copy(strFilenames,'cache/')
    tupleFile = strFilenames.split("/")
    fileLenght = len(tupleFile)
    file = tupleFile[fileLenght-1]
    print(file)
    