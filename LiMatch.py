from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter.font as font
from PIL import Image
from PIL import ImageTk
import pandas as pd
import os
import cv2
from datetime import datetime
def label_X():
    global amostras,Sample,Rotulo,label,classified
    Sample.append(amostras[0])
    Rotulo.append('X')
    if len(amostras) >1 :
        amostras.remove(amostras[0])
        # Sample file name
        nome_lima = amostras[0]
        # creating the first sample path
        path_Lima = path_train + "/" + nome_lima
        image_Lima = LoadImage(path_Lima,(300,300))
        #Updating sample image
        panel_Lima.configure(image=image_Lima)
        panel_Lima.image = image_Lima
        # Updating lima legend
        lima.set(nome_lima)
    else:
        messagebox.showinfo("Diretorio Vazio", "Todas as imagens foram classificadas :)")
        SaveLabeledFile()

def label_LS():
    global amostras,Sample,Rotulo,label
    Sample.append(amostras[0])
    Rotulo.append('LS')
    if len(amostras) >1 :
        amostras.remove(amostras[0])
        # Sample file name
        nome_lima = amostras[0]
        # creating the first sample path
        path_Lima = path_train + "/" + nome_lima
        image_Lima = LoadImage(path_Lima,(300,300))
        #Updating sample image
        panel_Lima.configure(image=image_Lima)
        panel_Lima.image = image_Lima
        # Updating lima legend
        lima.set(nome_lima)
    else:
        messagebox.showinfo("Diretorio Vazio", "Todas as imagens foram classificadas :)")
        SaveLabeledFile()



def label_LC():
    global amostras,Sample,Rotulo,label
    Sample.append(amostras[0])
    Rotulo.append('LC')

    if len(amostras) >1 :
        amostras.remove(amostras[0])
        # Sample file name
        nome_lima = amostras[0]
        # creating the first sample path
        path_Lima = path_train + "/" + nome_lima
        image_Lima = LoadImage(path_Lima,(300,300))
        #Updating sample image
        panel_Lima.configure(image=image_Lima)
        panel_Lima.image = image_Lima
        # Updating lima legend
        lima.set(nome_lima)
    else:
        messagebox.showinfo("Diretorio Vazio", "Todas as imagens foram classificadas :)")
        SaveLabeledFile()

def label_RS():
    global amostras,Sample,Rotulo,label
    Sample.append(amostras[0])
    Rotulo.append('RS')
    if len(amostras) >1 :
        amostras.remove(amostras[0])
        # Sample file name
        nome_lima = amostras[0]
        # creating the first sample path
        path_Lima = path_train + "/" + nome_lima
        image_Lima = LoadImage(path_Lima,(300,300))
        #Updating sample image
        panel_Lima.configure(image=image_Lima)
        panel_Lima.image = image_Lima
        # Updating lima legend
        lima.set(nome_lima)
    else:
        messagebox.showinfo("Diretorio Vazio", "Todas as imagens foram classificadas :)")
        SaveLabeledFile()

def label_RC():
    global  amostras,Sample,Rotulo,label
    Sample.append(amostras[0])
    Rotulo.append('RC')
    if len(amostras) >1 :
        amostras.remove(amostras[0])
        # Sample file name
        nome_lima = amostras[0]
        # creating the first sample path
        path_Lima = path_train + "/" + nome_lima
        image_Lima = LoadImage(path_Lima,(300,300))
        #Updating sample image
        panel_Lima.configure(image=image_Lima)
        panel_Lima.image = image_Lima
        # Updating lima legend
        lima.set(nome_lima)
    else:
        messagebox.showinfo("Diretorio Vazio", "Todas as imagens foram classificadas :)")
        SaveLabeledFile()



def on_closing():
    global arquivo_salvo
    if arquivo_salvo==1:
            root.destroy()
    else:
        if messagebox.askokcancel("Sair", "Tem certeza que deseja SAIR SEM SALVAR?"):
            root.destroy()





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

