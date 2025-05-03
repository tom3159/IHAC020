# Nmap - Couche 4 (Transport)
## COUCHE 4

### Observation
### Contournement

#### ATTAQUE = SCAN DE PORTS TCP/UDP

##### CONFIDENTIALITÉ
##### INTÉGRITÉ

**Description** :
Nmap est capable de scanner les ports TCP (SYN scan, connect scan) et UDP pour déterminer les services ouverts sur une machine cible.

**Exemples de commandes** :
```
nmap -sS 192.168.1.1
nmap -sT 192.168.1.1
nmap -sU 192.168.1.1
```

**Source** : https://nmap.org/book/man-port-scanning-techniques.html
