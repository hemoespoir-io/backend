import pandas as pd
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

"""def transform_data(df):

    sex_mapping = {2: "Male", -2: "Female"}
    genetique_mapping = {-3: "N", 4: "F8", 5: "F9"}
    mode_recessif_mapping = {-6: "absence", 6: "X"}
    transmission_genetique_mapping = {-7: "absence", 7: "mère porteuse"}
    facteurs_environnementaux_mapping = {-8: "No", 8: "Yes"}
    hemophilie_mapping = {0: "non malade", 1: "malade"}
    
    df['Sexe'] = df['Sexe'].map(sex_mapping)
    df['genetique'] = df['genetique'].map(genetique_mapping)
    df['mode recessif(heriditaire)'] = df['mode recessif(heriditaire)'].map(mode_recessif_mapping)
    df['Transmission genetique'] = df['Transmission genetique'].map(transmission_genetique_mapping)
    df['Facteurs environnementaux'] = df['Facteurs environnementaux'].map(facteurs_environnementaux_mapping)
    df['hemophilie'] = df['hemophilie'].map(hemophilie_mapping)
    
    return df"""


import os
import sendgrid
from sendgrid.helpers.mail import Mail
import ssl

# Désactiver la vérification SSL (Non recommandé pour la production)
ssl._create_default_https_context = ssl._create_unverified_context

api_key = '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'

if not api_key:
    raise ValueError("La clé API SendGrid n'est pas définie")

print(f"Clé API SendGrid : {api_key}")

message = Mail(
    from_email='okebennani@gmail.com',  
    to_emails='nabil.qasmi1@gmail.com',
    subject='Voulez-vous changer votre mot de passe ?',
    plain_text_content='Votre mot de passe peut être changé maintenant.',
    html_content='<strong>Votre mot de passe peut être changé maintenant.</strong>'
)

try:
    sg = sendgrid.SendGridAPIClient(api_key)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(f"Votre email a été bien envoyé mais il semble y avoir une petite erreur d'API : {e}")
