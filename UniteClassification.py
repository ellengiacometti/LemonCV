import os
import glob
import pandas as pd
# Setting path to read classification files
dir ="C:/Users/ellen.giacometti/PycharmProjects/LemonCV/CLASSIFICACOES"
# Creating columns for final file, the one with voted classification
final_sample = []
final_label=[]
R = []
L = []
C = []
S = []
X = []
# Looking up all  files inside provided path folder
for filename in os.listdir(dir):
    print(filename)
    # Reading CSV file with labeled info
    file = pd.read_csv(os.path.join(dir,filename), index_col=False, sep=";")
    # Separating file columns
    sample_column=pd.Series(file['Sample'])
    label_column=pd.Series(file['Rotulo'])

    for index, sample_filename in enumerate(sample_column):
        x=0
        maturity=''
        defect=''
        if len(label_column[index]) != 1:
            maturity = label_column[index][0]
            defect = label_column[index][1]
        else:
            x=1
        # Checking if sample was already classified
        if sample_filename in final_sample:
            index_final = final_sample.index(sample_filename)
            # Getting each attribute label and adding with previous one
            if x==1:
                X[index_final] = X[index_final] + 1
            else:
                if maturity == "R":
                    R[index_final] = R[index_final] + 1
                elif maturity == "L":
                    L[index_final] = L[index_final] + 1
                if defect == "C":
                    C[index_final] = C[index_final] + 1
                elif defect == "S":
                    S[index_final] = S[index_final] + 1
        #If sample was not in file , create a new line and add current label
        else:
            final_sample.append(sample_filename)

            if x==1:
                X.append(1)
                R.append(0)
                L.append(0)
                C.append(0)
                S.append(0)
            else:
                if maturity == "R" and defect == "C" :
                    X.append(0)
                    R.append(1)
                    C.append(1)
                    L.append(0)
                    S.append(0)

                elif maturity == "L" and defect == "C":
                    X.append(0)
                    R.append(0)
                    C.append(1)
                    L.append(1)
                    S.append(0)
                elif maturity == "L" and defect == "S":
                    X.append(0)
                    R.append(0)
                    C.append(0)
                    L.append(1)
                    S.append(1)
                elif maturity == "R"and defect == "S":
                    X.append(0)
                    R.append(1)
                    C.append(0)
                    L.append(1)
                    S.append(0)


data=pd.DataFrame([R, L, C, S, X])

for index in range(data.shape[1]):
    if  X[index]>(R[index]+L[index]) or X[index]>(C[index]+S[index]):
        # Drop Sample
        final_label.append('X')
    else:
        if R[index]>L[index]:
            if C[index]>=S[index]:
                # RC
                final_label.append('RC')
            else:
                # RS
                final_label.append('RS')
        elif L[index]>=R[index]:
            if C[index]>=S[index]:
                # LC
                final_label.append('LC')
            else:
                #LS
                final_label.append('LS')

final_sample_name= pd.Series(final_sample)
# Cleaning sample name (an additional sequence was introduced to serialize sample at Limatch)
final_sample_name=final_sample_name.str.slice(start=-12)

raw_data = {'nome': final_sample_name, 'R': R,'L': L,'C': C,'S': S,'X': X,'Voted Label':final_label}
df = pd.DataFrame(raw_data,columns=['Sample', 'R','L','C','S','X','Voted Label'])
df.to_csv('VotedClassification.csv',index=False,sep=";")
print("Arquivo Criado!")