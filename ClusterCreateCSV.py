"""Author: Ellen Giacometti
    CRIADO EM: 21/12/2018
    ÚLTIMA ATUALIZAÇÃO: 05/02/2019
    DESC: Código tendo as features cria um arquivo csv com as features e as respectivas labels"""
import os
import glob
import pandas as pd
from TrataImagem import TrataImagem

""" Lendo Diretório """
liso_path = "/home/ellen/Imagens/CLUSTERIZAÇÃO/LISO"
rugoso_path = "/home/ellen/Imagens/CLUSTERIZAÇÃO/RUGOSO"
dir=[liso_path, rugoso_path]


""" Extraindo Features de cada imagem """
print("[STATUS] Started extracting  TRAIN features")
valueType = 0
for type_dir in dir:
    """ Definindo Variáveis """
    i=1
    raio = []
    Kurtosis = []
    Skewness = []
    Dissimilarity = []
    Correlation = []
    Homogeneity = []
    Energy = []
    Contrast = []
    ASM = []
    colorH = []
    for name in os.listdir(type_dir):

        cur_path = type_dir + "/" + name
        cur_label = name
        for file in glob.glob(cur_path):
            print("Processing Image - {} in {}".format(i, cur_label))
            features = TrataImagem(file,0,0)
            # append the feature vector and label
            Kurtosis.append(features[6])
            Skewness.append(features[7])
            Dissimilarity.append(features[8])
            Correlation.append(features[9])
            Homogeneity.append(features[10])
            Energy.append(features[11])
            Contrast.append(features[12])
            ASM .append(features[13])
            colorH.append(features[3])
            # colorS.append(features[4])
            # colorV.append(features[5])
            i+=1

    # raw_data = {'Object':os.listdir(type_dir),'Kurtosis': Kurtosis,'Skewness':Skewness,'Dissimilarity':Dissimilarity,'Correlation':Correlation,'Homogeneity':Homogeneity,'Energy':Energy,'Contrast':Contrast, 'ASM':ASM,'ColorH': colorH,'ColorS': colorS,'ColorV': colorV,'TextureLabel':  texture_label,'ColorLabel': color_label,'Raio':raio}
    raw_data = {'Object': os.listdir(type_dir), 'Kurtosis': Kurtosis, 'Skewness': Skewness,
                'Dissimilarity': Dissimilarity, 'Correlation': Correlation, 'Homogeneity': Homogeneity,
                'Energy': Energy, 'Contrast': Contrast, 'ASM': ASM, 'Color': colorH}
    # df = pd.DataFrame(raw_data, columns = ['Object','Kurtosis','Skewness','Dissimilarity','Correlation','Homogeneity','Energy','Contrast', 'ASM', 'ColorH','ColorS','ColorV','TextureLabel','ColorLabel','Raio'])
    df = pd.DataFrame(raw_data,
                      columns=['Object', 'Kurtosis', 'Skewness', 'Dissimilarity', 'Correlation', 'Homogeneity',
                               'Energy', 'Contrast', 'ASM', 'Color'])
    valueType += 1
    if valueType==1:
        df.to_csv('LISO.csv',index=False,sep=";")
        print("LISO.csv CRIADO")
    else:
        df.to_csv('RUGOSO.csv', index=False, sep=";")
        print("RUGOSO.csv CRIADO")
# """Fit The Label Encoder"""
# # Create a label (category) encoder object
# le = preprocessing.LabelEncoder()
# # Fit the encoder to the pandas column
# le.fit(df['LABELS'])
# # View the labels (if you want)
# list(le.classes_)
#
# """Transform Categories Into Integers"""
# # Apply the fitted encoder to the pandas column
# le.transform(df['LABELS'])
#
# """Transform Integers Into Categories"""
# # Convert some integers into their category names
# list(le.inverse_transform([0, 1, 1]))


