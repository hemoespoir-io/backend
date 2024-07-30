#connexion avec le root
mysql -u root -p
#affichage des base de donnes
show databases;

#creation de la base de donnnees 
CREATE DATABASE pfe ;
#creation d'uun utilisateur 
CREATE USER 'hemoespoir'@'$1' IDENTIFIED BY '$2';
#les droit dacces 
GRANT ALL ON pfe.* TO 'hemoespoir'@"$1";
#privillieges
FLUSH PRIVILEGES;
#exit mysql server
exit;
#importation du fichier sql 
mysql -u hemoespoir -p pfe < shema.sql
