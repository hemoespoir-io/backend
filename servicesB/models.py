from dataclasses import dataclass
import datetime
@dataclass
class patient:
    def __init__(self, Id_Patient, NomUtilisateur, Nomcomplet, DateNaissance, Email, Telephone, 
                 Adresse, Motdepasse, image, Groupesanguin, Taille, Poids, Sexe, AntecedentMere, 
                 AntecedentPere, TypeDeMaladie):
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
        self.AntecedentPere = AntecedentPere
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
            "AntecedentPere": self.AntecedentPere,
            "TypeDeMaladie": self.TypeDeMaladie
        }
    


@dataclass
class medicament:
    id_Medicament: int
    nom_medicament: str
    Id_Patient: int  
    

    
    def to_dict(self):
        return {
            "id_Medicament": self.id_Medicament,
            "nom_medicament": self.nom_medicament,
            " Id_Patient": self. Id_Patient,
           
        }
@dataclass
class   medecins:
   
    nom: str
    specialite: str
    Id_Medecin: int  # Renommé de 'IdP' pour correspondre à 'id' de la table
    image: str
    numero_urgence: str  # Numéro d'urgence, ajouté pour correspondre à la structure de la table
    
    # Méthode pour convertir l'instance en dictionnaire, utile pour l'intégration avec des bases de données
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
    medecinId: int  # Correspond à 'medecinId'
    patientId: int  # Correspond à 'patientId'
    DateDePriseEnCharge: int  # Correspond à 'DateDePriseEnCharge'
    
    # Méthode pour convertir l'instance en dictionnaire, utile pour l'interaction avec des bases de données
    def to_dict(self):
        return {
            "medecinId": self.medecinId,
            "patientId": self.patientId,
            "DateDePriseEnCharge": self.DateDePriseEnCharge # Convertir la date en chaîne de caractères
        }


@dataclass
class  medicamentPatients:
    id_Medicament: int  # Renommé pour plus de clarté, correspond à 'idM'
    Id_Patient: int     # Renommé pour plus de clarté, correspond à 'Id'
    dose: str           # Stocke la dose du médicament
    derniere_date_de_prise: datetime.date  # Utilisation du type 'date' pour mieux gérer les dates

    # Méthode pour convertir l'instance en dictionnaire, utile pour l'interaction avec des bases de données
    def to_dict(self):
        return {
            "idM": self.id_Medicament,
            "Id_P": self.Id_Patient,
            "dose": self.dose,
            "derniere_date_de_prise": self.derniere_date_de_prise
        }