from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
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

    showinfo(
        title='Selected Files',
        message=filenames
    )
    strFilenames = str(filenames).replace('(','').replace(')','').replace(',','').replace("'",'')
    shutil.copy(strFilenames,'cache/')
    tupleFile = strFilenames.split("/")
    fileLenght = len(tupleFile)
    file = tupleFile[fileLenght-1]
    print(file)
    