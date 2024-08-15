from dal import DAOpatients, DAOmedicament, DAOmedecin
from models import patient, Medicament, medecin, medicamentPatients
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from dataclasses import dataclass
from datetime import datetime, date
from typing import List
import mysql.connector as mysql
from models import patient, Medicament, medecin, medicamentPatients, medecinPatient
from datetime import datetime
from dal import DAOpatients
from datetime import datetime

class patientServices:
    @staticmethod
    def get_appointement(config, medecinId, patientId, startDate, endDate):
        try:
            print(f"Tentative de recherche de rendez-vous: Medecin ID {medecinId}, Patient ID {patientId}")

            rendez_vous, error = DAOpatients.rendez_vous(config, medecinId, startDate, endDate)

            if error:
                return None, f"Tentative de recherche de rendez-vous: Medecin ID {medecinId}, Patient ID {patientId}: {error}"

            print(f"Fetched appointments: {rendez_vous}")

            for rdv in rendez_vous:
                print(f"Processing appointment: {rdv}")            
                if rdv.get('patientId') == str(patientId):
                
                    continue
                else:
                    rdv['description'] = ""

            return rendez_vous, None
        except Exception as e:
                print(f"Exception: {e}")
                return None, str(e)

    def FicheMedicale(config,patient_id):#
        try:    
            patient, e_patient = DAOpatients.fetch_patient_info_by_Id(config, patient_id)
            medicaments, _ =DAOpatients.fetch_medicaments_details_by_patient_id(config, patient_id)
            medecin, _ = DAOpatients.fetch_medecins_details_by_patient_id( config,patient_id)

            if not patient:
                return None, "No patient found with Id_Patient = " + str(patient_id) + ": " + str(e_patient)
            
            patient_info = {
                "patient": patient,
                "medicament": medicaments,
                "medecin": medecin
            }

            return patient_info, None
        except Exception as e:
            print(f"Exception: {e}")
            return None, str(e)
        
    @staticmethod
    def logIn(config ,username, password):
        try:
            print(f"Tentative de connexion pour l'utilisateur: {username}")
            patient, error = DAOpatients.logIn(config,username, password)
            if error:
                return None, "Tentative de connexion pour l'utilisateur: " + str(username) + ": " + str(error)
            
            return patient , None
        except Exception as e:
            print(f"Exception: {e}")
            return None, str(e)
######################

class medecinservices:
    @staticmethod

    def logInMedecin(config, username, password):
        try:
            print(f"Tentative de connexion pour l'utilisateur: {username}")
            medecin, error = DAOmedecin.logInMedecin(config, username, password)
            if error:
                return None, "Tentative de connexion pour l'utilisateur: " + str(username) + ": " + str(error)
            
            return medecin, None
        except Exception as e:
            print(f"Exception: {e}")
            return None, str(e)
