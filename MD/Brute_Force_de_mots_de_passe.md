# Brute Force de mots de passe
## COUCHE 7

### Contournement
### Inaccessibilité

#### ATTAQUE = BRUTE FORCE

##### CONFIDENTIALITE
##### DISPONIBILITE

**Description** :
Tentative systématique de deviner un mot de passe en essayant toutes les combinaisons possibles jusqu'à trouver la bonne.

**Source** : https://owasp.org/www-community/attacks/Brute_force_attack

**Exemple de commande Hydra** :
```
hydra -l admin -P /usr/share/wordlists/rockyou.txt 192.168.1.100 http-get /login
```
