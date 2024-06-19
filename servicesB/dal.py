import mysql.connector as mysql
from models import Patients , Medicament
con=mysql.connect(
    host="34.122.67.28",
    user='root',
    passwd='nabil123!',
    database='hemophelie',
    port='3306',
    charset="utf8mb4"
  )
cur=con.cursor()


class DAOpatients:

    @staticmethod
    def newPatients(patient:Patients):
        cur.execute('INSERT INTO Patient (NomUtilisateur, Nomcomplet, DateNaissance, Email, Telephone, Adresse, Motedepasse, image, Groupesanguin, Taille, Poids, Sexe, AntecedeantMere, AntecedeantPere) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                    (patient.nomutilisateur,patient.Nomcomplet,patient.Date_Naissance,patient.email,patient.num_tel,patient.adresse,patient.mdp,patient.image,patient.GR_S,patient.taille,patient.poids,patient.sexe,patient.antecedant_mere,patient.antecedant_pere))
        con.commit()
    
    @staticmethod
    def deletePatient(id:int):
        cur.execute("DELETE FROM Patient where Id=%s",(id,))
        con.commit()


    @staticmethod
    def updatePatient(NomUtilisateur:str,mdp:str):
        cur.execute("UPDATE Patients SET mdp=%s WHERE NomUtilisateur=%s", ( mdp ,NomUtilisateur,))
        con.commit()

    @staticmethod
    def patient_poid(nom: str):
        cur.execute("SELECT Poids FROM Patient where NomUtilisateur=%s", (nom,))
        result = cur.fetchall()
        return result

    @classmethod
    def logIn(cls, username: str, password: str):
        cursor = cls.db.cursor(dictionary=True)  # Create a cursor directly from the class-level db connection
        query = "SELECT * FROM Patient WHERE NomUtilisateur = %s AND Motedepasse = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchall()
        cursor.close()  # Good practice to close cursor after usage
        return result

        # Usage:
        db = PatientDatabase(host='hostname', user='username', password='yourpassword', database='yourdatabase')
        user_info = db.logIn('user', 'password')
        print(user_info)

    #print(DAOpatients.logOut("123","Email"))
    @staticmethod 
    def logOut(gmail:str,mdp:str):
        cur.execute("select * from Patient where Email=%s and Motedepasse=%s",(gmail,mdp,))  
        result=cur.fetchall() 
        return result


    @staticmethod
    def search(id:int):
        cur.execute("select * from Patient where id=%s",(id,))
        result=cur.fetchall()  
        return result
    

    @staticmethod
    def patient_age1(NomUtilisateur : str):
        cur.execute("SELECT DateNaissance FROM Patient where NomUtilisateur=%s",(NomUtilisateur,))
        result = cur.fetchall()
        return result[0][0]
    
    @staticmethod
    def patient_age2(dataNaissance : str):
        cur.execute("SELECT DateNaissance FROM Patient where DateNaissance=%s",(dataNaissance,))
        result = cur.fetchall()
        return result[0][0]
    
    @staticmethod
    def lastPatient():
        cur.execute("SELECT * FROM Patient ORDER BY id DESC LIMIT 1")
        result=cur.fetchall()
        return result
    
class DAOmedicament:   

    """
                nom: str
                idPatient:int
                dose: int
                Date: str
                time:str
    """

    """
        MedicamentService.ajouterMedicament(nom,dose,date,time,idPatient)
        def ajouterMedicament(nom:str,dose:int,date:str,time:str,idPatient:int)
    """

    @staticmethod
    def newMedicament(medicament:Medicament):
        cur.execute('INSERT INTO medicament (nom , Id ,dose, Date, time)VALUES (%s,%s,%s,%s,%s)',(medicament.nom,medicament.idPatient,medicament.dose,medicament.Date,medicament.time))
        con.commit()
    @staticmethod
    def deletemedicament(medi:Medicament):
        cur.execute("DELETE FROM medicament where nom=%s",(medi.nom,))
        con.commit()
    @staticmethod
    def search(nom:str,idPatient:int):
        cur.execute("select * from medicament where nom=%s and Id=%s",(nom,idPatient,))
        result=cur.fetchall()  
        """Med=Medicament(result[0][1],result[0][2],result[0][3],result[0][4])
            return Med"""
        return result
    
    @staticmethod
    def allMedicament(id:int):
        cur.execute('select * from medicament where Id=%s',(id,))
        result=cur.fetchall()
        return result

class DAOmedecin:
    
    @staticmethod
    def newMeddin(nom:str,spe:str,idp:int,image:str):
        cur.execute('INSERT INTO medecin (nom, specialite, Id,image) VALUES (%s, %s, %s,%s)',(nom,spe,idp,image))   
        con.commit()

    @staticmethod
    def deletemedecin(nom:str):
        cur.execute("DELETE FROM medecin where nom=%s", (nom,))
        con.commit()

    @staticmethod
    def getall(id: int):
        cur.execute("SELECT * FROM medecin WHERE id = %s", (id,))
        result = cur.fetchall()
        return result
    



    
if __name__=='__main__':
    #patient=Patients("nom","prenom","2024-05-25","Email","image.png","0621870090","Adresse","123","","","","","","")
    """DAOpatients.newPatients(patient)"""
    #medicament1=Medicament("nom1",63,100,"2024-05-30","10:30:10")
    #(medicament.nom,medicament.idPatient,medicament.dose,medicament.Date,medicament.time)
    #medicament2=Medicament(0,"nom",65,100,"2024-01-04","10")
    #DAOmedicament.newMedicament(medicament1)
    #DAOmedicament.newMedicament(medicament2)
    #DAOmedicament.newMedicament("nom1",100,"2024-10-04","10:00:00",65)
    #DAOmedicament.deletemedicament(medicament1)
    #print(DAOmedicament.search("nom2",65))
    #print(DAOpatients.logOut("Email","123"))
    #print(DAOpatients.patient_age2("2020-05-28"))
    #print(DAOpatients.lastPatient())
    #print(DAOmedicament.allMedicament(63))
    