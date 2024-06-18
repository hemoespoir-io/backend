from flask import Flask,request,jsonify,session
from services import patientServices,MedicamentService,medecinservices
from models import Patients,Medicament

app=Flask(__name__)


#Les routes

#Avoir une page qui sa form method=POST la methode POST
@app.route('/AddPatients', methods=['POST'])
def addPatients():
  patient_data = request.get_json()
  print(patient_data)
  patient = Patients(id=0,nomutilisateur=patient_data['nomutilisateur'],Nomcomplet=patient_data['Nomcomplet'],Date_Naissance=patient_data['Date_Naissance'],email=patient_data['email'],num_tel=patient_data['num_tel'],adresse=patient_data['adresse'],mdp=patient_data['mdp'],image=patient_data['image'],GR_S=patient_data['GR_S'],taille=patient_data['taille'],poids=patient_data['poids'],sexe=patient_data['sexe'],antecedant_mere=patient_data['antecedant_mere'],antecedant_pere=patient_data['antecedant_pere'])
  return patientServices.addPatients(patient)
  

#Avoir une page qui sa form method=DELETE la methode DELETE
@app.route('/DeletePatients/<id>',methods=['DELETE'])
def DeletePatients(id:int):
  return patientServices.deletePatients(id)


#Avoir une page qui sa form method=POST la methode POST
@app.route('/ModifyPatients',methods=['POST'])
def ModifyPatients():
    data = request.get_json()
    nom = data.get('nomutilisateur')
    mdp = data.get('mdp')
    return patientServices.ModifyPatients(nom,mdp)

app.secret_key = 'votre_cle_secrete'
@app.route('/LogIn', methods=['POST'])
def LogIn():
    data = request.get_json()
    print(data)
    nomutilisateur = data.get('nomutilisateur')
    mdp = data.get('mdp')
    print(nomutilisateur)
    print(mdp)
    
    patient = patientServices.LogIn(nomutilisateur, mdp)
    if patient:
        session['patient_id'] = patient.id 
        session['nomutilisateur'] = nomutilisateur
        
        return jsonify(patient.to_dict())
    else:
        return jsonify({'error': 'Nom d\'utilisateur ou mot de passe incorrect'}), 401
    


@app.route('/AddMedicament', methods=['POST'])
def addMedicament():
  #print(Medicement_data)
  data=request.get_json()

  nom=data.get('nom')
  dose=data.get('dose')
  date=data.get('date')
  time=data.get('time')
  idPatient=data.get('idpatient')
  
  #print(nom,dose,date,time,idPatient)
  medi=Medicament(id=0,nom=nom,idPatient=idPatient,dose=dose,Date=date,time=time)
  #print(medi)
  #nom:str,dose:int,date:str,time:str,idPatient:int
  
  return MedicamentService.ajouterMedicament(medi)


@app.route('/suppMedicament', methods=['POST'])
def deletemedicament():
  data=request.get_json()
  nom=data.get('nomMed')
  idPatient=data.get('IdPatient') 
  print(nom,idPatient)
  medicament=MedicamentService.searchMed(nom,idPatient)
  return MedicamentService.deletemedicament(medicament)

@app.route('/LogOut',methods=['POST'])
def Logout():
  data=request.get_json()
  gmail=data.get('gmail')
  mdp=data.get('mdp')
  session.pop(mdp,None)
  patient=patientServices.LogOut(gmail, mdp)
  return jsonify(patient.to_dict())


@app.route('/PasParJourS',methods=['POST'])
def PasParJourS():
  data=request.get_json()
  nomutilisateur=data.get('nomutilisateur')
  #print(patientServices.pasParJours(patientServices.calculate_age(patientServices.patient_age1(nomutilisateur)),patientServices.patient_poid(nomutilisateur)))
  return patientServices.pasParJours(patientServices.calculate_age(patientServices.patient_age1(nomutilisateur)),patientServices.patient_poid(nomutilisateur))
 


@app.route('/checkAge',methods=['POST'])
def checkAge():
  data=request.get_json()
  dateNaissance=data.get('dateNaissance')
  if not dateNaissance:
        return jsonify({'error': 'Date de naissance est requise'}), 400

  age = patientServices.calculate_age(dateNaissance)
  is_valid = patientServices.checkAge(age)
  return jsonify({'age': age, 'valid': is_valid})
  

@app.route('/lastPatient',methods=['POST'])
def lastPatient():
  patient=patientServices.lastPatient()
  print(patient)
  return jsonify(patient.to_dict())

@app.route('/DecisinoPatient',methods=['POST'])
def DecisinoPatient():
  data=request.get_json()
  id=data.get('Id')
  print(id)
  return patientServices.DecisinoPatient(id)


@app.route('/allMedicaments',methods=['POST'])
def allMedicaments():
  data=request.get_json()
  id=data.get('Id')
  print(MedicamentService.allMedicament(id))
  return MedicamentService.allMedicament(id)


@app.route('/addmedecin',methods=['POST'])
def addmedecin():
  data=request.get_json()
  print(data)
  nom=data.get('nom')
  specialite=data.get('spe')
  image=data.get('image')
  idPatient=data.get('idpatient')
  print(nom,specialite,image)
  return medecinservices.addmedecins(nom,specialite,idPatient,image)

@app.route('/deletemedecin',methods=['GET'])
def deletemedecin():
  data=request.get_json()
  nom=data.get('nom')
  return medecinservices.deletemed(nom)

@app.route('/allmedecin',methods=['POST'])
def allmedecin():
  data=request.get_json()
  print(data)
  Id=data.get('Id')
  #print(Id) 
  print(medecinservices.searchmedecin(Id))
  return medecinservices.searchmedecin(Id)

@app.route('/checkPoids',methods=['POST'])
def checkPoids():
  data=request.get_json()
  #print(data)
  poids=data.get('poids') 
  #print(poids)
  is_valid = patientServices.checkPoids(poids)
  #print(is_valid)
  return jsonify({'poids': poids, 'valid': is_valid})

@app.route('/Age',methods=['POST'])
def Age():
  data=request.get_json()
  nom=data.get('nomUti')
  print(type(patientServices.calculate_age(patientServices.patient_age1(nom))))
  return jsonify({'age':patientServices.calculate_age(patientServices.patient_age1(nom))})  

if __name__=='__main__':
  app.run(debug=True)