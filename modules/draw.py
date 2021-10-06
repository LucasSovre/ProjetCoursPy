from tkinter import *

app  = Tk()
app.geometry("1080x720")

def get_x_and_y(event):
    global lasx, lasy
    lasx, lasy = event.x,event.y

def draw(event):
    global lasx, lasy
    canvas.create_line((lasx, lasy, event.x, event.y), fill='red', width="2")
    lasx, lasy = event.x, event.y

def draw_r(event):
    global lasx, lasy
    canvas.create_rectangle((lasx, lasy, event.x, event.y), fill='red', width="2")
    lasx, lasy = event.x, event.y
    
def draw_o(event):
    global lasx, lasy
    canvas.create_oval((lasx, lasy, event.x, event.y), fill='red', width="2")
    lasx, lasy = event.x, event.y

canvas = Canvas(app,bg='white')
canvas.pack(fill='both',expand=1 )

# Recupere la position de x1,y1 et x2,y2 a chaque clique gauche de la souris
canvas.bind("<Button-1>",get_x_and_y)
# Dessine sur le canvas entre la position de depart(clique gauche maintenu) et de l'arrivé (clique gauche relaché)
canvas.bind("<B1-Motion>", draw)



app.mainloop()
