# VLAN Hopping
## COUCHE 2

### Usurpation
### Contournement

#### ATTAQUE = VLAN HOPPING

##### CONFIDENTIALITE
##### INTEGRITE

**Description** :
Technique permettant à un attaquant de générer du trafic sur un VLAN non autorisé, souvent via des attaques comme "switch spoofing" ou "double tagging".

## Déroulé de l’attaque (PoC)

### 1. Cible visée  
Un réseau avec plusieurs VLANs mal segmentés et des ports switch configurés de manière permissive (mode trunk activé sur ports non maîtrisés).

### 2. Switch Spoofing

#### Objectif :  
Faire croire au switch que l’attaquant est un autre switch légitime.

#### Exemple avec Yersinia (Linux) :
```bash
sudo yersinia -I
```
Naviguer dans l’interface et lancer une attaque **DTP (Dynamic Trunking Protocol)** pour activer le mode trunk sur le port connecté à l’attaquant.

Résultat : le switch place le port en trunk et l’attaquant peut envoyer/recevoir du trafic sur plusieurs VLANs.

### 3. Double Tagging

#### Objectif :  
Insérer deux balises VLAN (802.1Q) dans une trame Ethernet.

#### Exemple de trame :
- VLAN externe : 1 (port natif)
- VLAN interne : 10 (cible)

La première balise est retirée par le premier switch (trunk natif), la deuxième est traitée par le switch suivant, qui redirige la trame vers le VLAN cible.

> Cette attaque ne nécessite pas de port en mode trunk, mais repose sur une mauvaise configuration du VLAN natif.

---

## Défense

- Désactiver **DTP** sur tous les ports non trunk :
```bash
switchport mode access
switchport nonegotiate
```

- Ne jamais utiliser le VLAN 1 par défaut pour le trafic utilisateur
- Séparer le VLAN natif des VLANs utilisés
- Filtrer les balises VLAN inhabituelles sur les ports d’accès
- Activer des mécanismes comme **BPDU Guard**, **Port Security**, **Dynamic ARP Inspection**

---

## Sources

- https://www.geeksforgeeks.org/vlan-hopping-attack/  
- https://www.cisco.com/c/en/us/support/docs/lan-switching/802-1q/12063-3.html
