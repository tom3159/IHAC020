# NMAP
## COUCHE 4

### Inaccessibilité des informations chiffrées, Observation

#### ATTAQUE = nmap XMAS attack

##### CONFIDENTIALITE

Description 

envoie des paquets TCP avec les flags PSH, URG et FIN activés à l'IP cible. Ce scan est souvent utilisé pour contourner certains pare-feu ou systèmes de détection, mais il peut être plus facilement détecté par des systèmes modernes.  

 

Source  

https://nmap.org/book/scan-methods-null-fin-xmas-scan.html 

https://cheatography.com/romelsan/cheat-sheets/nmap-basics/ 


``` 

nmap -sX <IP_cible>
``` 