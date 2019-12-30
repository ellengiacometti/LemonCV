from tkinter import *
from PIL import Image
from PIL import ImageTk
import os
import cv2

def label_liso():
    global liso
    liso = liso +1
    print(liso)
    #todo update panel_Lima picture
def label_rugoso():
    global rugoso
    rugoso = rugoso +1
    print(rugoso)
    #todo update panel_Lima picture


'''Inicializacao de variaveis'''
#Creating the GUI interface
root = Tk()

#Setting new global  panels to store  images
global panel_ModeloLiso, panel_ModeloRugoso, panel_Lima,amostras
panel_ModeloLiso = None
panel_ModeloRugoso = None
panel_Lima =  None

'''Path dos modelos'''
path_ModeloLiso = "/home/ellen/Imagens/Modelos/lemonMaduro.jpg"
path_ModeloRugoso = "/home/ellen/Imagens/Modelos/lemonVerde.jpg"
path_ModeloLima = "/home/ellen/Imagens/Modelos/blank.png"

''' Path das Limas '''
path_train = "/home/ellen/Imagens/TRAIN1200-1200_SEMLABEL"
amostras = os.listdir(path_train)
#
liso=0
rugoso=0
if len(path_ModeloLiso ) > 0 and len(path_ModeloRugoso)>0:
        '''Model image - Liso'''
        # load the image from disk
        image_Liso = cv2.imread(path_ModeloLiso)
        # OpenCV represents images in BGR order; however PIL represents images in RGB order, so we need to swap the channels
        image_Liso = cv2.cvtColor(image_Liso, cv2.COLOR_BGR2RGB)
        # convert the images to PIL format...
        image_Liso = Image.fromarray(image_Liso)
        # ...and then to ImageTk format
        image_Liso = ImageTk.PhotoImage(image_Liso)
        # if the panels are None, initialize them

        '''Model image - Rugoso'''
        # load the image from disk
        image_Rugoso= cv2.imread(path_ModeloRugoso)
        # OpenCV represents images in BGR order; however PIL represents images in RGB order, so we need to swap the channels
        image_Rugoso = cv2.cvtColor(image_Rugoso, cv2.COLOR_BGR2RGB)
        # convert the images to PIL format...
        image_Rugoso = Image.fromarray(image_Rugoso)
        # ...and then to ImageTk format
        image_Rugoso = ImageTk.PhotoImage(image_Rugoso)

        '''Model image - Lima'''
        # load the image from disk
        image_Lima = cv2.imread(path_ModeloLima)
        # OpenCV represents images in BGR order; however PIL represents images in RGB order, so we need to swap the channels
        image_Lima = cv2.cvtColor(image_Lima, cv2.COLOR_BGR2RGB)
        # convert the images to PIL format...
        image_Lima = Image.fromarray(image_Lima)
        # ...and then to ImageTk format
        image_Lima = ImageTk.PhotoImage(image_Lima)
        # if the panels are None, initialize them
        # if the panels are None, initialize them
        if panel_ModeloLiso is None or panel_ModeloRugoso is None or panel_Lima is None:
            #Storing image
                 panel_ModeloLiso = Label(image=image_Liso)
                 panel_ModeloLiso.image = image_Liso
                 panel_ModeloLiso.pack(side="left", padx=10, pady=10)

            #Storing image
                 panel_ModeloRugoso = Label(image=image_Rugoso)
                 panel_ModeloRugoso.image = image_Rugoso
                 panel_ModeloRugoso.pack(side="right", padx=10, pady=10)

            # Storing image
                 panel_Lima = Label(image=image_Lima)
                 panel_Lima.image = image_Lima
                 panel_Lima.pack(side="bottom", padx=10, pady=10)

        # otherwise, update the image panels
        else:
         # update the pannels
                  panel_ModeloLiso.configure(image=panel_ModeloLiso)
                  panel_ModeloRugoso.configure(image=image_Rugoso)

                  panel_ModeloLiso.image = panel_ModeloLiso
                  panel_ModeloRugoso.image = image_Rugoso
else:
    print('Caminho das imagens modelo nao encontrado')
btn_Liso = Button(root, text="LISO", command=label_liso)
btn_Liso.pack(side="left", fill="both", expand="no", padx="20", pady="20")
btn_Rugoso = Button(root, text="RUGOSO", command=label_rugoso)
btn_Rugoso.pack(side="right", fill="both", expand="no", padx="20", pady="20")
# kick off the GUI
root.mainloop()

