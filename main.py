from tkinter import *
from tkinter import messagebox
from os import remove
import glob 
from PIL import Image
from modules.importation import *
from modules.b_and_w import *
from modules.redimensionner import sizeFunction
from modules.rotation import *

mainUI = Tk() #on instentie la fenetre principale du programme
mainUI.title('main') #renomme la fenetre principale
mainUI.geometry("1500x800")

index = 0
#on efface le cache de la session precedente
files = glob.glob('./cache/*') #selectionne tout les fichiers dans le cache
for f in files : 
    os.remove(f) #efface les fichiers 1 par 1

menuBar = Menu(mainUI) #création du menu principal
mainUI.config(menu=menuBar) #on defini le menu
subMenuFile = Menu(menuBar) #on défini le sous menu 
subMenuHelp = Menu(menuBar)
menuBar.add_cascade(label='Fichier', menu=subMenuFile)
subMenuFile.add_command(label='Importer', command=lambda : (display.initImg(select_files(str(index)))))
subMenuFile.add_command(label='Exporter')
menuBar.add_cascade(label='Aide', menu=subMenuHelp)

mainUI.columnconfigure(0, weight="1")#configuration des colonnes et lignes de la fenêtre principale
mainUI.columnconfigure(1, weight="6")
mainUI.columnconfigure(2, weight="3")
mainUI.rowconfigure(0, weight="1")
mainUI.rowconfigure(1 , weight="1")

toolbar = Frame(mainUI, background="green") #configuration de la barre d'outils
toolbar.grid(rowspan=2,row=0,column=0,sticky="nsew")
button1 = Button(toolbar, text="black & white", command=lambda : (display.black_and_white()))
button1.pack()

nextAndPrev = Frame(toolbar)
nextAndPrev.pack()
buttonPrev = Button(nextAndPrev, text="<--", command=lambda :(display.previousImg()))
buttonNext = Button(nextAndPrev, text="-->", command=lambda: (display.nexImg()))
buttonPrev.pack()
buttonNext.pack()

contrast = Frame(toolbar) #crée un frame pour l'input en question
contrast.pack()
button2 = Button(contrast, text='contrast',command=lambda : (display.contrast()))
button2.pack()
entryContrast = Entry(contrast)
entryContrast.pack()

sharpness = Frame(toolbar) #crée un frame pour l'input en question
sharpness.pack()
button3 = Button(sharpness, text='duretée',command=lambda : (display.sharpness()))
button3.pack()
entrySharpness = Entry(sharpness)
entrySharpness.pack()

saturation = Frame(toolbar) #crée un frame pour l'input en question
saturation.pack()
button4 = Button(saturation, text='saturation',command=lambda : (display.saturation()))
button4.pack()
entrySaturation = Entry(saturation)
entrySaturation.pack()

redimensionner = Frame(toolbar) #crée un frame pour l'input en question
redimensionner.pack()
button5 = Button(redimensionner, text='redimmensionner',command=lambda : (display.redimension()))
button5.pack()
entryRedimensionX = Entry(redimensionner)
entryRedimensionX.pack()
entryRedimensionY = Entry(redimensionner)
entryRedimensionY.pack()

rotation = Frame(toolbar) #crée un frame pour l'input en question
rotation.pack()
button6 = Button(rotation, text='Rotation',command=lambda : (display.rotation()))
button6.pack()
entryRotation = Entry(rotation)
entryRotation.pack()

visualization = Frame(mainUI, background="blue") #configuration du frame de canvas principal
visualization.grid(rowspan=2,row=0,column=1,sticky="nsew")

controlPanel = Frame(mainUI, background="yellow")#configuration du Frame controlPanel
controlPanel.grid(rowspan=2,row=0,column=2,sticky="nsew")

def verifyNumber(entry):
    if entry.isdigit():
        return entry
    else :
        messagebox.showerror("Erreur","L'entrée est incorecte, veuillez entrer un nombre entier svp")

class Displayed : 
    def __init__(self,parentFrame) :
        self.parentFrame = parentFrame
        self.canvas = Canvas(self.parentFrame,width=0,height=0)
        self.canvas.pack()

    def initImg(self,filename):
        global index
        self.filename = filename
        print(filename)
        self.image = PhotoImage(file=filename)
        pic = Image.open(filename)
        X,Y = pic.size
        self.canvas.config(width=X,height=Y)
        self.canvas.create_image(X/2,Y/2,image=self.image) #on affiche notre image sur le canvas
        self.canvas.update() #on update le canvas

    def previousImg(self):
        global index
        index = index - 1
        try :
            self.filename = './cache/' + str(index)+'.png'
            self.initImg('./cache/' + str(index)+'.png')
        except TclError:
            index = index + 1


    def nexImg(self):
        global index
        index = index + 1
        try :
            self.filename = './cache/' + str(index)+'.png'
            self.initImg('./cache/' + str(index)+'.png')
        except TclError:
            index = index - 1
    
    def black_and_white(self):
        global index
        index = index +1
        black_and_white(self.filename,'./cache/' + str(index) +'.png')
        self.initImg('./cache/' + str(index)+'.png')

    def contrast(self):
        global index
        index = index +1
        contrastFunction(self.filename,'./cache/' + str(index) +'.png',int(verifyNumber(entryContrast.get()))) #on viens directement chercher la valeur de l'entrée ici
        self.initImg('./cache/' + str(index)+'.png')

    def sharpness(self):
        global index
        index = index +1
        sharpnessFunction(self.filename,'./cache/' + str(index) +'.png',int(verifyNumber(entrySharpness.get()))) #on viens directement chercher la valeur de l'entrée ici
        self.initImg('./cache/' + str(index)+'.png')

    def saturation(self):
        global index
        index = index +1
        saturationFunction(self.filename,'./cache/' + str(index) +'.png',int(verifyNumber(entrySaturation.get()))) #on viens directement chercher la valeur de l'entrée ici
        self.initImg('./cache/' + str(index)+'.png')

    def redimension(self):
        global index
        index = index +1
        sizeFunction(self.filename,'./cache/' + str(index) +'.png',int(verifyNumber(entryRedimensionX.get())),int(verifyNumber(entryRedimensionY.get()))) #on viens directement chercher la valeur de l'entrée ici
        self.initImg('./cache/' + str(index)+'.png')

    def rotation(self):
        global index
        index = index +1
        rotate(self.filename,'./cache/' + str(index) +'.png',int(verifyNumber(entryRotation.get()))) #on viens directement chercher la valeur de l'entrée ici
        self.initImg('./cache/' + str(index)+'.png')
        

display = Displayed(visualization)

mainUI.mainloop() #on lance l'attente de commande et de L'UI