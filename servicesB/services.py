from dal import DAOpatients, DAOmedicament, DAOmedecin
from fichemedical import connect_db
from models import patient, medicament, medecins, medicamentPatients
from datetime import datetime
from dal import DAOpatients
import matplotlib.pyplot as plt
from dataclasses import dataclass
from datetime import datetime, date
from typing import List
from Analyse_de_donnes.test import decision
from Analyse_de_donnes.testt import Patients
from dal import  fetch_medicaments_details_by_patient_id
from models import patient  # Assurez-vous que votre modèle est bien structuré pour être utilisé ici.
class patientServices:
    @staticmethod
    def get_patient_details(patient_id):
        con = connect_db()
        if con is None:
            return None, "Connection to database failed"

        patient = DAOpatients.fetch_patient_info(con, patient_id)
        if not patient:
            con.close()
            return None, "No patient found with Id_Patient = " + str(patient_id)
        patient_info = {
            "patient": patient,
            "medicament": DAOpatients.fetch_medicaments_details_by_patient_id(con, patient_id)
            "medecins": DAOpatients.fetch_medecins_details_by_patient_id(con, patient_id) 
        }

        con.close()
        return patient_info, None

   
    @staticmethod
    def get_patient_by_username(username):
        result = DAOpatients.get_patient_by_username(username)
        if result:
            return patient(*result[0])
        return None

    @staticmethod
    def calculate_age(birth_date):
        if isinstance(birth_date, str):
            birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
        today = datetime.today()
        return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    @staticmethod
    def addPatients(patient):
        return DAOpatients.newPatients(patient)

    @staticmethod
    def deletePatients(id):
        return DAOpatients.deletePatient(id)
    
    @staticmethod
    def LogIn(nom: str, mdp: str):
        result = DAOpatients.logIn(nom, mdp)
        if result:
            # Création d'une instance de patient en utilisant les informations récupérées.
            # Assurez-vous que la classe 'Patients' est correctement définie avec un constructeur adapté.
            patient = Patients(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4], result[0][5], result[0][6], result[0][7], result[0][8], result[0][9], result[0][10], result[0][11], result[0][12], result[0][13], result[0][14])
            return patient
        else:
            return None  # Retourne None si aucun patient ne correspond aux critères.
    
    @staticmethod 
    def ModifyPatients(nom: str, mdp: str):
        return DAOpatients.updatePatient(nom, mdp)
    
    @staticmethod
    def patient_age1(nom: str):
        result = DAOpatients.patient_age1(nom)
        if result:
            date_naissance = result
            # Vous pourriez vouloir calculer l'âge ici en fonction de la date de naissance
            # Supposons que vous avez une fonction helper pour calculer l'âge
            # age = calculate_age(date_naissance)
            # return age
            return date_naissance
        else:
            return None  # Renvoie None si aucun patient n'est trouvé

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
    def LogOut(gmail: str, mdp: str):
        result = DAOpatients.logOut(gmail, mdp)
        if result:
            # Création d'une instance de patient avec les données récupérées.
            # Assurez-vous que la classe 'patient' est correctement définie avec un constructeur approprié.
            patient = patient(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4], result[0][5], result[0][6], result[0][7], result[0][8], result[0][9], result[0][10], result[0][11], result[0][12], result[0][13], result[0][14])
            return patient
        else:
            return None  # Retourne None si aucun patient ne correspond aux critères
    @staticmethod
    def patient_age2(DateNaissance: str):
        result = DAOpatients.patient_age2(DateNaissance)
        if result:
            return result  # Renvoie la date de naissance si trouvée
        else:
            return None  # Renvoie None si aucune date ne correspond

    @staticmethod
    def DecisinoPatient(id: int):
        return decision(id)
    
    @staticmethod 
    def search(id: int):
        result = DAOpatients.search(id)
        return result
    
    @staticmethod
    def lastPatient():
        result = DAOpatients.lastPatient()
        if result:
            # Création d'une instance de patient avec les données récupérées.
            # Assurez-vous que la classe 'patient' est correctement définie avec un constructeur approprié.
            patient = patient(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4], result[0][5], result[0][6], result[0][7], result[0][8], result[0][9], result[0][10], result[0][11], result[0][12], result[0][13], result[0][14])
            return patient
        else:
            return None  # Retourne None si aucun patient n'est trouvé
    @staticmethod
    def patient_poid(nom: str):
        result = DAOpatients.patient_poid(nom)
        if result:
            return result[0][0]  # Retourne le poids si trouvé
        else:
            return None  # Retourne None si aucun poids n'est trouvé
        
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
    def allMedicament(id_patient: int):
        allmedicaments = []
        result = DAOmedicament.allMedicament(id_patient)
        for i in result:
            # Assurez-vous que la classe `medicament` est correctement définie avec un constructeur approprié.
            med = medicament(*i)  # Création d'une instance de médicament en utilisant le tuple retourné
            allmedicaments.append(med)
        return allmedicaments
    
    @staticmethod
    def ajouterMedicament(medi):
        # DAOmedicament est appelé pour insérer le médicament dans la base de données.
        return DAOmedicament.newMedicament(medi)
       
    @staticmethod
    def deletemedicament(medi):
        # DAOmedicament est appelé pour supprimer le médicament spécifié de la base de données.
        return DAOmedicament.deletemedicament(medi)  
    
    @staticmethod
    def searchMed(nom: str, idPatient: int):
        result = DAOmedicament.search(nom, idPatient)
        if result:
            # Assurez-vous que la classe `medicament` est correctement définie avec un constructeur approprié.
            med = medicament(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4], result[0][5])  # Utilise l'opérateur de déballage pour passer les valeurs du tuple
            return med
        else:
            return None  # Retourne None si aucun médicament n'est trouvé
