#!/bin/bash
set -e

# Définir les chemins des répertoires
REPO_DIR="$(pwd)"  # Répertoire courant, supposé être IHAC020
DEP_DIR="$REPO_DIR/Deps"
PKG_DIR="$DEP_DIR/python_pkgs"

# Installer les paquets .deb téléchargés
cd $DEP_DIR
for deb in *.deb; do
    sudo dpkg -i $deb
done

# Créer un environnement virtuel Python et l'activer
python3 -m venv $REPO_DIR/IHAC020
source $REPO_DIR/IHAC020/bin/activate

# Mettre à jour pip et installer les paquets Python depuis les .whl
pip install --upgrade pip
pip install --no-index --find-links=$PKG_DIR pandas openpyxl numpy python-dateutil pytz tzdata et-xmlfile six

# Désactiver l'environnement virtuel
deactivate

echo "Installation terminée avec succès!"

