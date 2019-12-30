from tkinter import *
from PIL import Image
from PIL import ImageTk
import os
import cv2


def label_liso():
    global liso, amostras
    amostras.remove(amostras[0])
    # Sample file name
    nome_lima = amostras[0]
    # creating the first sample path
    path_Lima = path_train + "/" + nome_lima
    image_Lima = cv2.imread(path_Lima)
    # OpenCV represents images in BGR order; however PIL represents images in RGB order, so we need to swap the channels
    image_Lima = cv2.cvtColor(image_Lima, cv2.COLOR_BGR2RGB)
    # convert the images to PIL format...
    image_Lima = Image.fromarray(image_Lima)
    # ...and then to ImageTk format
    image_Lima = ImageTk.PhotoImage(image_Lima)
    #Updating sample image
    panel_Lima.configure(image=image_Lima)
    panel_Lima.image = image_Lima
    liso = liso + 1
    print(liso)


def label_rugoso():
    global rugoso, amostras
    amostras.remove(amostras[0])
    nome_lima = amostras[0]
    # creating the first sample path
    path_Lima = path_train + "/" + nome_lima
    image_Lima = cv2.imread(path_Lima)
    # OpenCV represents images in BGR order; however PIL represents images in RGB order, so we need to swap the channels
    image_Lima = cv2.cvtColor(image_Lima, cv2.COLOR_BGR2RGB)
    # convert the images to PIL format...
    image_Lima = Image.fromarray(image_Lima)
    # ...and then to ImageTk format
    image_Lima = ImageTk.PhotoImage(image_Lima)
    # Updating sample image
    panel_Lima.configure(image=image_Lima)
    panel_Lima.image = image_Lima
    rugoso = rugoso + 1
    print(rugoso)

def window(main):
    main.title('LiMatch')
    main.update_idletasks()
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

def LoadImage(path):
    # load the image from disk
    image = cv2.imread(path)
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
path_train = "/home/ellen/Imagens/TRAIN1200-1200_SEMLABEL"

'''Construcao GUI'''
#Creating the GUI interface
root = Tk()
#Defining resolution for my program  based in screen resolution
window(root)
#Setting new global  panels to store  images
global panel_ModeloLiso, panel_ModeloRugoso, panel_Lima
global amostras,index_lima,nome_lima
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
        image_Liso= LoadImage(path_ModeloLiso)
        '''Model image - Rugoso'''
        # load the image from disk
        image_Rugoso= LoadImage(path_ModeloRugoso)

        '''Model image - Lima'''
        # load the image from disk
        image_Lima = LoadImage(path_ModeloLima)

        # if the panels are None, initialize them
        if panel_ModeloLiso is None or panel_ModeloRugoso is None or panel_Lima is None:
            #Storing image
                panel_ModeloLiso = Label(image=image_Liso)
                panel_ModeloLiso.image = image_Liso
                panel_ModeloLiso.pack(padx=10, pady=10)
                panel_ModeloLiso.place(anchor=NW)


            #Storing image
                panel_ModeloRugoso = Label(image=image_Rugoso)
                panel_ModeloRugoso.image = image_Rugoso
                panel_ModeloRugoso.pack(padx=10, pady=10)
                panel_ModeloRugoso.place(anchor=NE)

            # Storing image
                panel_Lima = Label(image=image_Lima)
                panel_Lima.image = image_Lima
                panel_Lima.pack(padx=10, pady=10)
                panel_ModeloRugoso.place(anchor=CENTER)
        # otherwise, update the image panels
        else:
         # update the pannels
                  panel_ModeloLiso.configure(image=image_Liso)
                  panel_ModeloLiso.image = image_Liso

                  panel_ModeloRugoso.configure(image=image_Rugoso)
                  panel_ModeloRugoso.image = image_Rugoso



else:
    print('Caminho das imagens modelo nao encontrado')
btn_Liso = Button(root, text="LISO", command=label_liso)
btn_Liso.pack(side="bottom", fill="none", expand=False, padx="20", pady="20")
btn_Liso.place(x=250,y=500)
btn_Rugoso = Button(root, text="RUGOSO", command=label_rugoso)
btn_Rugoso.pack(side="bottom", fill="none", expand=False, padx="20", pady="20")
btn_Liso.place(x=500,y=500)
# kick off the GUI
root.mainloop()

