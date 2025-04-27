from openpyxl import load_workbook
import pandas as pd

# Charger le fichier Excel
fichier_excel = "Analyse_Risques_Biens.xlsx"
wb = load_workbook(filename=fichier_excel, read_only=True)

# Feuilles nécessaires
ws_criteres = wb['RISQUES_BIENS']
ws_osi_layers = wb['RISQUES_ATTAQUES']
ws_attack_types = wb['ATTAQUES_OUTILS']

# --- Extraction des données ---

# Critères de sécurité fixes
criteres = ["1-Confidentialité", "2-Intégrité", "3-Disponibilité"]

# Charger le DataFrame pour les couches OSI
df_osi_layers = pd.read_excel(fichier_excel, sheet_name="RISQUES_ATTAQUES")

# Couches OSI dynamiques
osi_row = df_osi_layers.iloc[0]

# Vérification et ajout de "Couche 1" si la première cellule est vide
if pd.isna(osi_row[0]):
    osi_layers = ["1-Couche 1"] + [
        f"{i+2}-Couche {str(int(float(val)))}"  # Convertir en float puis en int pour éviter les décimales
        for i, val in enumerate(osi_row[1:].values)
        if pd.notna(val)
    ]
else:
    osi_layers = [
        f"{i+1}-Couche {str(int(float(val)))}"  # Convertir en float puis en int pour éviter les décimales
        for i, val in enumerate(osi_row[1:].values)
        if pd.notna(val)
    ]

# Attaques
attaques = []
for row in ws_attack_types.iter_rows(min_row=2, values_only=True):
    if row[0]:  # Première colonne non vide
        attaques.append(row[0])

attaques_formatees = [f"{i+1}-{attaque}" for i, attaque in enumerate(attaques)]

# --- Fonction de normalisation des caractères accentués ---
def normalize_string(text):
    """Normalise une chaîne en enlevant les accents et caractères spéciaux"""
    return text.replace("é", "e").replace("è", "e").replace("ê", "e").replace("à", "a").replace("ç", "c") \
        .replace("ù", "u").replace("ô", "o").replace("î", "i").replace("ï", "i").replace("ü", "u").replace("ÿ", "y") \
        .replace("É", "E").replace("È", "E").replace("Ê", "E").replace("À", "A").replace("Ç", "C").replace("Ù", "U") \
        .replace("Ô", "O").replace("Î", "I").replace("Ï", "I").replace("Ü", "U").replace("Ÿ", "Y")

# --- Génération du script Bash ---

with open("menu_interactif.sh", "w") as f:
    f.write("""#!/bin/bash

# --- MENU GÉNÉRÉ AUTOMATIQUEMENT ---

# Fonction de normalisation des caractères accentués
normalize_string() {
    echo "$1" | iconv -f UTF-8 -t ASCII//TRANSLIT
}

""")
    f.write("criteres=(" + " ".join(f'"{c}"' for c in criteres) + ")\n")
    f.write("osi_layers=(" + " ".join(f'"{c}"' for c in osi_layers) + ")\n")
    f.write("attaques=(" + " ".join(f'"{a}"' for a in attaques_formatees) + ")\n")

    f.write("""
echo "Que souhaitez-vous faire ?"
echo "1 - Recherche sur les critères de sécurité"
echo "2 - Recherche selon les couches du modèle OSI"
echo "3 - Liste des types d'attaque"
read -p "Votre choix (1/2/3) : " choix

if [ "$choix" = "1" ]; then
  echo "Critères de sécurité :"
  for item in "${criteres[@]}"; do echo "$item"; done
  read -p "Choisissez un critère (1/2/3) : " critere_choix
  case $critere_choix in
    1|2|3)
        selection="${criteres[$((critere_choix-1))]}"
        motcle=$(echo $selection | cut -d'-' -f2)
        motcle_normalize=$(normalize_string "$motcle")
        echo "Vous avez choisi : $motcle"
        echo
        grep -i "$motcle_normalize" /home/$USER/cheatsheet/*
        ;;
    *) echo "Choix invalide" ;;
  esac

elif [ "$choix" = "2" ]; then
  echo "Couches du modèle OSI :"
  for couche in "${osi_layers[@]}"; do echo "$couche"; done
  read -p "Choisissez une couche : " osi_choix
  case $osi_choix in
""")

    for i in range(len(osi_layers)):
        f.write(f"""    {i+1})
        selection="${{osi_layers[{i}]}}"
        motcle=$(echo $selection | cut -d'-' -f2-)
        motcle_normalize=$(normalize_string "$motcle")
        echo "Vous avez choisi : $motcle"
        echo
        grep -i "$motcle_normalize" /home/$USER/cheatsheet/*
        ;;
""")

    f.write("""    *) echo "Choix invalide" ;;
  esac

elif [ "$choix" = "3" ]; then
  echo "Types d'attaque disponibles :"
  for attaque in "${attaques[@]}"; do echo "$attaque"; done
  read -p "Choisissez un type d'attaque : " attaque_choix
  case $attaque_choix in
""")

    for i in range(min(20, len(attaques_formatees))):
        f.write(f"""    {i+1})
        selection="${{attaques[{i}]}}"
        motcle=$(echo $selection | cut -d'-' -f2-)
        motcle_normalize=$(normalize_string "$motcle")
        echo "Vous avez choisi : $motcle"
        echo
        grep -i "$motcle_normalize" /home/$USER/cheatsheet/*
        ;;
""")

    f.write("""    *) echo "Choix invalide" ;;
  esac

else
  echo "Option invalide."
fi
""")

print("Le script Bash avec grep intégré a été généré sous le nom 'menu_interactif.sh'")

