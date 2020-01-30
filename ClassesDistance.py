import numpy as np # linear algebra
import pandas as pd
from scipy.spatial import distance

def DistanciaIntraClasseMedia(features_classe,numero_amostra_classe):
    soma_geral=0
    vetor_distancias=[]
    #matriz_dist = np.zeros((numero_amostra_classe,numero_amostra_classe))
    i=1
    j=1
    for features_lima_A in features_classe:
        for features_lima_B in features_classe:
            # matriz_dist[i-1][j-1] = distance.euclidean(features_lima_A, features_lima_B)
            soma_geral=distance.euclidean(features_lima_A, features_lima_B) + soma_geral
            vetor_distancias.append(distance.euclidean(features_lima_A, features_lima_B))
            #print("Indice","linha",(i-1),"coluna",j-1,"-",matriz_dist[i-1][j-1])
            j=1+j
        i=i+1
        j=1
    media_intra= soma_geral/(numero_amostra_classe*numero_amostra_classe)
    variancia = np.var(vetor_distancias)
    media = np.mean(vetor_distancias)
    print('Variancia',variancia)
    print('Media', media)
    return media_intra

def CentroideClasse(features_classe,numero_amostra_classe):
    centroide2=np.average(features_classe,axis=0)
    soma_features = [sum(feature) for feature in zip(*features_classe)]
    centroide = [feature / numero_amostra_classe for feature in soma_features]
    print ('centroide calculado',centroide)
    print('centroide average',centroide2)
    return centroide

if __name__ == '__main__':
    teste = lambda x: x.strip("[]").replace("'", "").split(", ")
    LISO_FILE = pd.read_csv('LISO.csv', index_col=False, sep=";",
                        converters={'Color': teste, 'ColorS': teste, 'ColorV': teste})
    ColorTrainH = [list(map(float, histH)) for histH in LISO_FILE['Color']]
    ColorTrainH = np.array(ColorTrainH)
    colunasTrain = LISO_FILE.columns[1:9]
    TextureTrain_LISO = LISO_FILE[colunasTrain].values

    RUGOSO_FILE = pd.read_csv('RUGOSO.csv', index_col=False, sep=";",
                        converters={'Color': teste, 'ColorS': teste, 'ColorV': teste})
    ColorTrainH = [list(map(float, histH)) for histH in RUGOSO_FILE['Color']]
    ColorTrainH = np.array(ColorTrainH)
    colunasTrain = RUGOSO_FILE.columns[1:9]
    TextureTrain_RUGOSO = RUGOSO_FILE[colunasTrain].values



    features_classe_lisa=TextureTrain_LISO
    features_classe_rugosa=TextureTrain_RUGOSO

    numero_amostra_classe_lisa=len(features_classe_lisa)
    numero_amostra_classe_rugosa = len(features_classe_lisa)
    print('%LISO%')
    Lisa = DistanciaIntraClasseMedia(features_classe_lisa,numero_amostra_classe_lisa)
    print('Distancia Intra Classe Media --LISO ', Lisa)
    Centroide_Lisa = CentroideClasse(features_classe_lisa, numero_amostra_classe_lisa)
    print('Centroide_Lisa', Centroide_Lisa)
    print('%RUGOSO%')
    Rugosa=DistanciaIntraClasseMedia(features_classe_rugosa,numero_amostra_classe_rugosa)
    print('Distancia Intra Classe Media --RUGOSO ', Rugosa)
    Centroide_Rugosa = CentroideClasse(features_classe_rugosa,numero_amostra_classe_rugosa)
    print('Centroide_Rugosa', Centroide_Rugosa)

    DistaciaEntreCentroide=distance.euclidean(Centroide_Rugosa, Centroide_Lisa)
    print('DistaciaEntreCentroide',DistaciaEntreCentroide)
