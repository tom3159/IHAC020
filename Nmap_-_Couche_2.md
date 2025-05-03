# Nmap - Couche 2 (Liaison de données)
## COUCHE 2

### Observation

#### ATTAQUE = DÉTECTION DE MATÉRIEL PAR ADRESSE MAC

##### CONFIDENTIALITÉ

**Description** :
À la couche liaison de données, Nmap permet de détecter les adresses MAC via des requêtes ARP (dans un réseau local). Cela permet d’identifier les équipements actifs.

**Exemples de commandes** :
```
nmap -sn 192.168.1.0/24
```

Cette commande utilise ARP pour découvrir les hôtes actifs dans le réseau local.

**Source** : https://nmap.org/book/man-host-discovery.html
