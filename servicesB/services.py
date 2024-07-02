from dal import DAOpatients, DAOmedicament, DAOmedecin
from models import patient, medicament, medecins, medicamentPatients
from datetime import datetime
import matplotlib.pyplot as plt
from dataclasses import dataclass
from datetime import datetime, date
from typing import List
from Analyse_de_donnes.test import decision
from Analyse_de_donnes.testt import Patients
import mysql.connector as mysql


def connect_db():
    try:
        con = mysql.connect(
            host="34.122.67.28",
            user='root',
            passwd='nabil123!',
            database='pfe',
            port='3306',
            charset="utf8mb4"
        )
        return con
    except mysql.Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

class patientServices:
    @staticmethod
    def get_patient_details(patient_id):
        con = connect_db()
        if con is None:
            return None, "Connection to database failed"

        with con.cursor(dictionary=True) as cur:
            patient = DAOpatients.fetch_patient_info_by_Id(cur, patient_id)
            if not patient:
                con.close()
                return None, "No patient found with Id_Patient = " + str(patient_id)
        
            patient_info = {
                "patient": patient,
                "medicament": DAOpatients.fetch_medicaments_details_by_patient_id(cur, patient_id),
                "medecins": DAOpatients.fetch_medecins_details_by_patient_id(cur, patient_id)
            }

        con.close()
        return patient_info, None

    @staticmethod
    def get_patient_byID(username):
        con = connect_db()
        if con is None:
            return None, "Connection to database failed"
        
        with con.cursor(dictionary=True) as cur:
            result = DAOpatients.get_patient_by_Id(cur, username)
            if result:
                con.close()
                return patient(*result[0])
            con.close()
            return None

    @staticmethod
    def calculate_age(birth_date):
        if isinstance(birth_date, str):
            birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
        today = datetime.today()
        return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    @staticmethod
    def addPatients(patient):
        con = connect_db()
        if con is None:
            return None, "Connection to database failed"
        
        with con.cursor(dictionary=True) as cur:
            DAOpatients.AjouterPatientbyId(cur, con, patient)
        con.close()

    @staticmethod
    def deletePatients(id):
        con = connect_db()
        if con is None:
            return None, "Connection to database failed"
        
        with con.cursor(dictionary=True) as cur:
            DAOpatients.SupprimerPatientbyId(cur, con, id)
        con.close()

    @staticmethod
    def LogIn(nom: str, mdp: str):
        con = connect_db()
        if con is None:
            return None, "Connection to database failed"
        
        with con.cursor(dictionary=True) as cur:
            result = DAOpatients.logIn(cur, nom, mdp)
            if result:
                patient = Patients(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4], result[0][5], result[0][6], result[0][7], result[0][8], result[0][9], result[0][10], result[0][11], result[0][12], result[0][13], result[0][14])
                con.close()
                return patient
            con.close()
            return None

    @staticmethod
    def ModifierPatientByPassword(nom: str, mdp: str):
        con = connect_db()
        if con is None:
            return None, "Connection to database failed"
        
        with con.cursor(dictionary=True) as cur:
            DAOpatients.ModifierPatientBymdp(cur, con, nom, mdp)
        con.close()

    @staticmethod
    def patient_age1(nom: str):
        con = connect_db()
        if con is None:
            return None, "Connection to database failed"
        
        with con.cursor(dictionary=True) as cur:
            result = DAOpatients.Get_Age_by_Date_Naissance(cur, nom)
            if result:
                con.close()
                return result
            con.close()
            return None

    @staticmethod
    def pasParJours(age, weight):
        dict = {}
        JoursPatient = []
        JoursPasPatient = []

        if int(weight) < 20 or int(weight) >= 100:
            JoursPatient = ["Anomalie : veuillez consulter un médecin le plus tôt possible"]
            JoursPasPatient = [0]
        else:
            if 3 < int(age) <= 5:
                jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
                pas_jour = [50, 40, 30, 40, 20, 10, 30]
                JoursPatient = jours
                JoursPasPatient = pas_jour
            elif 6 <= int(age) <= 10:
                jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
                pas_jour = [10000, 11000, 14000, 9000, 10000, 13000, 11000]
                JoursPatient = jours
                JoursPasPatient = pas_jour
            elif 10 < int(age) <= 20:
                jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
                pas_jour = [10000, 11000, 11500, 12000, 11000, 12000, 13000]
                JoursPatient = jours
                JoursPasPatient = pas_jour
            elif 20 < int(age) <= 60:
                jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
                pas_jour = [7000, 9000, 10000, 8500, 7500, 9500, 10000]
                JoursPatient = jours
                JoursPasPatient = pas_jour
            elif 60 < int(age) <= 70:
                jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
                pas_jour = [8000, 7500, 6500, 6000, 7900, 6800, 8200]
                JoursPatient = jours
                JoursPasPatient = pas_jour
            elif 70 < int(age) <= 80:
                jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
                pas_jour = [3000, 3000, 3000, 3000, 3000, 3000, 3000]
                JoursPatient = jours
                JoursPasPatient = pas_jour
            elif 80 < int(age) <= 100:
                jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
                pas_jour = [100, 80, 60, 70, 20, 60, 40]
                JoursPatient = jours
                JoursPasPatient = pas_jour

            if int(weight) > 90 and int(weight) < 100:
                JoursPasPatient = [int(steps * 0.5) for steps in JoursPasPatient]

        for i, j in zip(JoursPatient, JoursPasPatient):
            dict[i] = j
        return dict

    @staticmethod
    def checkAge(age: int):
        if age <= 3 or age >= 101:
            return False
        return True

    @staticmethod
    def checkPoids(poids: int):
        if int(poids) == 0:
            return False
        return True

    @staticmethod
    def LogOut_by_Email_Password(gmail: str, mdp: str):
        con = connect_db()
        if con is None:
            return None, "Connection to database failed"
        
        with con.cursor(dictionary=True) as cur:
            result = DAOpatients.logOutByEmail_Passowrd(cur, gmail, mdp)
            if result:
                patient = patient(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4], result[0][5], result[0][6], result[0][7], result[0][8], result[0][9], result[0][10], result[0][11], result[0][12], result[0][13], result[0][14])
                con.close()
                return patient
            con.close()
            return None

    @staticmethod
    def patient_age2(DateNaissance: str):
        con = connect_db()
        if con is None:
            return None, "Connection to database failed"
        
        with con.cursor(dictionary=True) as cur:
            result = DAOpatients.Get_Age_by_Date_Naissance(cur, DateNaissance)
            if result:
                con.close()
                return result
            con.close()
            return None

    @staticmethod
    def DecisinoPatient(id: int):
        return decision(id)

    @staticmethod
    def Rechercher_by_Id(id: int):
        con = connect_db()
        if con is None:
            return None, "Connection to database failed"
        
        with con.cursor(dictionary=True) as cur:
            result = DAOpatients.search_by_Id(cur, id)
            con.close()
            return result

    @staticmethod
    def lastPatient_byID():
        con = connect_db()
        if con is None:
            return None, "Connection to database failed"
        
        with con.cursor(dictionary=True) as cur:
            result = DAOpatients.lastPatient_Id(cur)
            if result:
                patient = patient(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4], result[0][5], result[0][6], result[0][7], result[0][8], result[0][9], result[0][10], result[0][11], result[0][12], result[0][13], result[0][14])
                con.close()
                return patient
            con.close()
            return None

    @staticmethod
    def patient_poid(id: int):
        con = connect_db()
        if con is None:
            return None, "Connection to database failed"
        
        with con.cursor(dictionary=True) as cur:
            result = DAOpatients.patient_poid_by_Id(cur, id)
            if result:
                con.close()
                return result[0][0]
            con.close()
            return None

    @staticmethod
    def generate_steps_plot(age, weight):
        steps_data = patientServices.pasParJours(age, weight)
        days = list(steps_data.keys())
        steps = list(steps_data.values())

        plt.figure(figsize=(12, 7))
        if int(weight) < 20 or int(weight) >= 95:
            plt.text(0.5, 0.5, "Anomalie : veuillez consulter un médecin le plus tôt possible\n\nVotre age: " + str(age) + "\n\nVotre Poids: " + str(weight),
                     horizontalalignment='center', verticalalignment='center', fontsize=15, color='red', transform=plt.gca().transAxes)
            plt.axis('off')
        else:
            plt.bar(days, steps, color='royalblue', edgecolor='black')
            plt.title(f'Nombre de pas par jour pour un patient de {age} ans et {weight} kg', fontsize=15, fontweight='bold')
            plt.xlabel('Jour de la semaine', fontsize=12)
            plt.ylabel('Nombre de pas', fontsize=12)
            plt.xticks(rotation=45, fontsize=10)
            plt.yticks(fontsize=10)
            plt.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)
            for i, v in enumerate(steps):
                plt.text(i, v + 100, str(v), ha='center', fontsize=10, fontweight='bold')
            plt.tight_layout()
        plt.show()


