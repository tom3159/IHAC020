# Cookie Hijacking
## COUCHE 7

### Usurpation
### Observation

#### ATTAQUE = SESSION HIJACKING PAR COOKIE

##### CONFIDENTIALITE
##### INTEGRITE

**Description** :
Le cookie hijacking permet à un attaquant d'intercepter et de réutiliser un cookie de session pour usurper l'identité de l'utilisateur sur un site web.


## Déroulé de l’attaque (PoC)

### 1.Cible visée  
Un site web non sécurisé (pas de HTTPS ou mal configuré), où les cookies de session sont transmis sans protection.

### 2.Interception via attaque MITM (Man-in-the-Middle)

Exemple avec **Wireshark** ou **tcpdump** sur un réseau Wi-Fi public non sécurisé.

#### Commande avec `tcpdump` :
```bash
sudo tcpdump -i wlan0 -A port 80
```

L'attaquant observe le trafic HTTP et extrait les cookies visibles en clair.

### 3.Récupération du cookie

Exemple d'extrait intercepté :
```
GET /dashboard HTTP/1.1  
Host: victim.com  
Cookie: PHPSESSID=abc123def456
```

### 4. Rejeu du cookie dans un navigateur

Avec un plugin comme **EditThisCookie** ou via les DevTools (onglet "Storage") du navigateur, l'attaquant injecte le cookie volé pour accéder à la session victime.

---

## Défense
- **Utiliser HTTPS uniquement** (force le chiffrement via HSTS)  
- **Attributs de cookie sécurisés** :
```http
Set-Cookie: PHPSESSID=abc123def456; Secure; HttpOnly; SameSite=Strict
```
- **Expiration courte** des cookies + renouvellement de session  
- Surveillance et alerte en cas d’utilisation du même cookie depuis des IPs différentes  

---

## Sources
- https://owasp.org/www-community/attacks/Session_hijacking  
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
