from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

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