def CreatePanel(root,image,panel_x,panel_y,texto,legend_x,legend_y,action):
    # Storing image
    if action=="LS":
         panel_default = Button(image=image, borderwidth=2, relief="solid",command=label_LS)
    elif action=="LC":
        panel_default = Button(image=image, borderwidth=2, relief="solid", command=label_LC)
    elif action=="RS":
         panel_default = Button(image=image, borderwidth=2, relief="solid",command=label_RS)
    elif action=="RC":
        panel_default = Button(image=image, borderwidth=2, relief="solid", command=label_RC)
    elif action=="X":
        panel_default = Button(image=image, borderwidth=2, relief="solid", command=label_X)

    panel_default.image = image
    # Setting legend
    legenda = StringVar()
    legenda.set(texto)
    legend_panel_default = Label(root, textvariable=legenda, font=('Helvetica', '14'))
    return panel_default,legend_panel_default

def LoadPreviousLabeledFile():
    global nome_lima,amostras,path_train
    filename = filedialog.askopenfilename( title = "Selecione o arquivo com a rotulacao",filetypes = (("CSV Files","*.csv"),))
    try:
        labeled_list= pd.read_csv(filename,sep=";")
        classified_SAMPLE=labeled_list["Sample"]
        classified_ROTULO=labeled_list["Rotulo"]

        if amostras is not None:
            amostras= list(set(amostras).difference(set(classified_SAMPLE.values)))
            for sample in classified_SAMPLE.values:
                Sample.append(sample)
            for rotulo in classified_ROTULO.values:
                Rotulo.append(rotulo)
            nome_lima = amostras[0]
            path_Lima = path_train + "/" + nome_lima
            image_Lima = LoadImage(path_Lima, (300, 300))
            # Updating sample image
            panel_Lima.configure(image=image_Lima)
            panel_Lima.image = image_Lima
            # Updating lima legend
            lima.set(nome_lima)
    except:
       messagebox.showerror(title='Erro ao carregar', message='Nao foi possivel carregar arquivo')
    print("Diretorio carregado:",filename)
def SaveLabeledFile():
    global arquivo_salvo
    raw_data = {'Sample': Sample, 'Rotulo': Rotulo}
    df = pd.DataFrame(raw_data, columns=['Sample', 'Rotulo'])
    filename = filedialog.asksaveasfilename( defaultextension='.csv')
    try:
        df.to_csv(filename, index=False, sep=";")
        arquivo_salvo=1;
        print(filename, '--> Criado com sucesso!')
    except:
       messagebox.showerror(title='Erro ao salvar', message='Nao foi possivel salvar')



'''Path dos modelos'''
ROOT_DIR = os.path.abspath(os.curdir)
path_ModeloLiso = os.path.join(ROOT_DIR,"Modelos/Modelo_LS.jpg")
path_ModeloRugoso =os.path.join(ROOT_DIR, "Modelos/Modelo_RS.jpg")
path_ModeloLisoDefeito =os.path.join(ROOT_DIR, "Modelos/Modelo_LC.jpg")
path_ModeloRugosoDefeito =os.path.join(ROOT_DIR, "Modelos/Modelo_RC.jpg")
path_X=os.path.join(ROOT_DIR, "Modelos/X.png")

''' Path das Limas '''
path_train = os.path.join(ROOT_DIR, "SEMLABEL")

'''Construcao GUI'''
#Creating the GUI interface
root = Tk()
#Creating a menubar to display an option to load previous labeled
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Carregar arquivo...", command=LoadPreviousLabeledFile)
filemenu.add_command(label="Salvar arquivo...", command=SaveLabeledFile)
filemenu.add_separator()
filemenu.add_command(label="Sair", command=on_closing)
menubar.add_cascade(label="Menu", menu=filemenu)

root.config(menu=menubar)
#Defining resolution for my program  based in screen resolution
root.title('LiMatch')
root.minsize()
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)

#Setting new global  panels to store  images
global panel_ModeloLiso, panel_ModeloRugoso, panel_ModeloLisoDefeito, panel_ModeloRugosoDefeito,panel_Lima
global amostras,index_lima,nome_lima,Rotulo,Sample,arquivo_salvo,classified

