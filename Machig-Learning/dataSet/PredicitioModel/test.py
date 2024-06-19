import pandas as pd

from sklearn.model_selection import train_test_split
import time
from sklearn.naive_bayes import GaussianNB


data = pd.read_excel("C:\\Users\\kella\\Desktop\\Traitement-des-patients-reduites\\Back-end\\dataSet\\dataSetNumbers.xlsx",sheet_name=1)


features=['age','Sexe','Transmission genetique','mode recessif(heriditaire)']

X=data[features]
Y=data['hemophilie']


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.1, random_state=101)

dtree = GaussianNB()
dtree = dtree.fit(X, Y)



def decision():

    print('Your name:')
    name= input()

    print('Enter your Sexe:')
    Sexe= input()
    
    print("What's your age:")
    age= input()

    print('DO you have a chromosome MP heridite from your mother:')
    MP= input()

    print('DO you have a chromosome X heridite from your father:')
    modeRecessif= input()

    SexeNumber = {
        'HOMME': 2,
        'FEMME': -2
        }.get(Sexe.upper(), None)

    modeRecessifNumber = {
        'NO': -6,
        'YES': 6,
        }.get(modeRecessif.upper(), None)

    MPNumber = {
        'NO': -7,
        'YES': 7,
        } .get(MP.upper(), None)
    

    listOfInformation=[age,SexeNumber,MPNumber,modeRecessifNumber]

    test_x = pd.DataFrame([listOfInformation], columns=['age','Sexe','Transmission genetique','mode recessif(heriditaire)'])
    print("Attendez pour votre resultat...")
    time.sleep(5)
    try:
        if dtree.predict(test_x)==[1]:
            print("la resultat est: vous etes malade")
        else:
            print("la resultat est: vous n'etes pas malade")
    except Exception:
        print("Error information")
    
    
if __name__=='__main__':
    decision()