#tout les imports sont ci dessous :
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from tkinter import filedialog

from os import remove
from shutil import copyfile
import glob 
import json
from PIL import Image

from modules.importation import *
from modules.b_and_w import *
from modules.redimensionner import sizeFunction
from modules.rotation import *
from modules.preset import Preset

#////////////////////////       Préparation du logiciel         ///////////////////////////////////

mainUI = Tk()               #on instentie la fenetre principale du programme
mainUI.title('main')        #renomme la fenetre principale
mainUI.geometry("1500x800") #on donne la taille de la fenêtre initiale 

index = 0                   #l'index servira a conaitre l'image dans le cache à afficher et à utiliser actuellement 
blackAndWhite = None        #voir fonction de sauvegarde preset   
PresetDict = {}             #dictionnaire dans lequel nous allons charger les presets

#on efface le cache de la session precedente
#le cache permet de sauvegarder temporairement les fichier afin de pouvoir faire un avant/aprés
files = glob.glob('./cache/*') #selectionne tout les fichiers dans le cache
for f in files : 
    os.remove(f)               #efface les fichiers 1 par 1

#///////////   Load presets data    /////////// 
def loadPresets():
    global PresetDict                               #utilisation de global pour avoir accés à la variable PresetDict
    jsonPresetFile = open('data/presets.json')      #ouverture de preset sous format json
    PresetDict = json.load(jsonPresetFile)          #on convertis json en dictionnaire
loadPresets()
def getPresetKey():                                 #on récupère les keys des presets pour les afficher dans le choix de presets
    global PresetDict
    list = []
    for key in PresetDict.keys():
        list.append(key)
    return list

def export ():                                      #fonction pour sauvegarder l'image
    copyfile('cache/'+str(index)+".png", filedialog.asksaveasfile(mode='w', defaultextension=".png").name)


#//////////////////////    Definition des widgets de la fenêtre   ////////////////////////////////

menuBar = Menu(mainUI) #création du menu principal
mainUI.config(menu=menuBar) #on defini le menu
subMenuFile = Menu(menuBar) #on défini le sous menu 
subMenuHelp = Menu(menuBar)
menuBar.add_cascade(label='Fichier', menu=subMenuFile)
subMenuFile.add_command(label='Importer', command=lambda : (display.initImg(select_files(str(index)))))
subMenuFile.add_command(label='Exporter', command= lambda : export())
menuBar.add_cascade(label='Aide', menu=subMenuHelp)

mainUI.columnconfigure(0)#configuration des colonnes et lignes de la fenêtre principale
mainUI.columnconfigure(1, weight="6")
mainUI.columnconfigure(2)
mainUI.rowconfigure(0, weight="1")
mainUI.rowconfigure(1 , weight="1")
mainUI.rowconfigure(2 , weight="1")
mainUI.rowconfigure(3 , weight="1")
mainUI.rowconfigure(4 , weight="1")
mainUI.rowconfigure(5 , weight="1")
mainUI.rowconfigure(6 , weight="1")
mainUI.rowconfigure(7 , weight="1")
mainUI.rowconfigure(8 , weight="1")
mainUI.rowconfigure(9 , weight="1")
mainUI.rowconfigure(10 , weight="1")
mainUI.rowconfigure(11, weight="1")
mainUI.rowconfigure(12 , weight="1")
mainUI.rowconfigure(13 , weight="1")
mainUI.rowconfigure(14 , weight="1")

toolbar = Frame(mainUI, background='#838383') #configuration de la barre d'outils
toolbar.grid(rowspan=2,row=0,column=0,sticky="nsew")
button1 = Button(toolbar, text="Black & White", command=lambda : (display.black_and_white()))
button1.grid(rowspan=1,padx=50,pady=20,row=2,column=0)

nextAndPrev = Frame(toolbar)  #création de l'UI pour "avant", "aprés" 
nextAndPrev.grid(rowspan=1,padx=50,pady=20,row=0,column=0)
buttonPrev = Button(nextAndPrev,text="<--", command=lambda :(display.previousImg()))
buttonNext = Button(nextAndPrev, text="-->", command=lambda: (display.nexImg()))
buttonPrev.grid(rowspan=1,row=0,column=0)
buttonNext.grid(rowspan=1,row=0,column=1)

contrast = Frame(toolbar) #crée un frame pour l'input en question
contrast.grid(rowspan=1,padx=50,pady=20,row=3,column=0)
button2 = Button(contrast, text='contrast',command=lambda : (display.contrast()))
button2.grid(rowspan=1,row=4,column=0)
entryContrast = Entry(contrast)
entryContrast.grid(rowspan=1,row=5,column=0)

sharpness = Frame(toolbar) #crée un frame pour l'input en question
sharpness.grid(rowspan=1,padx=50,pady=20,row=6,column=0)
button3 = Button(sharpness, text='duretée',command=lambda : (display.sharpness()))
button3.grid(rowspan=1,row=7,column=0)
entrySharpness = Entry(sharpness)
entrySharpness.grid(rowspan=1,row=8,column=0)

