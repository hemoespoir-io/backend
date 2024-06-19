import mysql.connector
from datetime import datetime

def get_database_connection():
    return mysql.connector.connect(
        host='34.122.67.28',
        user='root',
        password='nabil123!',
        database='hemophelie'
    )

class Patient:
    def __init__(self, id, username, full_name, dob, email, phone, address, password, image, blood_group, height, weight, gender, mother_history, father_history, disease_type):
        self.id = id
        self.username = username
        self.full_name = full_name
        self.dob = datetime.strptime(dob, '%Y-%m-%d').date() if isinstance(dob, str) else dob
        self.email = email
        self.phone = phone
        self.address = address
        self.password = password
        self.image = image
        self.blood_group = blood_group
        self.height = height
        self.weight = weight
        self.gender = gender
        self.mother_history = mother_history
        self.father_history = father_history
        self.disease_type = disease_type  # Assume a new field for disease type

class Medicament:
    def __init__(self, idM, nom, patient_id, dose_recommandee, dernier_date_de_prise, time):
        self.idM = idM
        self.nom = nom
        self.patient_id = patient_id
        self.dose_recommandee = dose_recommandee
        self.dernier_date_de_prise = dernier_date_de_prise
        self.time = time

class PatientServices:
    @staticmethod
    def get_patient_by_username(username):
        conn = get_database_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Patient WHERE username = %s"
        cursor.execute(query, (username,))
        row = cursor.fetchone()
        if row:
            return Patient(*row)
        cursor.close()
        conn.close()
        return None

    @staticmethod
    def get_all_medicaments_for_patient(patient_id):
        conn = get_database_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Medicament WHERE patient_id = %s"
        cursor.execute(query, (patient_id,))
        rows = cursor.fetchall()
        medicaments = [Medicament(*row) for row in rows]
        cursor.close()
        conn.close()
        return medicaments

    @staticmethod
    def calculate_age(birth_date):
        today = datetime.today().date()
        return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    @staticmethod
    def generate_medical_record(username):
        patient = PatientServices.get_patient_by_username(username)
        if not patient:
            return "Patient not found"
        age = PatientServices.calculate_age(patient.dob)
        medications = PatientServices.get_all_medicaments_for_patient(patient.id)
        medical_record = f"Fiche Médicale pour {patient.full_name}\n"
        medical_record += f"{'='*30}\nAge: {age} ans\nType de maladie: {patient.disease_type}\nPoids: {patient.weight} kg\n"
        medical_record += "Liste des Médicaments:\n" + '-'*30 + "\n"
        for med in medications:
            medical_record += f"Nom: {med.nom}, Dose recommandée: {med.dose_recommandee}, Dernière prise: {med.dernier_date_de_prise} à {med.time}\n"
        return medical_record

if __name__ == "__main__":
    username = input("Enter the username to fetch medical record: ")
    print(PatientServices.generate_medical_record(username))