class MedicamentService:
    @staticmethod
    def Medicament_details_ID(id_patient: int):
        con = connect_db()
        if con is None:
            return None, "Connection to database failed"
        
        allmedicaments = []
        with con.cursor(dictionary=True) as cur:
            result = DAOmedicament.Medicament_details_byID(cur, id_patient)
            for i in result:
                med = medicament(*i)
                allmedicaments.append(med)
        con.close()
        return allmedicaments

    @staticmethod
    def ajouterMedicament(medi):
        con = connect_db()
        if con is None:
            return None, "Connection to database failed"
        
        with con.cursor(dictionary=True) as cur:
            DAOmedicament.Ajouter_Medicament(cur, con, medi)
        con.close()

    @staticmethod
    def deletemedicament_by_Id(medi):
        con = connect_db()
        if con is None:
            return None, "Connection to database failed"
        
        with con.cursor(dictionary=True) as cur:
            DAOmedicament.deletemedicament_by_Id(cur, con, medi)
        con.close()

    @staticmethod
    def searchMedicament_by_Id(nom: str, idPatient: int):
        con = connect_db()
        if con is None:
            return None, "Connection to database failed"
        
        with con.cursor(dictionary=True) as cur:
            result = DAOmedicament.search_Medicament_by_Id(cur, nom, idPatient)
            if result:
                med = medicament(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4], result[0][5])
                con.close()
                return med
            con.close()
            return None


class medecinservices:
    @staticmethod
    def addMedecins(nom: str, spe: str, id: int, image: str):
        con = connect_db()
        if con is None:
            return None, "Connection to database failed"
        
        with con.cursor(dictionary=True) as cur:
            DAOmedecin.Ajouter_medecin(cur, con, nom, spe, id, image)
        con.close()

    @staticmethod
    def deletemed(id: int):
        con = connect_db()
        if con is None:
            return None, "Connection to database failed"
        
        with con.cursor(dictionary=True) as cur:
            DAOmedecin.deletemedecin(cur, con, id)
        con.close()

    @staticmethod
    def searchmedecin(id: int):
        con = connect_db()
        if con is None:
            return None, "Connection to database failed"
        
        allmedecin = []
        with con.cursor(dictionary=True) as cur:
            result = DAOmedecin.medecin_detail_by_Id(cur, id)
            for i in result:
                Med = medecins(i[0], i[1], i[3], i[2], i[4], i[5])
                allmedecin.append(Med)
        con.close()
        return allmedecin


if __name__ == "__main__":
    patient_info, error = patientServices.get_patient_details(9)
    
    if error:
        print(error)
    