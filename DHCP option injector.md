# DHCP option injector
## COUCHE 3


### Usurpation

#### ATTAQUE = DHCP Client Spoofing

##### CONFIDENTIALITE
##### INTEGRITE
##### DISPONIBILITE

Description

Usurper le DHCP pour que les clients passent par l'attaquant.

Source

https://github.com/misje/dhcpoptinj

``` 

sudo dhcpoptinj -d -f -q 42 -o'<code à injecter>'
``` 
