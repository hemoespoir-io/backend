import mysql.connector as mysql
from models import Patients, Medicament
from datetime import datetime
import matplotlib.pyplot as plt

# Connexion à la base de données
con = mysql.connect(
    host="34.122.67.28",
    user='root',
    passwd='nabil123!',
    database='hemophelie',
    port='3306',
    charset="utf8mb4"
)
cur = con.cursor()

class DAOpatients:
    @staticmethod
    def newPatients(patient: Patients):
        cur.execute('INSERT INTO Patient (NomUtilisateur, Nomcomplet, DateNaissance, Email, Telephone, Adresse, Motedepasse, image, Groupesanguin, Taille, Poids, Sexe, AntecedeantMere, AntecedeantPere) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                    (patient.nomutilisateur, patient.Nomcomplet, patient.Date_Naissance, patient.email, patient.num_tel, patient.adresse, patient.mdp, patient.image, patient.Groupesanguin, patient.taille, patient.Poids, patient.sexe, patient.AntecedeantMere, patient.AntecedeantPere))
        con.commit()

    @staticmethod
    def deletePatient(id: int):
        cur.execute("DELETE FROM Patient where Id=%s", (id,))
        con.commit()

    @staticmethod
    def updatePatient(NomUtilisateur: str, mdp: str):
        cur.execute("UPDATE Patient SET Motedepasse=%s WHERE NomUtilisateur=%s", (mdp, NomUtilisateur,))
        con.commit()

    @staticmethod
    def patient_poid(nom: str):
        cur.execute("SELECT Poids FROM Patient where NomUtilisateur=%s", (nom,))
        result = cur.fetchall()
        return result

    @staticmethod
    def logIn(username: str, password: str):
        query = "SELECT * FROM Patient WHERE NomUtilisateur = %s AND Motedepasse = %s"
        cur.execute(query, (username, password))
        result = cur.fetchall()
        return result

    @staticmethod
    def logOut(gmail: str, mdp: str):
        cur.execute("select * from Patient where Email=%s and Motedepasse=%s", (gmail, mdp,))
        result = cur.fetchall()
        return result

    @staticmethod
    def search(id: int):
        cur.execute("select * from Patient where Id=%s", (id,))
        result = cur.fetchall()
        return result

    @staticmethod
    def get_patient_by_username(username: str):
        query = "SELECT * FROM Patient WHERE NomUtilisateur = %s"
        cur.execute(query, (username,))
        result = cur.fetchall()
        return result

    @staticmethod
    def patient_age1(NomUtilisateur: str):
        cur.execute("SELECT DateNaissance FROM Patient where NomUtilisateur=%s", (NomUtilisateur,))
        result = cur.fetchall()
        return result[0][0]

    @staticmethod
    def patient_age2(dataNaissance: str):
        cur.execute("SELECT DateNaissance FROM Patient where DateNaissance=%s", (dataNaissance,))
        result = cur.fetchall()
        return result[0][0]

    @staticmethod
    def lastPatient():
        cur.execute("SELECT * FROM Patient ORDER BY Id DESC LIMIT 1")
        result = cur.fetchall()
        return result

class DAOmedicament:
    @staticmethod
    def newMedicament(medicament: Medicament):
        cur.execute('INSERT INTO Medicament (nom, Id, dose_recommandee, dernier_date_de_prise, time) VALUES (%s,%s,%s,%s,%s)', 
                    (medicament.nom, medicament.idPatient, medicament.dose_recommandee, medicament.dernier_date_de_prise, medicament.time))
        con.commit()

    @staticmethod
    def deletemedicament(medi: Medicament):
        cur.execute("DELETE FROM Medicament where nom=%s", (medi.nom,))
        con.commit()

    @staticmethod
    def search(nom: str, idPatient: int):
        cur.execute("select * from Medicament where nom=%s and Id=%s", (nom, idPatient,))
        result = cur.fetchall()
        return result

    @staticmethod
    def allMedicament(id: int):
        cur.execute('select * from Medicament where Id=%s', (id,))
        result = cur.fetchall()
        return result

class DAOmedecin:
    @staticmethod
    def newMeddin(nom: str, spe: str, idp: int, image: str):
        cur.execute('INSERT INTO Medecin (nom, specialite, Id, image) VALUES (%s, %s, %s, %s)', 
                    (nom, spe, idp, image))
        con.commit()

    @staticmethod
    def deletemedecin(nom: str):
        cur.execute("DELETE FROM Medecin where nom=%s", (nom,))
        con.commit()

    @staticmethod
    def getall(id: int):
        cur.execute("SELECT * FROM Medecin WHERE Id = %s", (id,))
        result = cur.fetchall()
        return result

class patientServices:
    @staticmethod
    def get_patient_by_username(username):
        result = DAOpatients.get_patient_by_username(username)
        if result:
            return Patients(*result[0])
        return None

    @staticmethod
    def calculate_age(birth_date):
        if isinstance(birth_date, str):
            birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
        today = datetime.today()
        return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    @staticmethod
    def fiche_medicale(username):
        patient = patientServices.get_patient_by_username(username)
        if not patient:
            return "Patient not found"
        age = patientServices.calculate_age(patient.Date_Naissance)
        weight = patient.Poids
        blood_group = patient.Groupesanguin
        medications = MedicamentService.allMedicament(patient.Id)
        
        medical_record = f"Fiche Médicale pour {patient.Nomcomplet}\n{'='*30}\n"
        medical_record += f"Age: {age} ans\n"
        medical_record += f"Poids: {weight} kg\n"
        medical_record += f"Groupe sanguin: {blood_group}\n"
        medical_record += f"Sexe: {patient.Sexe}\n"
        medical_record += f"Antécédent Mère: {patient.AntecedeantMere}\n"
        medical_record += f"Antécédent Père: {patient.AntecedeantPere}\n"
        medical_record += f"\nListe des Médicaments:\n{'-'*30}\n"
        for med in medications:
            medical_record += f"Nom: {med[0]}\nDose: {med[2]} UI\nDate de prise: {med[3]}\nHeure de prise: {med[4]}\n{'-'*30}\n"
        
        return medical_record

class MedicamentService:
    @staticmethod
    def allMedicament(id_patient: int):
        allmedicaments = []
        result = DAOmedicament.allMedicament(id_patient)
        for i in result:
            med = Medicament(i[0], i[1], i[2], i[3], i[4], i[5])
            allmedicaments.append(med)
        return allmedicaments

if __name__ == "__main__":
    print(patientServices.fiche_medicale("q"))
