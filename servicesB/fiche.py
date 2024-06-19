from dal import DAOpatients, DAOmedicament, DAOmedecin
from models import Patients, Medicament, medecin
from datetime import datetime
from test import decision
import matplotlib.pyplot as plt

class patientServices:
    @staticmethod
    def addPatients(patients: Patients):
        return DAOpatients.newPatients(patients)
    
    @staticmethod
    def deletePatients(id: int):
        return DAOpatients.deletePatient(id)   
    
    @staticmethod
    def LogIn(nom: str, mdp: str):
        result = DAOpatients.logIn(nom, mdp)
        patient = Patients(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4], result[0][5], result[0][6], result[0][7], result[0][8], result[0][9], result[0][10], result[0][11], result[0][12], result[0][13], result[0][14])
        return patient
    
    @staticmethod 
    def ModifyPatients(nom: str, mdp: str):
        return DAOpatients.updatePatient(nom, mdp)

    @staticmethod
    def patient_age1(nom: str):
        result = DAOpatients.patient_age1(nom)
        return result[0]  # Adjusted assuming result returns a list with the date in the first position

    @staticmethod
    def search(patient_id: int):
        result = DAOpatients.getPatientById(patient_id)
        if result:
            patient = Patients(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4], result[0][5], result[0][6], result[0][7], result[0][8], result[0][9], result[0][10], result[0][11], result[0][12], result[0][13], result[0][14])
            return patient
        return None

    @staticmethod
    def calculate_age(birth_date: datetime):
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    @staticmethod
    def displayMedicalRecord(patient_id: int):
        patient = patientServices.search(patient_id)
        if not patient:
            return "Patient not found."

        age = patientServices.calculate_age(patient.date_naissance)
        medications = MedicamentService.allMedicament(patient_id)
        department = medecinservices.getDepartmentForPatient(patient_id)

        medical_record = f"Patient ID: {patient_id}\n"
        medical_record += f"Name: {patient.nom}\n"
        medical_record += f"Age: {age} years\n"
        medical_record += f"Weight: {patient.poids} kg\n"
        medical_record += f"Disease: {patient.maladie}\n"
        medical_record += "Medications:\n"

        for med in medications:
            medical_record += f"- {med.nom} (Dose: {med.dose}mg), Last taken: {med.date}\n"

        medical_record += f"Department overseeing care: {department}\n"

        return medical_record

if __name__ == "__main__":
    print(patientServices.displayMedicalRecord(1))
