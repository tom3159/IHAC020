#!/bin/bash

# Vérification que le dossier /home/$USER/cheatsheet existe
if [ ! -d "/home/$USER/cheatsheet" ]; then
    echo "Création du répertoire /home/$USER/cheatsheet..."
    mkdir -p /home/$USER/cheatsheet
fi

# Copie de tous les fichiers .md vers /home/$USER/cheatsheet
echo "Copie des fichiers .md vers /home/$USER/cheatsheet..."
cp ./MD/*.md /home/$USER/cheatsheet/
