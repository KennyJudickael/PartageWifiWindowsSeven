# README - Configuration et Démarrage d'un Réseau Hébergé (Hotspot) sur Windows

Ce script Python a été conçu pour vous permettre de configurer et de démarrer un réseau Wi-Fi hébergé (hotspot) sur un ordinateur Windows. Le réseau hébergé peut être personnalisé en termes de nom de réseau (SSID) et de mot de passe.

## Prérequis

Avant d'utiliser ce script, assurez-vous de remplir les conditions préalables suivantes :

1. **Système d'exploitation** : Ce script est destiné à être exécuté sur un système d'exploitation Windows.

2. **Droits d'administration** : Vous devez exécuter ce script en tant qu'administrateur, car il effectue des opérations système qui nécessitent des privilèges élevés.

## Fonctionnalités

Ce script comporte les fonctionnalités suivantes :

1. **Création d'un fichier batch** : Le script génère un fichier batch (`start.bat`) contenant des commandes pour configurer et démarrer un réseau hébergé avec un nom de réseau (SSID) et un mot de passe personnalisés.

2. **Exécution du fichier batch** : Le fichier batch est exécuté en utilisant la bibliothèque `subprocess`, ce qui permet de configurer et de démarrer le réseau hébergé.

3. **Ajout au démarrage** : Le script ajoute une entrée au registre Windows (`HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`) pour que le script soit exécuté automatiquement chaque fois que vous démarrez votre ordinateur.

## Utilisation

Suivez ces étapes pour utiliser ce script :

1. **Personnalisez les paramètres** : Modifiez les valeurs de `SSID` et `key` dans la variable `batch_content` pour définir le nom du réseau (SSID) et le mot de passe de votre choix.

2. **Exécutez le script Python** : Exécutez le script Python en tant qu'administrateur. Le script générera le fichier batch et tentera de le démarrer.

3. **Vérification** : Consultez la sortie du script pour vous assurer que le réseau hébergé a été configuré et démarré avec succès ou s'il y a eu des erreurs.

4. **Redémarrage automatique** : Une entrée au registre est ajoutée pour exécuter le script au démarrage de l'ordinateur, de sorte que le réseau hébergé sera configuré automatiquement chaque fois que vous démarrez votre ordinateur.

## Personnalisation

Vous pouvez personnaliser les paramètres suivants dans le script :

- `batch_content`: Modifiez les valeurs de `SSID` et `key` pour définir le nom du réseau (SSID) et le mot de passe de votre choix.

- `batch_folder`: Changez le chemin où le fichier batch sera créé si nécessaire.

- `startup_key` et `script_name`: Modifiez ces valeurs si vous souhaitez changer le nom sous lequel le script est ajouté au démarrage.

## Avertissement

Veillez à ne pas divulguer le mot de passe de votre réseau hébergé, car il est stocké en clair dans le fichier batch. Gardez le fichier batch en sécurité.

**Note :** L'exécution de ce script peut nécessiter des privilèges d'administrateur et peut avoir des implications en matière de sécurité. Utilisez-le avec précaution et assurez-vous de comprendre son fonctionnement.