""" @staticmethod
    def get_patient_byID(patient_id):#
        con = connect_db()
        if con is None:
            return None, "Connection to database failed"
        
        try:
            print(f"Recherche du patient avec l'ID : {patient_id}")  
            with con.cursor(dictionary=True) as cur:
                query = "SELECT * FROM patient WHERE Id_Patient = %s"
                cur.execute(query, (patient_id,))
                patient_data = cur.fetchone()
            
            con.close()

            if patient_data is None:
                print("Aucune donnée de patient trouvée.") 
                return None, "Aucun patient trouvé"
            print(f"Données du patient trouvées : {patient_data}")  
            return patient_data, None
        except Exception as e:
            print(f"Une erreur est survenue : {e}")  
            return None, str(e)
    

    @staticmethod
    def addPatients(patient):
        con = connect_db()
        if con is None:
            return None, "Connection to database failed"
        
        try:
            with con.cursor(dictionary=True) as cur:
                DAOpatients.AjouterPatientbyId(cur, con, patient)
            con.close()
            return patient, None
        except Exception as e:
            print(f"Exception: {e}")
            if con:
                con.close()
            return None, str(e)
    @staticmethod
    def deletePatients(id):
        con = connect_db()
        if con is None:
            return None, "Connection to database failed"
        
        try:
            with con.cursor(dictionary=True) as cur:
                DAOpatients.SupprimerPatientbyId(cur, con, id)
            return {"result": "success"}, None
        except Exception as e:
            return None, str(e)
        finally:
            con.close()
    @staticmethod
    def ModifierPatientByPassword(nom: str, mdp: str):
        con = connect_db()
        if con is None:
            return None, "Connection to database failed"
        
        try:
            with con.cursor() as cur:
                DAOpatients.ModifierPatientBymdp(cur, con, nom, mdp)
            return True, None
        except Exception as e:
            return None, str(e)
        finally:
            con.close()

    @staticmethod
    def patient_age1(date_naissance: str):
        from datetime import datetime
        con = connect_db()
        if con is None:
            return None, "Connection to database failed"
        
        with con.cursor(dictionary=True) as cur:
            try:
                # Recherche par DateNaissance
                cur.execute("SELECT DateNaissance FROM patient WHERE DateNaissance=%s", (date_naissance,))
                result = cur.fetchone()
                con.close()
                if result:
                    # Calculer l'âge à partir de la date de naissance
                    birth_date = datetime.strptime(result['DateNaissance'], '%Y-%m-%d')
                    age = (datetime.now() - birth_date).days // 365
                    return age, None
                return None, "Patient not found"
            except Exception as e:
                con.close()
                return None, str(e)
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
    def logIn(username, password):
        try:
            print(f"Tentative de connexion pour l'utilisateur: {username}")
            result = DAOpatients.logIn(cur, username, password)
            print(f"Résultat de la requête: {result}")
            if result:
                patient_data = result[0]
                patient_obj = patient(
                    patient_data[0], patient_data[1], patient_data[2], patient_data[3],
                    patient_data[4], patient_data[5], patient_data[6], patient_data[7],
                    patient_data[8], patient_data[9], patient_data[10], patient_data[11],
                    patient_data[12], patient_data[13], patient_data[14],patient_data[15],
                )
                return patient_obj, None
            else:
                return None, "Identifiants invalides"
        except Exception as e:
            print(f"Exception: {e}")
            return None, str(e)
    @staticmethod
    def LogOut_by_Email_Password(gmail: str, mdp: str):
        con = connect_db()
        if con is None:
            return None, "Connection to database failed"
        
        try:
            with con.cursor() as cur:  # Removed dictionary=True since psycopg2 does not support it
                result = DAOpatients.logOutByEmail_Passowrd(cur, gmail, mdp)
                if result:
                    patient_data = result[0]
                    patient = patient(
                        patient_data[0], patient_data[1], patient_data[2], patient_data[3],
                        patient_data[4], patient_data[5], patient_data[6], patient_data[7],
                        patient_data[8], patient_data[9], patient_data[10], patient_data[11],
                        patient_data[12], patient_data[13], patient_data[14]
                    )
                    return patient, None
                else:
                    return None, "No patient found with provided email and password"
        except Exception as e:
            return None, str(e)
        finally:
            con.close()

    @staticmethod
       
    def patient_age2(DateNaissance: str):
        con = connect_db()
        if con is None:
            return None, "Connection to database failed"
        
        with con.cursor(dictionary=True) as cur:
            result = DAOpatients.Get_Age_by_Date_Naissance(cur, DateNaissance)
            if result:
                # Directement utiliser result comme objet datetime.date
                birth_date = result
                age = (datetime.now().date() - birth_date).days // 365
                con.close()
                return age, None
            con.close()
            return None, "Patient not found"
    @staticmethod
    def patient_poid(id: int):
        con = connect_db()
        if con is None:
            return None, "Connection to database failed"
        
        with con.cursor(dictionary=True) as cur:
            result = DAOpatients.patient_poid_by_Id(cur, id)
            if result:
                con.close()
                return result[0]['Poids']  # Assuming 'Poids' is the column name
            con.close()
            return None, "Patient not found"
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
    
    try:
        with con.cursor(dictionary=True) as cur:
            result = DAOpatients.lastPatient_Id(cur)
            if result:
                patient_data = result[0]
                patient = patient(
                    patient_data['Id_Patient'], 
                    patient_data[' Nabil Example  '], 
                    patient_data['field2'], 
                    patient_data['field3'], 
                    patient_data['field4'], 
                    patient_data['field5'], 
                    patient_data['field6'], 
                    patient_data['field7'], 
                    patient_data['field8'], 
                    patient_data['field9'], 
                    patient_data['field10'], 
                    patient_data['field11'], 
                    patient_data['field12'], 
                    patient_data['field13'], 
                    patient_data['field14']
                )
                return patient, None
            return None, "No patient found"
    except Exception as e:
        return None, str(e)
    finally:
        if con:
            con.close()


    
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
                med = Medicament(*i)
                allmedicaments.append(med)
        con.close()
        return allmedicaments

    @staticmethod
    def ajouterMedicament(medi):
        con = connect_db()
        if con is None:
            return None, "Connection to database failed"
    
        try:
            with con.cursor(dictionary=True) as cur:
                DAOmedicament.Ajouter_Medicament(cur, con, medi)
                return "Medicament added successfully", None
        except Exception as e:
            return None, str(e)
        finally:
            if con:
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
        
        try:
            with con.cursor(dictionary=True) as cur:
                result = DAOmedicament.search_Medicament_by_Id(cur, nom, idPatient)
                if result:
                    med = Medicament(result[0]['id_Medicament'], result[0][' nom_medicament'], result[0]['Id_Patient'])
                    return med, None
                return None, "No medicament found"
        except Exception as e:
            return None, f"Error fetching medicament: {e}"
        finally:
            con.close()
    

class medecinservices:
    @staticmethod
    def addMedecins(nom: str, spe: str, id: int, image: str, numero_urgence: str):
        con = connect_db()
        if con is None:
            return None, "Connection to database failed"
    
        try:
            with con.cursor(dictionary=True) as cur:
                DAOmedecin.Ajouter_medecin(cur, con, nom, spe, id, image)
            con.close()
            return True, "Médecin ajouté avec succès"
        except Exception as e:
            return None, f"Une erreur est survenue : {str(e)}"
    @staticmethod
    def deletemed(id: int):
        con = connect_db()
        if con is None:
            return None, "Connection to database failed"
        
        with con.cursor(dictionary=True) as cur:
            DAOmedecin.deletemed(cur, con, id)
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
                Med = medecins(i[0], i[1], i[3], i[2],i[3])
                allmedecin.append(Med)
        con.close()
        return allmedecin
    """

