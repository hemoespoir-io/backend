import mysql.connector as mysql
from mysql.connector import Error
#from Analyse_de_donnes.testt import Medicament
from models import patient, Medicament,medecin,medicamentPatients,medecinPatient


def connect_db(config):
    try:
        con = mysql.connect(
            host=config['DB_HOST'],
            user=config['DB_USER'],
            passwd=config['DB_PASSWD'],
            database=config['DB_DATABASE'],
            port='3306',
            charset="utf8"
        )
        return con, None
    except mysql.Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None, e


class DAOpatients:
  
   
     ##
    
    @staticmethod
    def logIn( config ,username, password):
        con, error = connect_db(config)
        if con is None:
            return None, "Connection to database failed: %s" % (error)
        
        try:
            with con.cursor(dictionary=True) as cur:
                query = "SELECT p.*, mp.medecinId FROM patient p INNER JOIN medecinpatient mp ON p.Id_Patient = mp.patientId WHERE p.NomUtilisateur = %s AND p.Motdepasse = %s;"
                cur.execute(query, (username, password))
                patient=cur.fetchall()
                con.close()
                return patient, None
        
        except Exception as e:
            print(f"Exception: {e}")
            return None, str(e)
        finally:
            con.close()
    @staticmethod
    def get_rendez_vous(config, medecinId, date, startHour, endHour):
        print("get RDV")
        con, error = connect_db(config)
        if con is None:
            return None, "Connection to database failed: %s" % (error)

        try:
            with con.cursor(dictionary=True) as cur:
                check_query = """ 
                SELECT * FROM rendez_vous 
                WHERE medecinId = %s AND date = %s 
                AND heure BETWEEN %s AND %s;
                """
                cur.execute(check_query, (medecinId, date, startHour, endHour))
                rendez_vous = cur.fetchone()

                print(rendez_vous)
                return rendez_vous, None
        except Exception as e:
            print(f"Exception: {e}")
            raise e
        finally:
            if con:
                con.close()
    @staticmethod
    def add_rendez_vous(config, medecinId, patientId, date, heure, description, duree):
        print("add RDV")
        con, error = connect_db(config)
        if con is None:
            return None, "Connection to database failed: %s" % (error)

        try:
            with con.cursor(dictionary=True) as cur:
               
                query = """ 
                     INSERT INTO rendez_vous (medecinId, patientId, date, heure, duree, description)
                    VALUES (%s, %s, %s, %s, %s, %s);
                    """
                cur.execute(query, (medecinId, patientId, date, heure, duree, description))
                _ = cur.fetchone()

        except Exception as e:
            print(f"Exception: {e}")
            raise e

        finally:
            if con:
                con.close() 
    
    @staticmethod
    def delete_rendez_vous(config, medecinId, patientId, date):
        print("Deleting RDV")
    
    # Connexion à la base de données
        con, error = connect_db(config)
        if con is None:
            return None, "Connection to database failed: %s" % (error)

        try:
        # Exécution de la requête SQL avec un curseur contextuel
            with con.cursor(dictionary=True) as cur:
                query = """ 
                DELETE FROM rendez_vous
                WHERE medecinId = %s 
                AND patientId = %s 
                AND date = %s;
                """
                cur.execute(query, (medecinId, patientId, date))
            
            # Confirmation des modifications
                con.commit()

            # Vérification du nombre de lignes affectées
                if cur.rowcount == 0:
                    return None, "Aucun enregistrement trouvé pour suppression"
                
                return "Suppression réussie", None

        except Exception as e:
        # En cas d'exception, retour en arrière de la transaction
            con.rollback()
            print(f"Exception: {e}")
            return None, str(e)

        finally:
        # Fermeture de la connexion à la base de données
            if con:
                con.close()        
    @staticmethod
    def fetch_patient_info_by_Id(config, patient_id):
        con, error = connect_db(config)
        if con is None:
            return None, "Connection to database failed %s" % (error)
        
        try:
            with con.cursor(dictionary=True) as cur:
                query = "SELECT * FROM patient WHERE Id_Patient = %s"
                cur.execute(query, (patient_id,))
                patient = cur.fetchall()
                return patient, None
        except Exception as e:
            return None, str(e)
        finally:
            con.close()
    
    ##
    @staticmethod
    def fetch_medecins_details_by_patient_id(config, Id_Patient):
        con, error = connect_db(config)
        if con is None:
            return None, "Connection to database failed %s" % (error)

        try:
            with con.cursor(dictionary=True) as cur:
                query = """
                    SELECT *
                    FROM medecinPatient mp
                    INNER JOIN medecin m ON mp.medecinId = m.Id_Medecin
                    WHERE mp.patientId = %s
                """
                cur.execute(query, (Id_Patient,))
                medecin = cur.fetchall()
                return medecin, None
        except Exception as e:
            return None, str(e)
        finally:
            con.close()
    
    
    @staticmethod
    def fetch_medicaments_details_by_patient_id(config, Id_Patient):
        con = connect_db(config)
        con, error = connect_db(config)
        if con is None:
            return None, "Connection to database failed %s" % (error)

        try:
            with con.cursor(dictionary=True) as cur:
                query = """
                    SELECT m.nom_medicament, mp.dose, mp.derniere_date_de_prise
                    FROM medicament m
                    JOIN medicamentPatients mp ON m.id_Medicament = mp.id_Medicament
                    WHERE mp.Id_Patient = %s
                """
                cur.execute(query, (Id_Patient,))
                medicaments = cur.fetchall()
                return medicaments, None
        except Exception as e:
            return None, str(e)
        finally:
            con.close()





            
    @staticmethod
    def AjouterPatientbyId(cur, con, patient):
        cur.execute('INSERT INTO patient (Id_Patient, NomUtilisateur, Nomcomplet, DateNaissance, Email, Telephone, Adresse, Motdepasse, image, Groupesanguin, Taille, Poids, Sexe, AntecedentMere,  TypeDeMaladie) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                    (patient.Id_Patient, patient.NomUtilisateur, patient.Nomcomplet, patient.DateNaissance, patient.Email, patient.Telephone, patient.Adresse, patient.Motdepasse, patient.image, patient.Groupesanguin, patient.Taille, patient.Poids, patient.Sexe, patient.AntecedentMere, patient.TypeDeMaladie))
        con.commit()

    @staticmethod
     
    def SupprimerPatientbyId(cur, con, id):
        try:
            # Démarrer une transaction
            cur.execute("START TRANSACTION;")
            
            # Supprimer d'abord de la table medecinPatient
            cur.execute("""
                DELETE medecinPatient 
                FROM medecinPatient 
                JOIN patient ON medecinPatient.patientId = patient.Id_Patient
                WHERE patient.Id_Patient = %s
            """, (id,))
            
            # Ensuite, supprimer de la table patient
            cur.execute("DELETE FROM patient WHERE Id_Patient = %s;", (id,))
            
            # Valider la transaction
            con.commit()
        except Exception as e:
            # En cas d'erreur, annuler la transaction
            con.rollback()
            raise e
    @staticmethod
    def ModifierPatientBymdp(cur, con, NomUtilisateur: str, mdp: str):
        cur.execute("UPDATE patient SET Motdepasse = %s WHERE NomUtilisateur = %s", (mdp, NomUtilisateur))
        con.commit()

    @staticmethod
    def patient_poid_by_Id(cur, id: int):
        cur.execute("SELECT Poids FROM patient WHERE Id_Patient=%s", (id,))
        result = cur.fetchall()
        if result:
            return result[0]
        else:
            return None
   

    @staticmethod
    def logOutByEmail_Passowrd(cur, gmail: str, mdp: str):
        query = "SELECT * FROM patient WHERE Email=%s AND Motdepasse=%s"
        cur.execute(query, (gmail, mdp))
        result = cur.fetchall()
        return result

    @staticmethod
    def search_by_Id(cur, id: int):
        cur.execute("SELECT * FROM patient WHERE Id_Patient=%s", (id,))
        result = cur.fetchall()
        return result
    @staticmethod
    def get_patient_by_Id(cur, Id_patient: int):
        query = "SELECT * FROM patient WHERE Id_Patient = %s"
        cur.execute(query, (Id_patient,))
        result = cur.fetchall()
        return result
    

    @staticmethod
    def Get_Age_by_Date_Naissance(cur, dataNaissance: str):
        cur.execute("SELECT DateNaissance FROM patient WHERE DateNaissance=%s", (dataNaissance,))
        result = cur.fetchall()
        if result:
            return result[0]['DateNaissance']
        else:
            return None
    @staticmethod
    def lastPatient_Id(cur):
        cur.execute("SELECT * FROM patient ORDER BY Id_Patient DESC LIMIT 1")
        result = cur.fetchall()
        return result
   
    """@staticmethod
    def fetch__details_by_patient_id( Id_Patient):
        con = connect_db(config)
        if con is None:
            return None, "Connection to database failed"

        with con.cursor(dictionary=True) as cur:
            query =""" """
                SELECT m.nom_medicament, mp.dose, mp.derniere_date_de_prise
                FROM medicament m
                JOIN medicamentPatients mp ON m.id_Medicament = mp.id_Medicament
                WHERE mp.Id_Patient = %s
            """
"""cur.execute(query, (Id_Patient,))
            medicaments=cur.fetchall()
            con.close()
            return medicaments
        con.close()"""

class DAOmedicament:
    @staticmethod

    def Ajouter_Medicament(cur, con, medi):
        cur.execute('INSERT INTO medicament (nom_medicament, Id_Patient, id_Medicament) VALUES (%s, %s, %s)',
                    (medi.nom_medicament, medi.Id_Patient, medi.id_Medicament))
        con.commit()

    @staticmethod
    def deletemedicament_by_Id(cur, con, medi: Medicament):
        try:
            cur.execute("DELETE FROM medicament WHERE id_Medicament=%s", (medi.id_Medicament,))
            con.commit()
        except Exception as e:
            con.rollback()
            raise e

    @staticmethod
     
    def search_Medicament_by_Id(cur, nom: str, idPatient: int):
        try:
            cur.execute("SELECT * FROM Medicament WHERE  nom_medicament=%s AND Id_Patient=%s", (nom, idPatient))
            result = cur.fetchall()
            return result
        except Exception as e:
            print(f"Error executing query: {e}")
            return None
    @staticmethod
    def Medicament_details_byID(cur, id: int):
        cur.execute("SELECT * FROM medicament WHERE id_Medicament=%s", (id,))
        result = cur.fetchall()
        return result


class DAOmedecin:
    @staticmethod
    #login medecin 
    def logInMedecin( config ,username, password):
        con, error = connect_db(config)
        if con is None:
            return None, "Connection to database failed: %s" % (error)
        
        try:
            with con.cursor(dictionary=True) as cur:
                query = "SELECT * FROM medecin WHERE nom  = %s AND mot_de_passe = %s"
                cur.execute(query, (username, password))
                medecin=cur.fetchall()
                con.close()
                return medecin, None
        
        except Exception as e:
            print(f"Exception: {e}")
            return None, str(e)
        finally:
            con.close()
    @staticmethod
    def get_medecin_appointement(config, medecinId, startDate, endDate):
        con, error = connect_db(config)
        if con is None:
            return None, "Connection to database failed: %s" % (error)
        
        try:
            with con.cursor(dictionary=True) as cur:
                query = """
                SELECT * FROM rendez_vous 
                WHERE medecinId = %s AND date BETWEEN %s AND %s
            """
                
                cur.execute(query, (medecinId, startDate, endDate))
                rendez_vous = cur.fetchall()
                con.close()
                return rendez_vous, None
        
        except Exception as e:
            print(f"Exception: {e}")
            return None, str(e)
        finally:
            con.close()
     ##
@staticmethod
def Ajouter_medecin(cur, con, nom: str, spe: str, idp: int, image: str):
        cur.execute('INSERT INTO medecin (nom, specialite, Id_Medecin, image,numero_urgence) VALUES (%s, %s, %s, %s,%s)',
                    (nom, spe, idp, image))
        con.commit()

@staticmethod
def deletemed(con, Idmedecin):
        with con.cursor(dictionary=True) as cur:
            cur.execute("DELETE FROM medecin WHERE Id_Medecin = %s", (Idmedecin,))
            con.commit()
            return True, "Record deleted"

@staticmethod
def medecin_detail_by_Id(cur, id: int):
        cur.execute("SELECT * FROM medecin WHERE Id_Medecin = %s", (id,))
        result = cur.fetchall()
        return result