saturation = Frame(toolbar) #crée un frame pour l'input en question
saturation.grid(rowspan=1,padx=50,pady=20,row=9,column=0)
button4 = Button(saturation, text='saturation',command=lambda : (display.saturation()))
button4.grid(rowspan=1,row=10,column=0)
entrySaturation = Entry(saturation)
entrySaturation.grid(rowspan=1,row=11,column=0)

redimensionner = Frame(toolbar) #crée un frame pour l'input en question
redimensionner.grid(rowspan=1,padx=50,pady=20,row=12,column=0)
button5 = Button(redimensionner, text='redimmensionner',command=lambda : (display.redimension()))
button5.grid(rowspan=1,row=3,column=0)
entryRedimensionX = Entry(redimensionner)
entryRedimensionX.grid(rowspan=1,row=13,column=0)
entryRedimensionY = Entry(redimensionner)
entryRedimensionY.grid(rowspan=1,row=14,column=0)

rotation = Frame(toolbar) #crée un frame pour l'input en question
rotation.grid(rowspan=1,padx=50,pady=20,row=15,column=0)
button6 = Button(rotation, text='Rotation',command=lambda : (display.rotation()))
button6.grid(rowspan=1,row=16,column=0)
entryRotation = Entry(rotation)
entryRotation.grid(rowspan=1,row=17,column=0)

visualization = Frame(mainUI, background="#404040") #configuration du frame de canvas principal
visualization.grid(rowspan=1,row=0,column=1)

presetPanel = Frame(mainUI, background="#838383")#configuration du Frame controlPanel
presetPanel.grid(rowspan=1,row=0,column=2,ipady=500,sticky="nsew")

savePresetButton = Button(presetPanel, text="Sauvegarder ce preset", command=lambda : (savePreset()))
entryPresetName = Entry(presetPanel)
savePresetButton.grid(rowspan=1,padx=50,pady=2,row=2,column=2,sticky="nsew")
entryPresetName.grid(rowspan=1,padx=50,pady=10,row=1,column=2,sticky="nsew")


presetList = ttk.Combobox(presetPanel, values=getPresetKey())
presetList.grid(rowspan=1,padx=50,pady=30,row=3,column=2,sticky="nsew")


browseFolderButton = Button(presetPanel, text="apply to a folder", command=lambda : (applyPresetToFolder()))
browseFolderButton.grid(rowspan=1,padx=50,pady=2,row=4,column=2)

#////////////////////// Definition des fonctions personalisées ///////////////////////////

def verifyNumber(entry): #cette fonction verifie que son entrées est un nombre
    if entry.isdigit():
        return entry
    else :               #si non affiche une erreur
        messagebox.showerror("Erreur","L'entrée est incorecte, veuillez entrer un nombre entier svp")

def savePreset():       #Permet de sauvegarder les modifs actuelles comme un preset
    temporaryDict ={                                                                   #récupère les réglages de modification
        "contrast" : entryContrast.get(),
        "sharpness" : entrySharpness.get(),
        "saturation" : entrySaturation.get(),
        "dimensions" : [entryRedimensionX.get(),entryRedimensionY.get()],
        "rotation" : entryRotation.get()
    }   
    if blackAndWhite != None:                                                           #comme black&white est un bouton on ne peut pas récuperer sa valeur, on utilise l'index de l'image à laquelle le b&w à été utilisé
        if blackAndWhite <= index:                                                      #en, vérifiant si b&w est inferieur ou égal à l'index actuel, on peut prendre en compte des retours en arrière de l'utilisateur
            temporaryDict["blackAndWhite"] = True
        else :
            temporaryDict["blackAndWhite"] = False
    else :
        temporaryDict["blackAndWhite"] = False
    if entryPresetName.get() not in PresetDict and entryPresetName.get() != "" :        #on verifie si le nom existe deja dans les presets
        i=0
        for key in temporaryDict.keys():
            if key == "rotation" :                                                      
                if temporaryDict[key] == "":                                            #si une valeur entrée est nulle:
                 temporaryDict[key] = 0                                                 #si c'est rotation on lui affecte 0 car on veut pas tourner l'image
            else:
                if temporaryDict[key] == "":                                            
                    temporaryDict[key] = 1                                              #sinon on lui affecte 1, (les mofifications sont multiplicatives, ainsi 1, ne changera pas l'aspect final)
        PresetDict[entryPresetName.get()] = json.dumps(temporaryDict)
    else :
        messagebox.showerror("Erreur","Un preset avec ce nom existe déja")              #si un preset de ce nom existe déja on affiche une érreur
    with open('data/presets.json', 'w',encoding='utf-8') as outfile:                    #on écrit le nouveau preset dans le fichier
        json.dump(PresetDict, outfile)
    entryPresetName.delete(0,END)                                                       #on reset l'entrée de nom du preset
    loadPresets()                                                                       #on re-charge les presets 
    presetList = ttk.Combobox(presetPanel, values=getPresetKey())                       #une reconfiguration du widget permet de mettre à jour sa liste en prenant en compte le nouveau preset
    presetList.grid(rowspan=1,padx=50,pady=30,row=3,column=2,sticky="nsew")

