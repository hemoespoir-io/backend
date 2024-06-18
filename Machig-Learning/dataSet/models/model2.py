import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.model_selection import cross_val_score,KFold

data = pd.read_excel("C:\\Users\\kella\\Desktop\\Traitement-des-patients-reduites\\Back-end\\dataSet\\dataSetNumbers.xlsx",sheet_name=1)


features=['age','Sexe','Transmission genetique','mode recessif(heriditaire)']
X=data[features]
Y = data['hemophilie']
#train_test_split=la manipulation de données dans l'apprentissage automatique
#test_size=0.2 c'est pour les donne de test et 0.8 c'est pour les donnes d'entrainement
X_train, X_test, y_train, y_test = train_test_split(X, Y.values.ravel(), test_size=0.1, random_state=101)
model = DecisionTreeClassifier()


model.fit(X_train, y_train)
prediction = model.predict(X_test)

#CROSS_VALIDATION
cv=KFold(5,random_state=0,shuffle=True)
print("Cross Validation: ",cross_val_score(model,X_train,y_train,cv=cv,scoring='accuracy').mean())

#print("Test and Train de DataSet est: ",metrics.accuracy_score(prediction, y_test) * 100)


