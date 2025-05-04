# Nmap - Couche 3 (Réseau)
## COUCHE 3

### Observation

#### ATTAQUE = SCAN D’ADRESSES IP ET ICMP

##### CONFIDENTIALITE

**Description** :
Nmap peut effectuer une découverte de réseau (ping scan) pour identifier les hôtes en ligne en envoyant des paquets ICMP Echo, Timestamp, ou Netmask.

**Exemples de commandes** :
```
nmap -PE -sn 10.0.0.0/24
nmap -PP -sn 10.0.0.0/24
nmap -PM -sn 10.0.0.0/24
```

**Source** : https://nmap.org/book/man-host-discovery.html
