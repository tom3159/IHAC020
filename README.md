# IHAC020 – TP FX IPI

**Auteurs** : Thomas, Johan, Axel, Chihab

---
Bienvenue dans ce projet ! Ce dépôt contient tous les fichiers nécessaires pour travailler efficacement sur l’analyse des risques liés aux biens.

---
## Installation et préparation

1. **Téléchargez l’ensemble du répertoire**.  
   Vous y trouverez tous les fichiers `.md` existants.

2. **Pour rédiger un nouveau fichier** :  
   Utilisez le modèle `Template_MD.txt`.

3. **Nommez chaque fichier** selon le nom de l’attaque, avec l’extension `.md`.

4. **Supprimez les lignes inutiles** dans vos fichiers.

5. **PREREQUIS** Le logiciel fait appelle a python l'environment virtuelle et des librairie. si ce n'est pas déja fait voici ce que vous pouvez executer sur une machine de type UBUNTU

```
# 1. Mettre à jour le système
sudo apt update && sudo apt upgrade -y

# 2. Installer les outils nécessaires
sudo apt install -y wget build-essential libssl-dev zlib1g-dev \
libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev \
libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev tk-dev \
uuid-dev libffi-dev curl git

# 3. Télécharger et compiler Python 3.12
cd /usr/src
sudo wget https://www.python.org/ftp/python/3.12.3/Python-3.12.3.tgz
sudo tar xvf Python-3.12.3.tgz
cd Python-3.12.3
sudo ./configure --enable-optimizations
sudo make -j$(nproc)
sudo make altinstall

# 4. Vérifier que Python 3.12 est bien installé
python3.12 --version

# 5. Créer et activer l’environnement virtuel IHAC020
cd ~  # ou dans le dossier de ton projet
python3.12 -m venv IHAC020
source IHAC020/bin/activate

# 6. Mettre pip à jour et installer les bibliothèques nécessaires
pip install --upgrade pip
pip install pandas openpyxl

```
---
## Utilisation de l’outil

Après avoir récupéré le script et les fichiers `.md`, rendez les scripts exécutables :
```
chmod +x ins_prerequis_offline.sh
chmod +x install.sh
```
> Les scripts utilisent du code Python et sont lancés dans un environnement virtuel.  
> Nous avons fourni les prérequis pour une machine Ubuntu.  
> Les dépendances sont disponibles dans le dossier `Deps`.
> le menu interactif se base sur le fichier Excel `Analyse_Risques_Biens.xlsx`. 
 
Lancez ensuite les scripts :
Pour la première utilisation, lancez également (si vous etes sous Ubuntu) :
```
.\ins_prerequis_offline.sh
```
il faudra lancer aussi une premiére fois
```
.\install.sh
```
À la fin, le script lancera automatiquement `menu_interactif.sh`.

Pour relancer l’outil ultérieurement :
```
.\menu_interactif.sh
```


---

## Fonctionnalités du menu interactif

Le menu vous propose de rechercher par :

- **Type de risque**
- **Couche du modèle OSI**
- **Critère de sécurité**

Laissez-vous guider par les instructions à l’écran.

---
## Vous pouraient ensuite lire les fiches avec le reader MD de votre choix

Ici un exemple d'outils que vous pouvez telecharger :
```
sudo snap install glow
```
```
glown FICHIER.MD
```
---
---


## Contribution

Pour toute contribution, veuillez suivre le modèle fourni et respecter la structure des fichiers.

---
N’hésitez pas à nous contacter pour toute question ou suggestion d’amélioration.

---
> *Bonne utilisation !*


