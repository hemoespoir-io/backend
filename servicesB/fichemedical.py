import mysql.connector as mysql
from models import medicamentPatients, medecins, medicament, patient

def connect_db():
    try:
        con = mysql.connect(
            host="34.122.67.28",
            user='root',
            passwd='nabil123!',
            database='pfe',
            port=3306,
            charset="utf8mb4"
        )
        print("Connection to the database was successful.")
        return con
    except mysql.Error as e:
        print(f"Error connecting to MySQL Platform: {e}")
        return None

def fetch_patient_info(con, patient_name):
    cursor = con.cursor(dictionary=True)
    query = "SELECT Id_Patient, NomUtilisateur, Nomcomplet, DateNaissance, Email, Telephone, Adresse, Motdepasse, image, Groupesanguin, Taille, Poids, Sexe, AntecedentMere, AntecedentPere, TypeDeMaladie FROM patient WHERE Nomcomplet LIKE %s"
    print(f"Executing query: {query} with patient_name: {patient_name}")
    cursor.execute(query, (f"%{patient_name}%",))
    patient_data = cursor.fetchall()
    print("Raw Data from DB:", patient_data)
    return [patient(**data) for data in patient_data]

def fetch_medicaments_and_details_for_patient(con, Id_Patient):
    cursor = con.cursor(dictionary=True)
    query = """
    SELECT m.nom, mp.dose, mp.derniere_date_de_prise
    FROM medicament m
    JOIN medicamentPatients mp ON m.id_Medicament = mp.id_Medicament
    WHERE mp.Id_Patient = %s
    """
    print(f"Executing query: {query} with Id_Patient: {Id_Patient}")
    cursor.execute(query, (Id_Patient,))
    combined_data = cursor.fetchall()
    print("Medicaments and details from DB:", combined_data)
    return combined_data

def print_patient_details(patient_name):
    con = connect_db()
    if con is None:
        return
    
    patients = fetch_patient_info(con, Id_Patient)
    if not patients:
        print(f"No patients found with name like: {Patient_id}")
        return

    for patient in patients:
        print(f"Patient: {patient.Nomcomplet}, Email: {patient.Email}")
        medicaments_details = fetch_medicaments_and_details_for_patient(con, patient.Id_Patient)
        if not medicaments_details:
            print("Aucun médicament trouvé pour ce patient.")
        else:
            print("Medicaments et détails:")
            for med in medicaments_details:
                print(f"- Médicament: {med['nom']}, Dose: {med['dose']}, Dernière prise: {med['derniere_date_de_prise']}")
    
    con.close()

if __name__ == "__main__":
    # Exemple d'utilisation
    print_patient_details("122")
