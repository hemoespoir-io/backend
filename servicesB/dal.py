import mysql.connector as mysql
from mysql.connector import Error
#from Analyse_de_donnes.testt import Medicament
from models import patient, Medicament,medecins,medicamentPatients,medecinPatient


class DAOpatients:
    @staticmethod
    def AjouterPatientbyId(cur, con, patient):
        cur.execute('INSERT INTO patient (Id_Patient, NomUtilisateur, Nomcomplet, DateNaissance, Email, Telephone, Adresse, Motdepasse, image, Groupesanguin, Taille, Poids, Sexe, AntecedentMere, AntecedentPere, TypeDeMaladie) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                    (patient.Id_Patient, patient.NomUtilisateur, patient.Nomcomplet, patient.DateNaissance, patient.Email, patient.Telephone, patient.Adresse, patient.Motdepasse, patient.image, patient.Groupesanguin, patient.Taille, patient.Poids, patient.Sexe, patient.AntecedentMere, patient.AntecedentPere, patient.TypeDeMaladie))
        con.commit()

    @staticmethod
     
    def SupprimerPatientbyId(cur, con, id):
        try:
            # Démarrer une transaction
            cur.execute("START TRANSACTION;")
            
            # Supprimer d'abord de la table medecinPatient
            cur.execute("""
                DELETE medecinPatient 
                FROM medecinPatient 
                JOIN patient ON medecinPatient.patientId = patient.Id_Patient
                WHERE patient.Id_Patient = %s
            """, (id,))
            
            # Ensuite, supprimer de la table patient
            cur.execute("DELETE FROM patient WHERE Id_Patient = %s;", (id,))
            
            # Valider la transaction
            con.commit()
        except Exception as e:
            # En cas d'erreur, annuler la transaction
            con.rollback()
            raise e
    @staticmethod
    def ModifierPatientBymdp(cur, con, NomUtilisateur: str, mdp: str):
        cur.execute("UPDATE patient SET Motdepasse = %s WHERE NomUtilisateur = %s", (mdp, NomUtilisateur))
        con.commit()

    @staticmethod
    def patient_poid_by_Id(cur, id: int):
        cur.execute("SELECT Poids FROM patient WHERE Id_Patient=%s", (id,))
        result = cur.fetchall()
        if result:
            return result[0]
        else:
            return None
    @staticmethod
    def logIn(cur, username, password):
        query = "SELECT * FROM patient WHERE NomUtilisateur = %s AND Motdepasse = %s"
        cur.execute(query, (username, password))
        return cur.fetchall()
    

    @staticmethod
    def logOutByEmail_Passowrd(cur, gmail: str, mdp: str):
        query = "SELECT * FROM patient WHERE Email=%s AND Motdepasse=%s"
        cur.execute(query, (gmail, mdp))
        result = cur.fetchall()
        return result

    @staticmethod
    def search_by_Id(cur, id: int):
        cur.execute("SELECT * FROM patient WHERE Id_Patient=%s", (id,))
        result = cur.fetchall()
        return result
    @staticmethod
    def get_patient_by_Id(cur, Id_patient: int):
        query = "SELECT * FROM patient WHERE Id_Patient = %s"
        cur.execute(query, (Id_patient,))
        result = cur.fetchall()
        return result
    

    @staticmethod
    def Get_Age_by_Date_Naissance(cur, dataNaissance: str):
        cur.execute("SELECT DateNaissance FROM patient WHERE DateNaissance=%s", (dataNaissance,))
        result = cur.fetchall()
        if result:
            return result[0]['DateNaissance']
        else:
            return None
    @staticmethod
    def lastPatient_Id(cur):
        cur.execute("SELECT * FROM patient ORDER BY Id_Patient DESC LIMIT 1")
        result = cur.fetchall()
        return result

    @staticmethod
    def fetch_patient_info_by_Id(cur, patient_id):
        query = """
        SELECT * FROM patient 
        WHERE Id_Patient = %s
        """
        cur.execute(query, (patient_id,))
        return cur.fetchall()
    @staticmethod
    def fetch_medecins_details_by_patient_id(cur, Id_Patient):
            query = """
        SELECT *
        FROM medecinPatient mp
        INNER JOIN  medecins m ON mp.medecinId = m.Id_Medecin  -- Ajustez le nom de la table et la colonne si nécessaire
        WHERE mp.patientId = %s
        """
            cur.execute(query, (Id_Patient,))
            return cur.fetchall()
    @staticmethod
    def fetch_medicaments_details_by_patient_id(cur, Id_Patient):
        query = """
            SELECT m.nom_medicament, mp.dose, mp.derniere_date_de_prise
            FROM medicament m
            JOIN medicamentPatients mp ON m.id_Medicament = mp.id_Medicament
            WHERE mp.Id_Patient = %s
        """
        cur.execute(query, (Id_Patient,))
        return cur.fetchall()


class DAOmedicament:
    @staticmethod

    def Ajouter_Medicament(cur, con, medi):
        cur.execute('INSERT INTO medicament (nom_medicament, Id_Patient, id_Medicament) VALUES (%s, %s, %s)',
                    (medi.nom_medicament, medi.Id_Patient, medi.id_Medicament))
        con.commit()

    @staticmethod
    def deletemedicament_by_Id(cur, con, medi: Medicament):
        try:
            cur.execute("DELETE FROM medicament WHERE id_Medicament=%s", (medi.id_Medicament,))
            con.commit()
        except Exception as e:
            con.rollback()
            raise e

    @staticmethod
     
    def search_Medicament_by_Id(cur, nom: str, idPatient: int):
        try:
            cur.execute("SELECT * FROM Medicament WHERE  nom_medicament=%s AND Id_Patient=%s", (nom, idPatient))
            result = cur.fetchall()
            return result
        except Exception as e:
            print(f"Error executing query: {e}")
            return None
    @staticmethod
    def Medicament_details_byID(cur, id: int):
        cur.execute("SELECT * FROM medicament WHERE id_Medicament=%s", (id,))
        result = cur.fetchall()
        return result


class DAOmedecin:
    @staticmethod
    def Ajouter_medecin(cur, con, nom: str, spe: str, idp: int, image: str):
        cur.execute('INSERT INTO medecins (nom, specialite, Id_Medecin, image,numero_urgence) VALUES (%s, %s, %s, %s,%s)',
                    (nom, spe, idp, image))
        con.commit()

    @staticmethod
    def deletemed(con, Idmedecin):
        with con.cursor(dictionary=True) as cur:
            cur.execute("DELETE FROM medecins WHERE Id_Medecin = %s", (Idmedecin,))
            con.commit()
            return True, "Record deleted"

    @staticmethod
    def medecin_detail_by_Id(cur, id: int):
        cur.execute("SELECT * FROM medecins WHERE Id_Medecin = %s", (id,))
        result = cur.fetchall()
        return result
