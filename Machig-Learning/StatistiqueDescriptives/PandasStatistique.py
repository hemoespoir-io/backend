import pandas as pd

data = pd.read_excel("C:\\Users\\kella\\Desktop\\Traitement-des-patients-reduites\\Back-end\\dataSet\\dataSetNumbers.xlsx",sheet_name=1)
#moyenne, colleration, medium, les notions statistiques, plot,..

features=['age','Sexe','Transmission genetique','mode recessif(heriditaire)']

X=data[features]
Y=data['hemophilie']

#print(data)
#print(data.head())
#print(data.describe())
#print(data.mean)
"""new_dataX=data[features]
print(new_dataX.corr())"""
"""print(data[features[0]].value_counts())
print(data[features[1]].median())
print(data[features[2]].mode())
print(data[features[0]].std())
print(data[features[2]].cov(data[features[3]]))"""

data_sans_valeurs_manquantes = data.dropna()
print(data_sans_valeurs_manquantes)