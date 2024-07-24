-- creation de la base de donnes 
CREATE DATABASE `pfe`; 
-- utilisation de la base de donnes 
USE `pfe`;
-- creation de la table patient 
CREATE TABLE `patient` (
  `Id_Patient` int NOT NULL AUTO_INCREMENT,
  `NomUtilisateur` varchar(50) DEFAULT NULL,
  `Nomcomplet` varchar(50) DEFAULT NULL,
  `DateNaissance` date DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Telephone` varchar(50) DEFAULT NULL,
  `Adresse` varchar(50) DEFAULT NULL,
  `Motdepasse` varchar(50) DEFAULT NULL,
  `image` text,
  `Groupesanguin` varchar(50) DEFAULT NULL,
  `Taille` varchar(50) DEFAULT NULL,
  `Poids` varchar(50) DEFAULT NULL,
  `Sexe` varchar(50) DEFAULT NULL,
  `AntecedentMere` varchar(50) DEFAULT NULL,
  `AntecedentPere` varchar(50) DEFAULT NULL,
  `TypeDeMaladie` varchar(50) NOT NULL,
  PRIMARY KEY (`Id_Patient`)
);

-- creation de la table medecins
CREATE TABLE `medecins` (
  `Id_Medecin` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) DEFAULT NULL,
  `specialite` varchar(255) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `numero_urgence` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`Id_Medecin`)
);

-- creation de la table medicament 
CREATE TABLE `Medicament` (
  `id_Medicament` int NOT NULL AUTO_INCREMENT,
  `nom_medicament` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_Medicament`)
);

-- creation de la table medecinPatient 
CREATE TABLE `medecinPatient` (
  `medecinId` int NOT NULL,
  `patientId` int NOT NULL,
  `DateDePriseEnCharge` date DEFAULT NULL,
  KEY `medecinId` (`medecinId`),
  KEY `patientId` (`patientId`),
  CONSTRAINT `medecinPatient_ibfk_1` FOREIGN KEY (`medecinId`) REFERENCES `medecins` (`Id_Medecin`),
  CONSTRAINT `medecinPatient_ibfk_2` FOREIGN KEY (`patientId`) REFERENCES `patient` (`Id_Patient`)
);

-- creation de la table medicamentPatients
CREATE TABLE `medicamentPatients` (
  `id_Medicament` int DEFAULT NULL,
  `Id_Patient` int DEFAULT NULL,
  `dose` varchar(50) DEFAULT NULL,
  `derniere_date_de_prise` date DEFAULT NULL,
  KEY `idx_id_Medicament` (`id_Medicament`),
  KEY `idx_Id_Patient` (`Id_Patient`)
);

-- creation de la table video
CREATE TABLE `Video` (
  `Id_video` int NOT NULL AUTO_INCREMENT,
  `titre` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Id_video`)
);
