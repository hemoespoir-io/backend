import mysql.connector as mysql
from models import patient, medicament
from datetime import datetime
import matplotlib.pyplot as plt
import sqlite3
con = mysql.connect(
    host="34.122.67.28",
    user='root',
    passwd='nabil123!',
    database='pfe',
    port='3306',
    charset="utf8mb4"
)

cur = con.cursor()


def fetch_medicaments_and_details_for_patient(con, Id_Patient):
    cursor = con.cursor(dictionary=True)
    query = """
    SELECT m.nom, mp.dose, mp.derniere_date_de_prise
    FROM medicament m
    JOIN medicamentPatients mp ON m.id_Medicament = mp.id_Medicament
    WHERE mp.Id_Patient = %s
    """
    cursor.execute(query, (Id_Patient,))
    combined_data = cursor.fetchall()
    return combined_data



class DAOpatients:
    @staticmethod
   
    def newPatients(patient):
        # Ici, il est supposé que `cur` et `con` sont des objets déjà instanciés et connectés à la base de données.
        cur.execute('INSERT INTO patient ( Id_Patient, NomUtilisateur, Nomcomplet, DateNaissance, Email, Telephone, Adresse, Motdepasse, image, Groupesanguin, Taille, Poids, Sexe, AntecedentMere,AntecedentPere,TypeDeMaladie) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                    ( patient.Id_Patient, patient.NomUtilisateur, patient.Nomcomplet, patient.DateNaissance, patient.Email, patient.Telephone, patient.Adresse, patient.Motdepasse, patient.image, patient.Groupesanguin, patient.Taille, patient.Poids, patient.Sexe, patient.AntecedentMere, patient.AntecedentPere,patient.TypeDeMaladie))
        con.commit()


    @staticmethod
    def deletePatient(id):
        # Ici, il est supposé que `cur` et `con` sont des objets déjà instanciés et connectés à la base de données.
        cur.execute("DELETE FROM patient WHERE Id_Patient=%s", (id,))
        con.commit()
    @staticmethod
    def updatePatient(NomUtilisateur: str, mdp: str):
        # Assurez-vous que `cur` est un curseur de base de données configuré pour effectuer des opérations SQL.
        cur.execute("UPDATE patient SET Motdepasse = %s WHERE NomUtilisateur = %s", (mdp, NomUtilisateur,))
        con.commit()

    @staticmethod
    def patient_poid(nom: str):
        # Assurez-vous que `cur` est un curseur de base de données configuré pour effectuer des opérations SQL.
        cur.execute("SELECT Poids FROM patient WHERE NomUtilisateur=%s", (nom,))
        result = cur.fetchall()
        return result

    @staticmethod
    def logIn(username: str, password: str):
        # Assurez-vous que `cur` est un curseur de base de données configuré pour effectuer des opérations SQL.
        query = "SELECT * FROM patient WHERE NomUtilisateur = %s AND Motdepasse = %s"
        cur.execute(query, (username, password))
        result = cur.fetchall()
        return result

    @staticmethod
    def logOut(gmail: str, mdp: str):
        # Assurez-vous que `cur` est un curseur de base de données configuré pour effectuer des opérations SQL.
        cur.execute("SELECT * FROM patient WHERE Email=%s AND Motdepasse=%s", (gmail, mdp,))
        result = cur.fetchall()
        return result

    @staticmethod
    def search(id: int):
        # Assurez-vous que `cur` est un curseur de base de données configuré pour effectuer des opérations SQL.
        cur.execute("SELECT * FROM patient WHERE Id_Patient=%s", (id,))
        result = cur.fetchall()
        return result
    @staticmethod
    def get_patient_by_username(username: str):
        query = "SELECT * FROM patient WHERE NomUtilisateur = %s"
        cur.execute(query, (username,))
        result = cur.fetchall()
        return result

    @staticmethod
    def patient_age1(NomUtilisateur: str):
        
        cur.execute("SELECT DateNaissance FROM patient WHERE NomUtilisateur=%s", (NomUtilisateur,))
        result = cur.fetchall()
        if result:
            return result[0][0]  # Renvoie la date de naissance
        else:
            return None 
    @staticmethod
    def patient_age2(dataNaissance: str):
       
        cur.execute("SELECT DateNaissance FROM patient WHERE DateNaissance=%s", (dataNaissance,))
        result = cur.fetchall()
        if result:
            return result[0][0]  
        else:
            return None 

    @staticmethod
    def lastPatient():
       
        cur.execute("SELECT * FROM patient ORDER BY Id_Patient DESC LIMIT 1")
        result = cur.fetchall()
        return result
    @staticmethod
    def fetch_medecins_details_by_patient_id(con, Id_Patient):
        cursor = con.cursor(dictionary=True)
        query = """
        SELECT nom, specialite, Id_Medecin, image, num_urg, DatePriseEncharge
        FROM medecins
        WHERE Id_Medecin IN (SELECT Id_Medecin FROM medecinPatients WHERE Id_Patient = %s)
        """
        print(f"Executing query: {query} with Id_Patient: {Id_Patient}")
        cursor.execute(query, (Id_Patient,))
        medecins_data = cursor.fetchall()
        print("Medecins details from DB:", medecins_data)
        return medecins_data

    @staticmethod
    def fetch_medicaments_details_by_patient_id(con, Id_Patient):
        cursor = con.cursor(dictionary=True)
        query = """
            SELECT m.nom, mp.dose, mp.derniere_date_de_prise
            FROM medicament m
            JOIN medicamentPatients mp ON m.id_Medicament = mp.id_Medicament
            WHERE mp.Id_Patient = %s
            """
        print(f"Executing query: {query} with Id_Patient: {Id_Patient}")
        cursor.execute(query, (Id_Patient,))
        combined_data = cursor.fetchall()
        print("medicament and details from DB:", combined_data)
        return combined_data
    
    @staticmethod
    def fetch_patient_info(con, patient_id):
        cursor = con.cursor(dictionary=True)
        query = "SELECT * FROM patient WHERE Id_Patient = %s"
        cursor.execute(query, (patient_id,))
        return cursor.fetchall()

class DAOmedicament:
    @staticmethod
    def newMedicament(medi: medicament):
        cur.execute('INSERT INTO medicament (nom, Id_Patient,id_Medicament ) VALUES (%s,%s,%s)', 
                    (medi.nom, medi.Id_Patient, medi.id_Medicament))
        con.commit()
        
    @staticmethod
    def deletemedicament(medi:  medicament):
        cur.execute("DELETE FROM  medicament where nom=%s", (medi.nom,))
        con.commit()
        

    @staticmethod
    def search(nom: str, idPatient: int):
        cur.execute("select * from  medicament where nom=%s and Id_Patient=%s", (nom, idPatient,))
        result = cur.fetchall()
        return result

    @staticmethod
    def allMedicament(id: int):
        # Assurez-vous que `cur` est un curseur de base de données configuré pour effectuer des opérations SQL.
        cur.execute('SELECT * FROM medicament WHERE id_Medicament=%s', (id,))
        result = cur.fetchall()
        return result
class DAOmedecin:
    @staticmethod
    def newMedecin(nom: str, spe: str, idp: int, image: str):
        # Assurez-vous que `cur` et `con` sont des curseurs de base de données et une connexion configurés pour effectuer des opérations SQL.
        cur.execute('INSERT INTO medecins (nom, specialite, Id_Medecin, image) VALUES (%s, %s, %s, %s)', 
                    (nom, spe, idp, image))
        con.commit()

    @staticmethod
    def deletemedecin(nom: str):
        # Assurez-vous que `cur` et `con` sont des curseurs de base de données et une connexion configurés pour effectuer des opérations SQL.
        cur.execute("DELETE FROM medecins WHERE nom=%s", (nom,))
        con.commit()

    @staticmethod
    def getall(id: int):
        # Assurez-vous que `cur` est un curseur de base de données configuré pour effectuer des opérations SQL.
        cur.execute("SELECT * FROM medecins WHERE Id_Medecin = %s", (id,))
        result = cur.fetchall()
        return result
