from dataclasses import dataclass
import datetime
from sqlite3 import Date
import time
@dataclass
class patient:
    def __init__(self, Id_Patient, NomUtilisateur, Nomcomplet, DateNaissance, Email, Telephone, 
                 Adresse, Motdepasse, image, Groupesanguin, Taille, Poids, Sexe, AntecedentMere, 
                  TypeDeMaladie):
        self.Id_Patient = Id_Patient
        self.NomUtilisateur = NomUtilisateur
        self.Nomcomplet = Nomcomplet
        self.DateNaissance = DateNaissance
        self.Email = Email
        self.Telephone = Telephone
        self.Adresse = Adresse
        self.Motdepasse = Motdepasse
        self.image = image
        self.Groupesanguin = Groupesanguin
        self.Taille = Taille
        self.Poids = Poids
        self.Sexe = Sexe
        self.AntecedentMere = AntecedentMere
        self.TypeDeMaladie = TypeDeMaladie
        
    def to_dict(self):
        return {
            "Id_Patient": self.Id_Patient,
            "NomUtilisateur": self.NomUtilisateur,
            "Nomcomplet": self.Nomcomplet,
            "DateNaissance": self.DateNaissance,
            "Email": self.Email,
            "Telephone": self.Telephone,
            "Adresse": self.Adresse,
            "Motdepasse": self.Motdepasse,
            "image": self.image,
            "Groupesanguin": self.Groupesanguin,
            "Taille": self.Taille,
            "Poids": self.Poids,
            "Sexe": self.Sexe,
            "AntecedentMere": self.AntecedentMere,  
            "TypeDeMaladie": self.TypeDeMaladie
        }
    


@dataclass
class Medicament:
    def __init__(self, id_Medicament: int, nom_medicament: str, Id_Patient: int):
        self.id_Medicament = id_Medicament
        self.nom_medicament = nom_medicament
        
    
    def to_dict(self):
        return {
            "id_Medicament": self.id_Medicament,
            "nom_medicament": self.nom_medicament,
            
        }
@dataclass
class   medecin:
   
    nom: str
    specialite: str
    Id_Medecin: int  
    image: str
    numero_urgence: str 
    
   
    def to_dict(self):
        return {
            
            "nom": self.nom,
            "specialite": self.specialite,
            "Id_Medecin": self.Id_Medecin,
            "image": self.image,
            "numero_urgence": self.numero_urgence,
        }


@dataclass
class medecinPatient:
    medecinId: int 
    patientId: int  
    DateDePriseEnCharge: int  
    
    def to_dict(self):
        return {
            "medecinId": self.medecinId,
            "patientId": self.patientId,
            "DateDePriseEnCharge": self.DateDePriseEnCharge 
        }


@dataclass
class  medicamentPatients:
    id_Medicament: int  
    Id_Patient: int    
    dose: str           
    derniere_date_de_prise: datetime.date 

    
    def to_dict(self):
        return {
            "idM": self.id_Medicament,
            "Id_P": self.Id_Patient,
            "dose": self.dose,
            "derniere_date_de_prise": self.derniere_date_de_prise
        }
class RendezVous:
    medecinId: int
    patientId: int
    date: Date
    heure: int
    description: str
    duree: int

    def to_dict(self):
        return {
            "medecinId": self.medecinId,
            "patientId": self.patientId,
            "date": self.date,
            "heure": self.heure,
            "description": self.description,
            "duree": self.duree
        }