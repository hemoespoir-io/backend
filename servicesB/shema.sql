USE `pfe`;

-- Creation de la table patient
CREATE TABLE patient (
  Id_Patient INT AUTO_INCREMENT,
  NomUtilisateur VARCHAR(50) NOT NULL,
  Nomcomplet VARCHAR(50) NOT NULL,
  DateNaissance DATE NOT NULL,
  Email VARCHAR(50) NOT NULL,
  Telephone VARCHAR(50) NOT NULL,
  Adresse VARCHAR(50) NOT NULL,
  Motdepasse VARCHAR(50) NOT NULL,
  image TEXT,
  Groupesanguin VARCHAR(50) NOT NULL,
  Taille VARCHAR(50) NOT NULL,
  Poids VARCHAR(50) NOT NULL,
  Sexe VARCHAR(50) NOT NULL,
  AntecedentMere VARCHAR(50) NOT NULL,
  AntecedentPere VARCHAR(50) NOT NULL,
  TypeDeMaladie VARCHAR(50) NOT NULL,
  PRIMARY KEY (Id_Patient)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- Creation de la table medicament
CREATE TABLE Medicament (
  id_Medicament INT NOT NULL AUTO_INCREMENT,
  nom_medicament VARCHAR(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (id_Medicament)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- Creation de la table medecins
CREATE TABLE medecins (
  nom VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  specialite VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  Id_Medecin INT NOT NULL AUTO_INCREMENT,
  image VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  numero_urgence VARCHAR(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (Id_Medecin)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- Creation de la table medecinPatient
CREATE TABLE medecinPatient (
  medecinId INT NOT NULL,
  patientId INT NOT NULL,
  DateDePriseEnCharge DATE NOT NULL,
  PRIMARY KEY (medecinId, patientId),
  KEY medecinId (medecinId),
  KEY patientId (patientId),
  CONSTRAINT medecinPatient_ibfk_1 FOREIGN KEY (medecinId) REFERENCES medecins (Id_Medecin) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT medecinPatient_ibfk_2 FOREIGN KEY (patientId) REFERENCES patient (Id_Patient) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- Creation de la table medicamentPatients
CREATE TABLE medicamentPatients (
  id_Medicament INT NOT NULL,
  Id_Patient INT NOT NULL,
  dose VARCHAR(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  derniere_date_de_prise DATE DEFAULT NULL,
  PRIMARY KEY (id_Medicament, Id_Patient),
  KEY idx_Id_Medicament (id_Medicament),
  KEY idx_Id_Patient (Id_Patient),
  CONSTRAINT medicamentPatients_ibfk_1 FOREIGN KEY (id_Medicament) REFERENCES Medicament (id_Medicament) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT medicamentPatients_ibfk_2 FOREIGN KEY (Id_Patient) REFERENCES patient (Id_Patient) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
--ajout du champs mots de passe dans la table medecins
ALTER TABLE medecins
ADD COLUMN mot_de_passe VARCHAR(255) NULL;
--ajouter une class rendez-vous
CREATE TABLE rendez_vous (
    medecinId INT(11) NOT NULL,
    patientId INT(11) NOT NULL,
    date DATE NOT NULL,
    heure TIME NOT NULL,
    description TEXT,
    duree int NOT NULL,
    PRIMARY KEY (medecinId, patientId, date, heure),
    FOREIGN KEY (medecinId) REFERENCES medecin(Id_Medecin),
    FOREIGN KEY (patientId) REFERENCES patient(Id_Patient)
);