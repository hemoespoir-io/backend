from datetime import datetime
import matplotlib.pyplot as plt
from dataclasses import dataclass

# Import your DAOs and models
from dal import DAOpatients, DAOmedicament, DAOmedecin
from models import Patient, medicament, medecin

class PatientService:
    @staticmethod
    def get_patient_by_username(username: str) -> Patient:
        result = DAOpatients.get_patient_by_username(username)
        return Patient(*result[0]) if result else None

    @staticmethod
    def calculate_age(birth_date: str) -> int:
        birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
        today = datetime.today()
        return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    @staticmethod
    def add_patient(patient: Patient):
        return DAOpatients.newPatients(patient)

    @staticmethod
    def delete_patient(patient_id: int):
        return DAOpatients.deletePatient(patient_id)

    @staticmethod
    def log_in(username: str, password: str) -> Patient:
        result = DAOpatients.logIn(username, password)
        return Patient(*result[0])

    @staticmethod
    def update_patient(username: str, password: str):
        return DAOpatients.updatePatient(username, password)

    @staticmethod
    def get_patient_age(username: str) -> datetime:
        return DAOpatients.patient_age1(username)

    @staticmethod
    def check_age(age: int) -> bool:
        return 3 < age < 101

    @staticmethod
    def check_weight(weight: int) -> bool:
        return weight > 0

    @staticmethod
    def log_out(email: str, password: str) -> Patient:
        result = DAOpatients.logOut(email, password)
        return Patient(*result[0])

    @staticmethod
    def generate_steps_plot(age: int, weight: int):
        steps_data = PatientService.pas_par_jours(age, weight)
        days = list(steps_data.keys())
        steps = list(steps_data.values())

        plt.figure(figsize=(12, 7))
        if "Anomaly" in steps_data:
            plt.text(0.5, 0.5, steps_data["Anomaly"], horizontalalignment='center', verticalalignment='center', fontsize=15, color='red', transform=plt.gca().transAxes)
            plt.axis('off')
        else:
            plt.bar(days, steps, color='royalblue', edgecolor='black')
            plt.title(f'Steps per day for a {age}-year-old weighing {weight} kg', fontsize=15)
            plt.xlabel('Day of the Week', fontsize=12)
            plt.ylabel('Steps', fontsize=12)
            plt.xticks(rotation=45)
            plt.yticks()
            plt.grid(True)
            plt.tight_layout()
        plt.show()

    @staticmethod
    def pas_par_jours(age: int, weight: int) -> dict:
        if weight < 20 or weight >= 100:
            return {"Anomaly": "Please consult a doctor immediately"}
        
        steps_chart = {
            (3, 5): [50, 40, 30, 40, 20, 10, 30],
            (6, 10): [10000, 11000, 14000, 9000, 10000, 13000, 11000],
            (11, 20): [10000, 11000, 11500, 12000, 11000, 12000, 13000],
            (21, 60): [7000, 9000, 10000, 8500, 7500, 9500, 10000],
            (61, 70): [8000, 7500, 6500, 6000, 7900, 6800, 8200],
            (71, 80): [3000, 3000, 3000, 3000, 3000, 3000, 3000],
            (81, 100): [100, 80, 60, 70, 20, 60, 40]
        }

        for (low, high), steps in steps_chart.items():
            if low <= age <= high:
                days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
                if 90 < weight < 100:
                    steps = [step * 0.5 for step in steps]
                return dict(zip(days, steps))
        
        return {}
class MedicamentService:
    @staticmethod
    def all_medicaments(patient_id: int) -> list:
        results = DAOmedicament.allMedicament(patient_id)
        return [medicament(*result) for result in results]

    @staticmethod
    def add_medicament(medicament: medicament):
        return DAOmedicament.newMedicament(medicament)

    @staticmethod
    def delete_medicament(medicament: medicament):
        return DAOmedicament.deletemedicament(medicament)

    @staticmethod
    def search_medicament(name: str, patient_id: int) -> medicament:
        result = DAOmedicament.search(name, patient_id)
        return medicament(*result[0])

class MedecinService:
    @staticmethod
    def add_medecin(name: str, specialty: str, id: int, image: str):
        return DAOmedecin.newMeddin(name, specialty, id, image)

    @staticmethod
    def delete_medecin(name: str):
        return DAOmedecin.deletemedecin(name)

    @staticmethod
    def search_medecin(id: int) -> list:
        results = DAOmedecin.getall(id)
        return [ medecin(*result) for result in results]

# Example usage
if __name__ == "__main__":
    # Example operations
    print(MedecinService.search_medecin(91))
    pass