import mysql.connector as mysql
from models import medicamentPatients,medecinService,medecin,medicament,Patient
def connect_db():
    try:
        con = mysql.connect(
            host="34.122.67.28",
            user='root',
            passwd='nabil123!',
            database='hemophelie',
            port=3306,
            charset="utf8mb4"
        )
        return con
    except mysql.Error as e:
        print(f"Error connecting to MySQL Platform: {e}")
        return None
def fetch_patient_info(con, patient_name):
    cursor = con.cursor(dictionary=True)
    query = "SELECT * FROM Patient WHERE Nomcomplet LIKE %s"
    cursor.execute(query, (f"%{patient_name}%",))
    patient_data = cursor.fetchall()
    print("Raw Data from DB:", patient_data)  # Ajouter pour déboguer
    return [Patient(**data) for data in patient_data]

def fetch_medicaments_for_patient(con, patient_id):
    cursor = con.cursor(dictionary=True)
    query = "SELECT * FROM medicament WHERE Id = %s"
    cursor.execute(query, (patient_id,))
    medicament_data = cursor.fetchall()
    return [medicament(**data) for data in medicament_data]

def fetch_medicament_patient_details(con, patient_id):
    cursor = con.cursor(dictionary=True)
    query = "SELECT * FROM medicamentPatients WHERE Id = %s"
    cursor.execute(query, (patient_id,))
    details = cursor.fetchall()
    return [medicamentPatients(**data) for data in details]

def print_patient_details(patient_name):
    con = connect_db()
    if con is None:
        return
    
    patients = fetch_patient_info(con, patient_name)
    for patient in patients:
        print(f"Patient: {patient.Nomcomplet}, Email: {patient.Email}")
        medicaments = fetch_medicaments_for_patient(con, patient.Id)
        print("Medicaments:")
        for med in medicaments:
            print(f"- {med.nom}")

        med_patients_details = fetch_medicament_patient_details(con, patient.Id)
        print("Details de Prise de Medicaments:")
        for detail in med_patients_details:
            print(f"- Dose: {detail.dose}, Dernière Prise: {detail.derniere_date_de_prise}")

    con.close()
if __name__ == "__main__":
# Exemple d'utilisation
    print_patient_details("Qnabil")
