from tkinter import *
from tkinter import messagebox
import tkinter.font as font
from PIL import Image
from PIL import ImageTk
import pandas as pd
import os
import cv2
from datetime import datetime


def label_liso():
    global liso, amostras,Sample,Rotulo
    Sample.append(amostras[0])
    Rotulo.append('L')
    liso = liso + 1
    if len(amostras) >1 :
        amostras.remove(amostras[0])
        # Sample file name
        nome_lima = amostras[0]
        # creating the first sample path
        path_Lima = path_train + "/" + nome_lima
        image_Lima = LoadImage(path_Lima,(600,600))
        #Updating sample image
        panel_Lima.configure(image=image_Lima)
        panel_Lima.image = image_Lima
        # Updating lima legend
        lima.set(nome_lima)
    else:
        messagebox.showinfo("Diretorio Vazio", "Todas as imagens foram classificadas :)")




def label_rugoso():
    global rugoso, amostras,Sample,Rotulo
    Sample.append(amostras[0])
    Rotulo.append('R')
    rugoso = rugoso + 1
    if len(amostras) >1 :
        amostras.remove(amostras[0])
        nome_lima = amostras[0]
        # creating the first sample path
        path_Lima = path_train + "/" + nome_lima
        image_Lima = LoadImage(path_Lima,(600,600))
        # Updating sample image
        panel_Lima.configure(image=image_Lima)
        panel_Lima.image = image_Lima
        #Updating lima legend
        lima.set(nome_lima)
    else:
        messagebox.showinfo("Diretorio Vazio", "Todas as imagens foram classificadas :)")



def on_closing():
    raw_data = {'Sample': Sample, 'Rotulo': Rotulo}
    df = pd.DataFrame(raw_data,columns=['Sample', 'Rotulo'])
    now = datetime.now()
    filename='Labeled_'+ now.strftime("%H:%M_%m%d%Y") +'.csv'
    df.to_csv(filename, index=False, sep=";")
    print(filename, '--> Criado com sucesso!')
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

def window(main):
    main.title('LiMatch')
    screenWidth=main.winfo_screenwidth()
    screenHeight=main.winfo_screenheight()

    if (screenWidth >= 1024) and (screenHeight >= 768):
        width = 1000
        height = 800
        x = (screenWidth // 2) - (width // 2)
        y = (screenHeight // 2) - (height // 2)
        main.geometry('{}x{}+{}+{}'.format(screenWidth,screenHeight,x,y))
    else:
        width = 800
        height = 600
        x = (screenWidth // 2) - (width // 2)
        y = (screenHeight // 2) - (height // 2)
        main.geometry('{}x{}+{}+{}'.format(screenWidth,screenHeight,x,y))

def LoadImage(path,dim):
    # load the image from disk
    image = cv2.imread(path)
    image = cv2.resize(image,dim)
     # OpenCV represents images in BGR order; however PIL represents images in RGB order, so we need to swap the channels
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # convert the images to PIL format...
    image = Image.fromarray(image)
    # ...and then to ImageTk format
    image = ImageTk.PhotoImage(image)
    return image

'''Path dos modelos'''
path_ModeloLiso = "/home/ellen/Imagens/Modelos/lemonMaduro.jpg"
path_ModeloRugoso = "/home/ellen/Imagens/Modelos/lemonVerde.jpg"

''' Path das Limas '''
# Test for end of sample's list
#path_train = "/home/ellen/Imagens/Modelos/"

path_train = "/home/ellen/Imagens/TRAIN1200-1200_SEMLABEL"

'''Construcao GUI'''
#Creating the GUI interface
root = Tk()
#Defining resolution for my program  based in screen resolution
window(root)
#Setting new global  panels to store  images
global panel_ModeloLiso, panel_ModeloRugoso, panel_Lima
global amostras,index_lima,nome_lima,Rotulo,Sample
Rotulo=[]
Sample=[]
panel_ModeloLiso = None
panel_ModeloRugoso = None
panel_Lima =  None

'''Inicializacao de variaveis'''
liso=0
rugoso=0


'''Preenchendo o panel de amostras'''
# List with all samples names
amostras = os.listdir(path_train)
#Sample file name
nome_lima = amostras[0]
# creating the first sample path
path_ModeloLima = path_train + "/" + nome_lima

if len(path_ModeloLiso ) > 0 and len(path_ModeloRugoso)>0:
        '''Model image - Liso'''
        image_Liso= LoadImage(path_ModeloLiso,(400,400))
        '''Model image - Rugoso'''
        # load the image from disk
        image_Rugoso= LoadImage(path_ModeloRugoso,(400,400))

        '''Model image - Lima'''
        # load the image from disk
        image_Lima = LoadImage(path_ModeloLima,(600,600))

        # if the panels are None, initialize them
        #Storing image
        panel_ModeloLiso = Label(image=image_Liso,borderwidth=2, relief="solid")
        panel_ModeloLiso.image = image_Liso
        panel_ModeloLiso.pack(padx=10, pady=10)
        panel_ModeloLiso.place(x=150,y=100)
        #Setting legend
        legend_ModeloLiso= Label(root, text="LISO",font=('Helvetica', '14'))
        legend_ModeloLiso.place(x=325,y=90)
        #Storing image
        panel_ModeloRugoso = Label(image=image_Rugoso,borderwidth=2, relief="solid")
        panel_ModeloRugoso.image = image_Rugoso
        panel_ModeloRugoso.pack(padx=10, pady=10)
        panel_ModeloRugoso.place(x=1250, y=100)
        #Setting legend
        legend_ModeloRugoso= Label(root, text="RUGOSO",font=('Helvetica', '14'))
        legend_ModeloRugoso.place(x=1400,y=90)
        # Storing image
        panel_Lima = Label(image=image_Lima,borderwidth=6, relief="solid")
        panel_Lima.image = image_Lima
        panel_Lima.pack(padx=10, pady=10)
        panel_Lima.place(x=600,y=200)
        # Setting legend
        lima=StringVar()
        lima.set(nome_lima)
        legend_Lima = Label(root, textvariable=lima, font=('Helvetica', '14'))
        legend_Lima.place(x=825, y=190)
        # otherwise, update the image panels
else:
    print('Caminho das imagens modelo nao encontrado')
myFont = font.Font(family='Helvetica',size=16,weight="bold")
btn_Liso = Button(root, text="LISO", command=label_liso,height = 5, width = 30)
btn_Liso['font']=myFont
btn_Liso.pack(side="bottom", fill="none", expand=TRUE, padx="20", pady="20")
btn_Liso.place(x=450,y=850)

btn_Rugoso = Button(root, text="RUGOSO", command=label_rugoso,height = 5, width = 30)
btn_Rugoso['font']=myFont
btn_Rugoso.pack(side="bottom", fill="none", expand=TRUE, padx="20", pady="20")
btn_Rugoso.place(x=900,y=850)

root.protocol("WM_DELETE_WINDOW", on_closing)
# kick off the GUI
root.mainloop()




