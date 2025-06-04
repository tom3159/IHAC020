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

5. **PREREQUIS** Le logiciel fait appelle a python l'environment virtuelle et des librairie OPENPYXL et PANDAS. si ce n'est pas déja fait installer les en fonction de vos distribution


---
## Utilisation de l’outil
Lancer votre environement virtuel python
### Exemple non contractuel
   ```
   #exemple pour les ubuntu et kali linux avec python déja installer
   python3 -m venv venv
   source venv/bin/activate
   pip install pandas openpyxl
   python3 generate_menu.py
   ```
### Lancemment du python pour generer le fichier
```
python3 generate_menu.py
```

À la fin, le script genere automatiquement `menu_interactif.sh`.
render le executable
```
chmod +x menu_interactif.sh
```

Pour relancer l’outil ultérieurement :
```
.\menu_interactif.sh
```
## Exemples


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
glow FICHIER.MD
```
---
---


## Contribution

Pour toute contribution, veuillez suivre le modèle fourni et respecter la structure des fichiers.

---
N’hésitez pas à nous contacter pour toute question ou suggestion d’amélioration.

---
> *Bonne utilisation !*


## Explication
En entrée : Nous sommes partis d’un fichier Excel.
Nous nous sommes servis de bibliothèques Python pour générer un menu qui s’adapte au contenu du fichier.

En sortie : Nous obtenons un script qui effectue des recherches avec grep pour identifier les types de risques, les différentes couches du modèle OSI et les critères de sécurité.
On peut effectuer des recherches simples ou combinées.

Aujourd’hui, grâce à la première séance du cours, nous avons alimenté au moins une cheat sheet par couche du modèle OSI.
Chaque cheat sheet nous fournit les commandes de base ainsi que les liens officiels pour exploiter les outils.
