from datetime import datetime, timedelta
from flask import Flask, json, make_response,request,jsonify,session
from services import   medecinservices, patientServices
from flask_cors import CORS
import logging
from datetime import datetime
app = Flask(__name__)

app.config.from_envvar('APP_SETTINGS')


#Les routes

#Avoir une page qui sa form method=POST la methode POST

"""
@app.route('/add_patient', methods=['POST'])
def add_patient():
    patient = request.get_json()  # On suppose que le patient est envoyé au format JSON
    if not patient:
        return jsonify({'error': 'No patient data provided'}), 400

    con = connect_db()
    if con is None:
        return jsonify({'error': 'Connection to database failed'}), 500

    try:
        with con.cursor(dictionary=True) as cur:
            DAOpatients.AjouterPatientbyId(cur, con, patient)
        con.close()
        return jsonify({'success': True}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500



#Avoir une page qui sa form method=DELETE la methode DELETE
@app.route('/DeletePatients/<int:id>', methods=['DELETE'])
def DeletePatients(id):
    result, error = patientServices.deletePatients(id)
    if error:
        response = {
            "status": "error",
            "message": error
        }
        return make_response(jsonify(response), 500)
    else:
        response = {
            "status": "success",
            "result": result
        }
        return make_response(jsonify(response), 200)

#Avoir une page qui sa form method=POST la methode POST


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
  medi=medicament(id=0,nom=nom,idPatient=idPatient,dose=dose,Date=date,time=time)
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


@app.route('/PasParJourS', methods=['POST'])
def PasParJourS():
    data = request.get_json()
    nomutilisateur = data.get('nomutilisateur')
    
    if not nomutilisateur:
        return jsonify({'error': 'Username must be provided'}), 400
    
    birth_date, error = Service.patient_age1(nomutilisateur)
    
    if error or birth_date is None:
        return jsonify({'error': 'Failed to retrieve birth date'}), 500
    
    age = Service.calculate_age(birth_date)
    
    if isinstance(age, str) and 'invalid' in age:
        return jsonify({'error': 'Invalid birth date format'}), 500
    
    weight = Service.patient_poid(nomutilisateur)
    
    if weight is None:
        return jsonify({'error': 'Failed to retrieve weight'}), 500
    
    steps_per_day = Service.pasParJours(age, weight)
    


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


app = Flask(__name__)

##################
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/fichemedical', methods=['GET'])
def get_patient_details():
    patient_id = request.args.get('patientid')
    if not patient_id:
        return jsonify({"error": "Missing patient ID"}), 400

    details, error = patientServices.FicheMedicale(int(patient_id))
    if error:
        return jsonify({"error": error}), 500

    return jsonify(details), 200
@app.route('/patient/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    
    patient_data, error = patientServices.get_patient_byID(patient_id)
    
    if error:
        return jsonify({'error': error}), 404
    return jsonify(patient_data), 200
@app.route('/patient/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    result, error = patientServices.deletePatients(patient_id)
    
    if error:
        return jsonify({'error': error}), 500
    return jsonify(result), 200
@app.route('/patient/logout', methods=['POST'])
def log_out():
    data = request.json
    if not data or 'gmail' not in data or 'mdp' not in data:
        return jsonify({'error': 'Email and password must be provided'}), 400
    
    gmail = data['gmail']
    mdp = data['mdp']
    
    patient, error = patientServices.LogOut_by_Email_Password(gmail, mdp)
    
    if error:
        return jsonify({'error': error}), 404
    return jsonify({
       
        # Ajoutez ici tous les autres champs de votre modèle Patients
    }), 200
@app.route('/ModifyPatients', methods=['POST'])
def modify_patients():
    data = request.get_json()
    nom = data.get('nomutilisateur')
    mdp = data.get('mdp')
    
    if not nom or not mdp:
        return jsonify({'error': 'Username and password must be provided'}), 400
    
    success, error = patientServices.ModifierPatientByPassword(nom, mdp)
    
    if error:
        return jsonify({'error': error}), 500
    return jsonify({'message': 'Patient modified successfully'}), 200
   
patients = [
    patient(11, "qasminabil", "nabil qasmi", "2002-08-15", "nabil.qasmi@gmail.com", "06 ** ** ** **", 
            "medecin ghassani dr hanane benchekroune", "nabil123", "lien ou données de l'image", 
            "A++", 1.80, 70, "H", "oui", "oui", "hemophelie A")
   
]



@app.route('/get_patient_age', methods=['GET'])
def get_patient_age():
    date_naissance = request.args.get('DateNaissance')
    if not date_naissance:
        return jsonify({"error": "Parameter 'DateNaissance' is required"}), 400
    
    age, error = patientServices.patient_age2(date_naissance)
    if error:
        return jsonify({"error": error}), 500
    
    return jsonify({"age": age}), 200

@app.route('/get_patient_poid', methods=['GET'])
def get_patient_poid():
    patient_id = request.args.get('id')
    if not patient_id:
        return jsonify({"error": "Parameter 'id' is required"}), 400

    try:
        patient_id = int(patient_id)
    except ValueError:
        return jsonify({"error": "Parameter 'id' must be an integer"}), 400
    
    poid, error = patientServices.patient_poid(patient_id)
    if error:
        return jsonify({"error": error}), 500

    return jsonify({"poid": poid}), 200


@app.route('/addPatient', methods=['POST'])
def add_patient():
    data = request.json
    required_fields = [
        "NomUtilisateur", "Nomcomplet", "DateNaissance", "Email",
        "Telephone", "Adresse", "Motdepasse", "Groupesanguin", "Taille",
        "Poids", "Sexe", "AntecedentMere", "AntecedentPere", "TypeDeMaladie"
    ]
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400

    try:
        new_patient = patient(
            Id_Patient=121,
            NomUtilisateur=data['NomUtilisateur'],
            Nomcomplet=data['Nomcomplet'],
            DateNaissance=data['DateNaissance'],
            Email=data['Email'],
            Telephone=data['Telephone'],
            Adresse=data['Adresse'],
            Motdepasse=data['Motdepasse'],
            image=data.get('image'),  # This can be None if not provided
            Groupesanguin=data['Groupesanguin'],
            Taille=data['Taille'],
            Poids=data['Poids'],
            Sexe=data['Sexe'],
            AntecedentMere=data['AntecedentMere'],
            AntecedentPere=data['AntecedentPere'],
            TypeDeMaladie=data['TypeDeMaladie']
        )

        patient_info, error = patientServices.addPatients(new_patient)
        if error:
            return jsonify({"error": error}), 400
        else:
            return jsonify({"patient": patient_info.__dict__}), 201
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@app.route('/addMedecin', methods=['POST'])
def add_medecin():
        data = request.get_json()
        medecin_nom = data.get('nom')
        medecin_spe = data.get('spe')
        medecin_id = data.get('id')
        medecin_image = data.get('image')
        medecin_numero_urgence = data.get('numero_urgence')

        result, message = medecinservices.addMedecins(medecin_nom, medecin_spe, medecin_id, medecin_image, medecin_numero_urgence)
    
        if result:
            return jsonify({'success': True, 'message': message}), 200
        else:
            return jsonify({'success': False, 'message': message}), 400
app = Flask(__name__)
@app.route('/deleteMedecin', methods=['DELETE'])
def delete_medecin():
    medecin_id = request.json.get('id')
    if not medecin_id:
        return jsonify({"error": "Medecin ID is required"}), 400

    result, message = DAOmedecin.deletemed(medecin_id)
    if result is None:
        return jsonify({"error": message}), 500
    return jsonify({"message": message}), 200"""