Rotulo=[]
Sample=[]
panel_ModeloLiso = None
panel_ModeloRugoso = None
panel_ModeloLisoDefeito = None
panel_ModeloRugosoDefeito = None
panel_Lima =  None
arquivo_salvo=0
classified= None
model_size=(300,250)
lima_size=(500,470)
'''Preenchendo o panel de amostras'''
# List with all samples names
amostras = os.listdir(path_train)
#Sample file name
nome_lima = amostras[0]
# creating the first sample path
path_ModeloLima = path_train + "/" + nome_lima

if len(path_ModeloLiso ) > 0 and len(path_ModeloRugoso)>0:
        '''Model image - Liso'''
        image_Liso= LoadImage(path_ModeloLiso,model_size)
        '''Model image - Rugoso'''
        # load the image from disk
        image_Rugoso= LoadImage(path_ModeloRugoso,model_size)
        '''Model image - Liso Defeito'''
        image_LisoDefeito = LoadImage(path_ModeloLisoDefeito, model_size)
        '''Model image - Rugoso Defeito'''
        # load the image from disk
        image_RugosoDefeito = LoadImage(path_ModeloRugosoDefeito, model_size)
        '''Model image - Lima'''
        # load the image from disk
        image_Lima = LoadImage(path_ModeloLima,lima_size)
        '''Model image -  Drop'''
        image_X = LoadImage(path_X, (80, 80))

        btLS,legLS=CreatePanel(root, image_Liso, 150, 50, 'LISO - SEM DEFEITO', 255, 40,action="LS")
        btRS,legRS=CreatePanel(root, image_Rugoso, 1250, 50, 'RUGOSO - SEM DEFEITO', 1350, 40,action="RS")
        btLC,legLC=CreatePanel(root,image_LisoDefeito,150,550,'LISO - COM DEFEITO',255,540,action="LC")
        btRC,legRC=CreatePanel(root, image_RugosoDefeito, 1250, 550, 'RUGOSO - COM DEFEITO', 1350, 540,action="RC")
        btX,legX=CreatePanel(root, image_X, 850, 825, 'INADEQUADO', 840, 935, action="X")
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
        # Inserting GRID
        # legLS.grid(row=0,column=0,padx=2,pady=10)
        # legRS.grid(row=0,column=2,padx=2,pady=10)
        # btLS.grid(row=1,column=0,padx=2,pady=2)
        # btRS.grid(row=1,column=2,padx=2,pady=2)
        # legend_Lima.grid(row=1, column=1, padx=2, pady=2,sticky=S)
        # panel_Lima.grid(row=2, column=1, padx=2, pady=2)
        # legLC.grid(row=3,column=0,padx=2,pady=10,sticky=S)
        # legRC.grid(row=3,column=2,padx=2,pady=10,sticky=S)
        # btLC.grid(row=5,column=0,padx=2,pady=2)
        # btRC.grid(row=5,column=2,padx=2,pady=2)
        # legX.grid(row=4, column=1, padx=2, pady=10,sticky=S)
        # btX.grid(row=5, column=1, padx=2, pady=10)
        legLS.grid(row=1, column=0)
        legRS.grid(row=1, column=2)
        btLS.grid(row=1, column=0,rowspan=2)
        btRS.grid(row=1, column=2,rowspan=2)
        legend_Lima.grid(row=1, column=1,sticky=S)
        panel_Lima.grid(row=2, column=1,rowspan=4,sticky=N)
        legLC.grid(row=5, column=0, sticky=N)
        legRC.grid(row=5, column=2,  sticky=N)
        btLC.grid(row=5, column=0,rowspan=4)
        btRC.grid(row=5, column=2,rowspan=4)
        btX.grid(row=5, column=1,sticky=S)
        try:
            root.state('zoomed')  # windows
        except:
            root.attributes('-zoomed', True)  # linux
else:
    print('Caminho das imagens modelo nao encontrado')
root.protocol("WM_DELETE_WINDOW", on_closing)
# kick off the GUI
root.mainloop()

