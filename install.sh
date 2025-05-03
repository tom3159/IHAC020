#!/bin/bash

# Création de l'environnement virtuel IHAC020 si non existant
if [ ! -d "IHAC020" ]; then
    echo "Création de l'environnement virtuel IHAC020..."
    python3 -m venv IHAC020
fi

# Activation de l'environnement
source IHAC020/bin/activate

# Vérification que le dossier /home/$USER/cheatsheet existe
if [ ! -d "/home/$USER/cheatsheet" ]; then
    echo "Création du répertoire /home/$USER/cheatsheet..."
    mkdir -p /home/$USER/cheatsheet
fi

# Copie de tous les fichiers .md vers /home/$USER/cheatsheet
echo "Copie des fichiers .md vers /home/$USER/cheatsheet..."
cp ./*.md /home/$USER/cheatsheet/

# Génération du script Bash interactif
echo "Génération du script Bash depuis le fichier Excel..."
IHAC020/bin/python3 generate_menu.py

# Rend le menu interactif exécutable
chmod +x menu_interactif.sh

echo "Installation terminée. Lancement du menu interactif :"
./menu_interactif.sh

