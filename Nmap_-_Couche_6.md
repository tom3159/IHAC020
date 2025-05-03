# Nmap - Couche 6 (Présentation)
## COUCHE 6

### Observation

#### ATTAQUE = DÉTECTION DE CHIFFREMENT SSL/TLS

##### CONFIDENTIALITÉ

**Description** :
À la couche de présentation, Nmap peut identifier les versions des protocoles de chiffrement (SSL/TLS) utilisées, ce qui permet de repérer des faiblesses potentielles.

**Exemples de commandes** :
```
nmap -p 443 --script ssl-enum-ciphers 192.168.1.10
```

**Source** : https://nmap.org/nsedoc/scripts/ssl-enum-ciphers.html
