import os
import subprocess

# Le contenu du fichier batch à générer
batch_content = """@echo off
netsh WLAN set hostednetwork mode=allow SSID="YourNetworkName" key="YourPassword"
netsh wlan start hostednetwork
"""


# Fonction pour configurer et démarrer le réseau hébergé
def start_hosted_network():
    # Obtenez le chemin complet du script Python
    script_path = os.path.abspath(__file__)

    # Choisissez l'emplacement où vous voulez placer le fichier batch
    batch_folder = r"C:\Scripts"
    batch_filename = os.path.join(batch_folder, "start.bat")

    # Si le fichier batch n'existe pas, créez-le
    if not os.path.exists(batch_filename):
        with open(batch_filename, "w") as batch_file:
            batch_file.write(batch_content)
        print(f"Le fichier {batch_filename} a été créé.")

    try:
        # Exécutez le fichier batch en utilisant subprocess
        subprocess.run([batch_filename], shell=True, check=True)
        print("Le réseau hébergé a été configuré et démarré avec succès.")
    except subprocess.CalledProcessError:
        print(
            "Une erreur s'est produite lors de la configuration et du démarrage du réseau hébergé."
        )


# Appel de la fonction pour configurer et démarrer le réseau hébergé
start_hosted_network()

# Ajouter une entrée au registre pour exécuter le script au démarrage
startup_key = r"HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run"
script_name = "StartupScript"
os.system(f'reg add "{startup_key}" /v "{script_name}" /d "{script_path}" /f')
