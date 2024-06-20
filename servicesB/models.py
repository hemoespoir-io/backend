from dataclasses import dataclass
import datetime
@dataclass
class Patient:
    Id: int
    NomUtilisateur: str
    Nomcomplet: str
    DateNaissance: str  # Utiliser 'datetime.date' pour une gestion plus typée des dates
    Email: str
    Telephone: str
    Adresse: str
    Motedepasse: str
    image: str
    Groupesanguin: str
    Taille: str
    Poids: str
    Sexe: str
    AntecedeantMere: str
    AntecedeantPere: str
    TypeDeMaladie: str 

    def to_dict(self):
        return {
            "Id": self.Id,
            "NomUtilisateur": self.NomUtilisateur,
            "Nomcomplet": self.Nomcomplet,
            "DateNaissance": self.DateNaissance,
            "Email": self.Email,
            "Telephone": self.Telephone,
            "Adresse": self.Adresse,
            "Motedepasse": self.Motedepasse,
            "image": self.image,
            "Groupesanguin": self.Groupesanguin,
            "Taille": self.Taille,
            "Poids": self.Poids,
            "Sexe": self.Sexe,
            "AntecedeantMere": self.AntecedeantMere,
            "AntecedeantPere": self.AntecedeantPere,
            "TypeDeMaladie": self.TypeDeMaladie
        }


@dataclass
class medicament:
    idM: int
    nom: str
    Id: int  # Correspond à 'Id' dans la table, mais renommé pour la clarté
    

    # Méthode pour retourner une représentation sous forme de dictionnaire
    def to_dict(self):
        return {
            "idM": self.idM,
            "nom": self.nom,
            "Id": self.Id,
           
        }
@dataclass
class medecin:
    id: int  # Renommé de 'IdP' pour correspondre à 'id' de la table
    nom: str
    specialite: str
    image: str
    num_urg: str  # Numéro d'urgence, ajouté pour correspondre à la structure de la table
    date_prise_en_charge: str  # Formaté en snake_case pour suivre les conventions Python

    # Méthode pour convertir l'instance en dictionnaire, utile pour l'intégration avec des bases de données
    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "specialite": self.specialite,
            "image": self.image,
            "num_urg": self.num_urg,
            "DatePriseEncharge": self.date_prise_en_charge
        }

from dataclasses import dataclass

@dataclass
class medecinService:
    medecinId: int  # Correspond à 'medecinId'
    patientId: int  # Correspond à 'patientId'

    # Méthode pour convertir l'instance en dictionnaire, utile pour l'interaction avec des bases de données
    def to_dict(self):
        return {
            "medecinId": self.medecinId,
            "patientId": self.patientId
        }

@dataclass
class medicamentPatients:
    idM: int  # Renommé pour plus de clarté, correspond à 'idM'
    Id: int     # Renommé pour plus de clarté, correspond à 'Id'
    dose: str           # Stocke la dose du médicament
    derniere_date_de_prise: datetime.date  # Utilisation du type 'date' pour mieux gérer les dates

    # Méthode pour convertir l'instance en dictionnaire, utile pour l'interaction avec des bases de données
    def to_dict(self):
        return {
            "idM": self.idM,
            "Id": self.Id,
            "dose": self.dose,
            "derniere_date_de_prise": self.derniere_date_de_prise
        }