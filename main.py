from tkinter import *
from PIL import Image
from modules.importation import *

mainUI = Tk() #on instentie la fenetre principale du programme
mainUI.title('main') #renomme la fenetre principale
mainUI.geometry("1500x800")

menuBar = Menu(mainUI) #création du menu principal
mainUI.config(menu=menuBar) #on defini le menu
subMenuFile = Menu(menuBar) #on défini le sous menu 
subMenuHelp = Menu(menuBar)
menuBar.add_cascade(label='Fichier', menu=subMenuFile)
subMenuFile.add_command(label='Importer', command=lambda : (display.initImg(select_files())))
subMenuFile.add_command(label='Exporter')
menuBar.add_cascade(label='Aide', menu=subMenuHelp)

mainUI.columnconfigure(0, weight="1")#configuration des colonnes et lignes de la fenêtre principale
mainUI.columnconfigure(1, weight="6")
mainUI.columnconfigure(2, weight="3")
mainUI.rowconfigure(0, weight="1")
mainUI.rowconfigure(1 , weight="1")

toolbar = Frame(mainUI, background="green") #configuration de la barre d'outils
toolbar.grid(rowspan=2,row=0,column=0,sticky="nsew")

visualization = Frame(mainUI, background="blue") #configuration du frame de canvas principal
visualization.grid(rowspan=2,row=0,column=1,sticky="nsew")

controlPanel = Frame(mainUI, background="yellow")#configuration du Frame controlPanel
controlPanel.grid(rowspan=2,row=0,column=2,sticky="nsew")

class canvas : 
    def __init__(self,parentFrame) :
        self.parentFrame = parentFrame
        self.canvas = Canvas(self.parentFrame,width=0,height=0)
        self.canvas.pack()

    def initImg(self,filename):
        self.image = PhotoImage(file=filename)
        pic = Image.open(filename)
        X,Y = pic.size
        self.canvas.config(width=X,height=Y)
        self.canvas.create_image(X/2,Y/2,image=self.image) #on affiche notre image sur le canvas
        self.canvas.update() #on update le canvas

display = canvas(visualization)

mainUI.mainloop() #on lance l'attente de commande et de L'UI