import mysql.connector
from datetime import datetime, date

def get_database_connection():
    connection = mysql.connector.connect(
        host='34.122.67.28',
        user='root',
        password='nabil123!',
        database='hemophelie'
    )
    return connection

class Patients:
    def __init__(self, id, username, full_name, dob, email, phone, address, password, image, blood_group, height, weight, gender, mother_history, father_history):
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

class Medicament:
    def __init__(self, idM, nom, patient_id, dose_recommandee, dernier_date_de_prise, time):
        self.idM = idM
        self.nom = nom
        self.patient_id = patient_id
        self.dose_recommandee = dose_recommandee
        self.dernier_date_de_prise = dernier_date_de_prise
        self.time = time

class patientServices:
    @staticmethod
    def get_patient_by_username(username):
        conn = get_database_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Patient WHERE NomUtilisateur = %s"
        print("Executing query:", query, "with username:", username)  # Debug output
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        if result:
            print("Query result:", result)  # Debug output
            return Patients(*result)
        else:
            print("No results found for username:", username)  # Debug output
        cursor.close()
        conn.close()
        return None

    @staticmethod
    def calculate_age(birth_date):
        if isinstance(birth_date, str):
            birth_date = datetime.strptime(birth_date, '%Y-%m-%d').date()
        elif not isinstance(birth_date, date):
            raise TypeError("birth_date must be either a string formatted as '%Y-%m-%d' or a datetime.date object")
        today = date.today()
        return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    @staticmethod
    def fiche_medicale(username):
        patient = patientServices.get_patient_by_username(username)
        if patient is None:
            return "Patient not found"
        age = patientServices.calculate_age(patient.dob)
        medications = MedicamentService.get_all_medicaments_for_patient(patient.id)
        medical_record = f"Fiche Médicale pour {patient.full_name}\n"
        medical_record += f"{'='*30}\n"
        medical_record += f"Age: {age} ans\n"
        medical_record += f"Poids: {patient.weight} kg\n"
        medical_record += f"Groupesanguin: {patient.blood_group}\n"
        medical_record += f"\nListe des Médicaments:\n"
        medical_record += f"{'-'*30}\n"
        for med in medications:
            medical_record += f"Nom: {med.nom}\n"
            medical_record += f"Dose recommandée: {med.dose_recommandee}\n"
            medical_record += f"Dernière date de prise: {med.dernier_date_de_prise}\n"
            medical_record += f"Heure de la dernière prise: {med.time}\n"
            medical_record += f"{'-'*30}\n"
        return medical_record

class MedicamentService:
    @staticmethod
    def get_all_medicaments_for_patient(patient_id):
        try:
            conn = get_database_connection()
            cursor = conn.cursor()
            query = "SELECT idM, nom, Id, dose_recommandee, dernier_date_de_prise, time FROM medicament WHERE Id = %s"
            cursor.execute(query, (patient_id,))
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            if results:
                medications = [Medicament(*result) for result in results]
                return medications
            else:
                print(f"No medications found for patient ID {patient_id}")
                return []
        except Exception as e:
            print("Error:", e)
            return []

if __name__ == "__main__":
    username = input("Enter the username to fetch medical record: ")
    print(patientServices.fiche_medicale(username))
