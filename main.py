from tkinter import *
from PIL import Image
from modules.importation import *
from modules.b_and_w import *

mainUI = Tk() #on instentie la fenetre principale du programme
mainUI.title('main') #renomme la fenetre principale
mainUI.geometry("1500x800")

index = 0

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

visualization = Frame(mainUI, background="blue") #configuration du frame de canvas principal
visualization.grid(rowspan=2,row=0,column=1,sticky="nsew")

controlPanel = Frame(mainUI, background="yellow")#configuration du Frame controlPanel
controlPanel.grid(rowspan=2,row=0,column=2,sticky="nsew")

class Displayed : 
    def __init__(self,parentFrame) :
        self.parentFrame = parentFrame
        self.canvas = Canvas(self.parentFrame,width=0,height=0)
        self.canvas.pack()

    def initImg(self,filename):
        global index
        self.filename = filename
        self.image = PhotoImage(file=filename)
        pic = Image.open(filename)
        X,Y = pic.size
        self.canvas.config(width=X,height=Y)
        self.canvas.create_image(X/2,Y/2,image=self.image) #on affiche notre image sur le canvas
        self.canvas.update() #on update le canvas
        index = index + 1
    
    def black_and_white(self):
        global index
        black_and_white(self.filename,'./cache/' + str(index) +'.png')
        self.initImg('./cache/' + str(index)+'.png')

display = Displayed(visualization)

mainUI.mainloop() #on lance l'attente de commande et de L'UI