class medecinservices:
    @staticmethod
    def addMedecins(nom: str, spe: str, id: int, image: str):
        # Appel de la fonction DAL pour ajouter un médecin dans la base de données.
        return DAOmedecin.newMedecin(nom, spe, id, image)

    @staticmethod
    def deletemed(nom: str):
        # Appel de la fonction DAL pour supprimer un médecin dans la base de données.
        return DAOmedecin.deletemedecin(nom)
    
    @staticmethod
    def searchmedecin(id: int):
        allmedecin = []
        result = DAOmedecin.getall(id)
        for i in result:
            # Assurez-vous que la classe `medecins` est correctement définie avec un constructeur approprié.
            # Vérifiez l'ordre des paramètres si l'ordre est i[0], i[1], i[3], i[2] dans le constructeur.
            Med = medecins(i[0], i[1], i[3], i[2],i[4],i[5])
            allmedecin.append(Med)
        return allmedecin


    
if __name__ == "__main__":

    #patient=patient(1,"nabil","kella","10/04/2003","nabil.kella@gmail.com","0000000","image.jpg","A",1.80,77,"Homme","adresse","000","oui","non","hemophile")
    #patientServices.addPatients(patient)
    #patientServices.deletePatients(1)
    #patientServices.ModifyPatients(patient.__name__,"000")
    #print(patientServices.LogIn)
    #print(patientServices.DecisinoPatient(1))
    #MedicamentService.ajouterMedicament(nom, Id_Patient,id_Medicament)
    #MedicamentService.ajouterMedicament("nom4",80,"2021-01-02","10:00:00",65)
    #MedicamentService.ajouterMedicament(medicament)
    #print(patientServices.LogOut("Email","123"))
    #print(patientServices.checkAge(patientServices.calculate_age(patientServices.patient_age1("2003-04-10"))))
    #patientServices.pasParJours(patientServices.calculate_age(patientServices.patient_age(nomutilisateur)))
    # print(patientServices.pasParJours(patientServices.calculate_age(patientServices.patient_age1("oth123"))))
    # print(patientServices.checkAge(patientServices.calculate_age("2020-05-28")))
    # print(patientServices.DecisinoPatient(23))
    # print(patientServices.lastPatient())
    # print(MedicamentService.allMedicament(63))
    # print(MedicamentService.searchMed('nom1',65))
    # medicament2=Medicament(0,"nom2",65,130,"2024-01-04","10")
    # DAOmedicament.newMedicament(medicament1)
    # MedicamentService.ajouterMedicament(medicament2)

    # poids=patientServices.patient_poid("q")
    # age=patientServices.calculate_age(patientServices.patient_age1("q"))
    # patientServices.generate_steps_plot(age,poids)
    # print(poids,age)
    # print(patientServices.pasParJours(14,19))
    # print(patientServices.checkPoids(patientServices.patient_poid("aze")))
    # medecinservices.addmedecins("nom","spe",91,"image")
    # print(medecinservices.searchmedecin(91)) 
    print(patientServices.get_patient_details(9)) 
     