CORS(app)  # Permettre CORS pour toutes les routes





@app.route('/fichemedical', methods=['GET'])
def get_patient_details():
    
    patient_id = request.args.get('patientid')
    if not patient_id:
        return jsonify({"error": "Missing patient ID"}), 400

    try:
        details, error = patientServices.FicheMedicale(app.config, int(patient_id))
        if error:
            return jsonify({"serveurerror": error}), 500

        return jsonify(details), 200
    except ValueError:
        return jsonify({"error": ValueError}), 500
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400
    
    try:
        patient_info, error = patientServices.logIn(app.config, username, password)
        
        if error:
            return jsonify({"serveurerror": error}), 500
        
        return jsonify({"patient": patient_info}), 200

    except ValueError:
        return jsonify({"error": ValueError}), 500
    
#loginMedecin
@app.route('/loginMedecin', methods=['POST'])
def loginMedecin():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400
    
    try:
        medecin_info, error = medecinservices.logInMedecin(app.config, username, password)
        
        if error:
            return jsonify({"serveurerror": error}), 500
        
        return jsonify({"medecin": medecin_info}), 200

    except ValueError:
        return jsonify({"error": ValueError}), 500
    
    #####################################
# Exemple de rendez-vous déjà réservés
CORS(app) 
@app.route('/getAppointment', methods=['POST'])
def getAppointment():
    data = request.json
    medecinId = data.get('medecinId')
    patientId = data.get('patientId')
    startDate = data.get('startDate')
    endDate = data.get('endDate')
    
    if not medecinId or not patientId or not startDate or not endDate:
        return jsonify({"error": "Missing required parameters"}), 400
    
    try:
        startDate = datetime.strptime(startDate, "%Y-%m-%d")
        endDate = datetime.strptime(endDate, "%Y-%m-%d")
    except ValueError:
        return jsonify({"error": "Invalid date format, should be YYYY-MM-DD"}), 400

    try:
        appointment_info, error = patientServices.get_appointement(app.config, medecinId, patientId, startDate, endDate)
        
        if error:
            logging.error(f"Error retrieving appointments: {error}")
            return jsonify({"servererror": error}), 500
        
        return jsonify({"appointments": appointment_info}), 200

    except Exception as e:
        logging.exception("An unexpected error occurred")
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=True)