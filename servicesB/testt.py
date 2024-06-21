from dataclasses import dataclass
from dal import DAOpatients, DAOmedicament, DAOmedecin
from datetime import datetime
import matplotlib.pyplot as plt

@dataclass
class Patients:
    id: int
    nomutilisateur: str
    Nomcomplet: str
    Date_Naissance: str
    email: str
    num_tel: str
    adresse: str
    mdp: str
    image: str
    GR_S: str
    taille: str
    poids: str
    sexe: str
    antecedant_mere: str
    antecedant_pere: str

    def to_dict(self):
        return {
            "id": self.id,
            "nomutilisateur": self.nomutilisateur,
            "Nomcomplet": self.Nomcomplet,
            "Date_Naissance": self.Date_Naissance,
            "email": self.email,
            "num_tel": self.num_tel,
            "adresse": self.adresse,
            "mdp": self.mdp,
            "image": self.image,
            "GR_S": self.GR_S,
            "taille": self.taille,
            "poids": self.poids,
            "sexe": self.sexe,
            "antecedant_mere": self.antecedant_mere,
            "antecedant_pere": self.antecedant_pere
        }

@dataclass
class Medicament:
    id: int
    nom: str
    idPatient: int
    dose: int
    Date: str
    time: str

@dataclass
class medecin:
    nom: str
    specialite: str
    image: str
    IdP: int

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
        weight = patient.poids
        blood_group = patient.GR_S
        medications = MedicamentService.allMedicament(patient.id)
        
        medical_record = f"Fiche Médicale pour {patient.Nomcomplet}\n{'='*30}\n"
        medical_record += f"Age: {age} ans\n"
        medical_record += f"Poids: {weight} kg\n"
        medical_record += f"Groupe sanguin: {blood_group}\n"
        medical_record += f"Sexe: {patient.sexe}\n"
        medical_record += f"Antécédent Mère: {patient.antecedant_mere}\n"
        medical_record += f"Antécédent Père: {patient.antecedant_pere}\n"
        medical_record += f"\nListe des Médicaments:\n{'-'*30}\n"
        for med in medications:
            medical_record += f"Nom: {med.nom}\nDose: {med.dose} UI\nDate de prise: {med.Date}\nHeure de prise: {med.time}\n{'-'*30}\n"
        
        return medical_record

    @staticmethod
    def addPatients(patients: Patients):
        return DAOpatients.newPatients(patients)
    
    @staticmethod
    def deletePatients(id: int):
        return DAOpatients.deletePatient(id)
    
    @staticmethod
    def LogIn(nom: str, mdp: str):
        result = DAOpatients.logIn(nom, mdp)
        patient = Patients(*result[0])
        return patient
    
    @staticmethod 
    def ModifyPatients(nom: str, mdp: str):
        return DAOpatients.updatePatient(nom, mdp)
    
    @staticmethod
    def patient_age1(nom: str):
        result = DAOpatients.patient_age1(nom)
        date_naissance = result
        return date_naissance

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
        patient = Patients(*result[0])
        return patient

    @staticmethod
    def patient_age2(DateNaissance: str):
        result = DAOpatients.patient_age2(DateNaissance)
        return result

    @staticmethod
    def DecisinoPatient(id: int):
        return decision(id)
    
    @staticmethod 
    def search(id: int):
        return DAOpatients.search(id)
    
    @staticmethod
    def lastPatient():
        result = DAOpatients.lastPatient()
        patient = Patients(*result[0])
        return patient
    
    @staticmethod
    def patient_poid(nom: str):
        result = DAOpatients.patient_poid(nom)
        for i in result:
            return i[0]
        
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
            med = Medicament(i[0], i[1], i[2], i[3], i[4], i[5])
            allmedicaments.append(med)
        return allmedicaments
    
    @staticmethod
    def ajouterMedicament(medi: Medicament):
        return DAOmedicament.newMedicament(medi)
       
    @staticmethod
    def deletemedicament(medi: Medicament):
        return DAOmedicament.deletemedicament(medi)   
    
    @staticmethod
    def searchMed(nom: str, idPatient: int):
        result = DAOmedicament.search(nom, idPatient)
        med = Medicament(*result[0])
        return med 


class medecinservices:
    @staticmethod
    def addmedecins(nom: str, spe: str, id: int, image: str):
        return DAOmedecin.newMeddin(nom, spe, id, image)

    @staticmethod
    def deletemed(nom: str):
        return DAOmedecin.deletemedecin(nom)
    
    @staticmethod
    def searchmedecin(id: int):
        allmedecin = []
        result = DAOmedecin.getall(id)
        for i in result:
            Med = medecin(i[0], i[1], i[3], i[2])
            allmedecin.append(Med)
        return allmedecin


if __name__ == "__main__":
    # Example usage of fiche_medicale
    print(patientServices.fiche_medicale("q"))