if __name__ == "__main__":
   
        ######################
    """medecin_nom = "Dr. saraqasmi"
    medecin_spe = "Cardiology"
    medecin_id = 11
    medecin_image = "image_path.jpg"
    medecin_numero_urgence="numero_urgence"


    # Run the test
    result, message = medecinservices.addMedecins(medecin_nom, medecin_spe, medecin_id, medecin_image,medecin_numero_urgence)
    if result is None:
        print(f"Test failed: {message}")
    else:
        print("Test passed: Medecin added successfully")"""
    #les test Patient
    """ new_patient = patient(
        Id_Patient=12222,
        NomUtilisateur="nabil123",
        Nomcomplet="Nabil Example",
        DateNaissance="1990-01-01",
        Email="nabil@example.com",
        Telephone="1234567890",
        Adresse="123 Main St",
        Motdepasse="password123",
        image=None,
        Groupesanguin="O+",
        Taille="180cm",
        Poids="75kg",
        Sexe="M",
        AntecedentMere="Diabetes",
        AntecedentPere="Hypertension",
        TypeDeMaladie="Hemophilia"
    )
    patient_info, error = patientServices.addPatients(new_patient)
    if error:
        print("Erreur :", error)
    else:
        print("Patient ajouté avec succès :", patient_info.__dict__)"""
    """conn = connect_db()
    if not conn:
        print("Échec de la connexion à la base de données.")
    else:
        cur = conn.cursor()

        username = "nabil123"
        password = "password123"

        patient, error = patientServices.logIn(cur, username, password)
        if error:
            print(f"Erreur : {error}")
        elif patient:
            print(f"Connexion réussie pour le patient : {patient.data}")
        else:
            print("Échec de connexion : Identifiants invalides")

        cur.close()
        conn.close()
    """
    """medicament_a_chercher = "hemophil"
    id_patient = 1

    result, error = MedicamentService.searchMedicament_by_Id(medicament_a_chercher, id_patient)
    if error:
        print(f"Error: {error}")
    else:
        print(f"Result: {result.to_dict()}")"""
    """patient, error = lastPatient_byID()
    if error:
        print(f"Error: {error}")
    else:
        print(f"Last patient: {patient}")"""
    """patient_id = 1  # Remplacez par l'ID du patient que vous souhaitez rechercher

    result = patientServices.get_patient_byID(patient_id)

    if result is None:
        print("Erreur : La fonction a retourné None")
    else:
        patient_data, error = result
        if error:
            print(f"Erreur : {error}")
        else:
            print(f"Données du patient : {patient_data}")
"""
    
    """gmail = "nabil.qasmi1@gmail.com"
    mdp = "nabil123"

    patient, error = patientServices.LogOut_by_Email_Password(gmail, mdp)
    if error:
        print(f"Erreur : {error}")
    elif patient:
        print(f"Déconnexion réussie pour le patient : {patient}")
    else:
        print("Déconnexion échouée : Email ou mot de passe incorrect")"""
    """nom_utilisateur = "exempleNomUtilisateur"
    nouveau_mdp = "nouveauMotDePasse"

    success, error = patientServices.ModifierPatientByPassword(nom_utilisateur, nouveau_mdp)
    if error:
        print(f"Erreur : {error}")
    elif success:
        print("modifié avec succès")
    else:
        print("Modification  échouée")
    """
    
    
    """conn = connect_db()
    if not conn:
        print("Échec de la connexion à la base de données.")
    else:
        cur = conn.cursor()

        username = "exempleNomUtilisateur"
        password = "exempleMotDePasse"

        patient, error = patientServices.logIn(cur, username, password)
        if error:
            print(f"Erreur : {error}")
        elif patient:
            print(f"Connexion réussie pour le patient : {patient}")
        else:
            print("Échec de connexion : Identifiants invalides")

        cur.close()
        conn.close()
    
    """""""""""
    """ patient_info, error = patientServices.addPatients(patient)
    print("patient ajouter par succes:",patient_info)
    print("Erreur :", error)
    """
""" patient_info, error = patientServices.FicheMedicale(9)
    print("Informations du patient :", patient_info)
    print("Erreur :", error)"""
  