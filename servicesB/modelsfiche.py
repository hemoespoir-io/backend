class Patients:
    def __init__(self, id, nomutilisateur, nomcomplet, date_naissance, email, telephone, adresse, motdepasse, image, groupesanguin, taille, poids, sexe, antecedant_mere, antecedant_pere):
        self.id = id
        self.nomutilisateur = nomutilisateur
        self.nomcomplet = nomcomplet
        self.date_naissance = date_naissance
        self.email = email
        self.telephone = telephone
        self.adresse = adresse
        self.motdepasse = motdepasse
        self.image = image
        self.groupesanguin = groupesanguin
        self.taille = taille
        self.poids = poids
        self.sexe = sexe
        self.antecedant_mere = antecedant_mere
        self.antecedant_pere = antecedant_pere

class Medicament:
    def __init__(self, idM, nom, idPatient, dose, date, time):
        self.idM = idM
        self.nom = nom
        self.idPatient = idPatient
        self.dose = dose
        self.date = date
        self.time = time

class Medecin:
    def __init__(self, nom, specialite, id, image):
        self.nom = nom
        self.specialite = specialite
        self.id = id
        self.image = image