def applyPresetToFolder ():                                                             #fonction pour appliquer un preset à tout un dossier
    folder = filedialog.askdirectory()                                                  #on demande le dossier contenant les images à modifier
    files = glob.glob(folder+"/*.png")                                                  #permet de selectioner toutes les images png
    selectedPreset = json.loads(PresetDict[presetList.get()])                           #on charge le preset selcetionné dans la liste déroulante
    #on crée un objet de la classe preset
    preset = Preset(selectedPreset["blackAndWhite"],selectedPreset["contrast"],selectedPreset["sharpness"],selectedPreset["saturation"],selectedPreset["dimensions"],selectedPreset["rotation"])
    for file in files :                                                                 #on applique le preset à tout les fichiers png selectionnés plus tot
        preset.apply(file)
        


#//////////////////////    Definition de la classe principal permettant l'affichage //////////////////

class Displayed : 
    def __init__(self,parentFrame) :                                #constructeur de la classe
        self.parentFrame = parentFrame
        self.canvas = Canvas(self.parentFrame,width=0,height=0)     #on initie le canva en 0x0 pour ne pas être vue par l'utilisateur 
        self.canvas.pack()

    def initImg(self,filename):                                     #initiation de l'image
        global index
        self.filename = filename
        self.image = PhotoImage(file=filename)
        pic = Image.open(filename)
        X,Y = pic.size                                              #on récupère ses dimensions
        self.canvas.config(width=X,height=Y)
        self.canvas.create_image(X/2,Y/2,image=self.image)          #on affiche notre image sur le canvas
        self.canvas.update()                                        #on update le canvas

    def previousImg(self):
        global index
        index = index - 1                                           #on recule l'index de 1
        try :
            self.filename = './cache/' + str(index)+'.png'
            self.initImg('./cache/' + str(index)+'.png')
        except TclError:                                            #permet de gerer l'erreur d'un utilisateur qui reviendrais trop en arrière (i<0)
            index = index + 1

    def nexImg(self):                                               #raisonement analogue à previousIMG mais pour la suivante
        global index
        index = index + 1
        try :
            self.filename = './cache/' + str(index)+'.png'
            self.initImg('./cache/' + str(index)+'.png')
        except TclError:
            index = index - 1
    
    def black_and_white(self):                                      #appel la fonction de modification Black&White
        global index
        global blackAndWhite
        index = index +1
        blackAndWhite = index
        black_and_white(self.filename,'./cache/' + str(index) +'.png')
        self.initImg('./cache/' + str(index)+'.png')

    def contrast(self):                                              #appel la fonction de modification contrast
        global index
        index = index +1
        contrastFunction(self.filename,'./cache/' + str(index) +'.png',int(verifyNumber(entryContrast.get()))) #on viens directement chercher la valeur de l'entrée ici
        self.initImg('./cache/' + str(index)+'.png')

    def sharpness(self):                                              #appel la fonction de modification sharpness (duretée)
        global index
        index = index +1
        sharpnessFunction(self.filename,'./cache/' + str(index) +'.png',int(verifyNumber(entrySharpness.get()))) #on viens directement chercher la valeur de l'entrée ici
        self.initImg('./cache/' + str(index)+'.png')

    def saturation(self):                                              #appel la fonction de modification saturation
        global index
        index = index +1
        saturationFunction(self.filename,'./cache/' + str(index) +'.png',int(verifyNumber(entrySaturation.get()))) #on viens directement chercher la valeur de l'entrée ici
        self.initImg('./cache/' + str(index)+'.png')

    def redimension(self):                                             #appel la fonction de modification redimensionnement
        global index
        index = index +1
        sizeFunction(self.filename,'./cache/' + str(index) +'.png',int(verifyNumber(entryRedimensionX.get())),int(verifyNumber(entryRedimensionY.get()))) #on viens directement chercher la valeur de l'entrée ici
        self.initImg('./cache/' + str(index)+'.png')

    def rotation(self):                                                #appel la fonction de modification rotation
        global index
        index = index +1
        rotate(self.filename,'./cache/' + str(index) +'.png',int(verifyNumber(entryRotation.get()))) #on viens directement chercher la valeur de l'entrée ici
        self.initImg('./cache/' + str(index)+'.png')
        
#///////////////// on instentie la classe permettant l'affichage du canvas /////////////////////////////

display = Displayed(visualization) #on instensie le canvas

mainUI.mainloop() #on lance l'attente de commande et de L'UI
