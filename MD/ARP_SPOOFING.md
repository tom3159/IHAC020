# ettercap
## COUCHE 2


### usurpation
### Contournement 
### Déni de services,Divulgation des informations chiffrées
### Observation

#### ATTAQUE = ARP_SPOOFING

##### CONFIDENTIALITE
##### INTEGRITE
##### DISPONIBILITE

Description : Usurper une ip en associant l'ip de l'attaqué avec le mac de l'attaquant, on peut avoir donc dans la table ARP une association ip d'un appareil avec le mac d'un autre appareil.
Source : https://www.kalilinux.fr/commandes/ettercap-sur-kali-linux/

Ajuster la configuration d'Ettercap pour l'empoisonnement ARP
Tout d’abord, mettez à jour le fichier de configuration Ettercap pour générer du trafic vers le superutilisateur.

```
sudo vi /etc/Ettercap/etter.conf
```

Recherchez la section [privs] dans le fichier. Modifiez les deux lignes suivantes.
```
ec_uid = 0 # nobody is the default
ec_gid = 0 # nobody is the default
```

Sauvegarder le fichier.
Mettre en place l'attaque MITM
Notez le routeur de votre réseau. Tapez la commande suivante :
```
ip r
```

Les résultats indiqueront le paramètre par défaut via, puis une adresse IP. Il s'agit de l'adresse du routeur. Notez-la.
Démarrez Ettercap avec son interface graphique front-end. Avec la commande :
```
sudo -E Ettercap -G
```
Dans cette stratégie d'attaque, nous allons faire croire à l'ordinateur de la victime que notre ordinateur est le routeur. L'ordinateur expéditeur connaît déjà l'adresse IP du routeur. Nous ne la modifierons pas. Au lieu de cela, nous allons lier l'adresse MAC de notre ordinateur à cette adresse IP.

Cliquez sur Sniff dans le menu supérieur, puis sélectionnez Unified Sniffing dans le menu déroulant. Vous verrez une boîte de dialogue Ettercap Input. Sélectionnez l'interface réseau qui se trouve sur le même réseau que l'ordinateur cible et appuyez sur OK .
Cliquez sur l' option Hôtes dans le menu supérieur et sélectionnez Rechercher des hôtes dans le menu déroulant. Ensuite, cliquez à nouveau sur l' option Hôtes et choisissez Liste des hôtes . Cela vous montrera les autres appareils connectés au réseau. Tout d'abord, vous devez déterminer lequel de ces ordinateurs est votre ordinateur cible.
La liste des hôtes affiche les adresses IP de tous les ordinateurs connectés au réseau. Cliquez sur la ligne de la cible et cliquez sur le bouton Ajouter à la cible 1. Cliquez ensuite sur l'adresse du routeur du réseau et appuyez sur le bouton Ajouter à la cible 2. Vous pouvez ajouter autant d'adresses Cible 1 que vous le souhaitez. Pour chaque adresse Cible 1 que vous insérez dans cette configuration, l'ordinateur associé à cette adresse IP verra son trafic détourné via l'ordinateur exécutant le système Ettercap. Tous les autres ordinateurs communiqueront avec le routeur de la manière habituelle.
Cliquez sur l' option MITM dans le menu supérieur, puis sur Empoisonnement ARP . Dans la boîte de dialogue qui apparaît, sélectionnez Sniff remote connections (Rechercher les connexions distantes ), puis cliquez sur OK . Cliquez ensuite sur l' option Start (Démarrer) dans le menu supérieur, puis choisissez Start Sniffing (Démarrer la détection). Cela permet de remapper l'adresse IP du routeur sur votre ordinateur. Le système Ettercap transmettra le trafic au routeur réel et canalisera les réponses vers la cible.
Exécutez l'attaque MITM
Vous recevrez désormais tout le trafic de cette machine cible vers le routeur. Toutes les connexions HTTPS seront rétrogradées vers une communication HTTP non protégée.
Dans l'interface Ettercap, cliquez sur l' option Affichage dans le menu supérieur et sélectionnez Connexions dans le menu déroulant. Cliquez ensuite sur une ligne de la liste de connexions affichée dans le panneau central de l'interface pour ouvrir un tableau de bord partagé. Cela vous montrera les données d'en-tête de paquet pour la connexion. Si la charge utile n'est pas chiffrée, vous devez lire le contenu du corps du paquet.

