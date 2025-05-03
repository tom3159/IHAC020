# Nmap - Couche 5 (Session)
## COUCHE 5

### Observation

#### ATTAQUE = DÉTECTION DE SERVICES DE SESSION (SMB, RPC)

##### CONFIDENTIALITÉ

**Description** :
Nmap permet de découvrir les services réseau gérant des sessions comme SMB, NetBIOS ou RPC, souvent utilisés dans les réseaux Windows.

**Exemples de commandes** :
```
nmap -p 139,445 --script=smb-os-discovery 192.168.1.10
nmap -sU -p 137 --script nbstat.nse 192.168.1.10
```

**Source** : https://nmap.org/nsedoc/scripts/smb-os-discovery.html
