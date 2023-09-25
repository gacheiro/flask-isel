# Tutoriel Flask - Routes et pages

[Flask](https://flask.palletsprojects.com/en/2.3.x/) est un micro-framework web pour Python qui vous permet de créer rapidement des applications web. Dans ce tutoriel, nous allons vous guider à travers le processus de création d'une simple page "Hello, world !" en utilisant Flask, et de la définition de pages statiques et dynamiques dans une application web Flask.

## Pour commencer

Avant de commencer, assurez-vous d'avoir Flask installé. Si ce n'est pas le cas, vous pouvez installer la dernière version `2.3.3` en utilisant pip :

```bash
pip install Flask==2.3.3
```

Maintenant, plongeons dans le code.

## Structure du projet

Assurez-vous de créer un dossier vide nommé `tut01`. À l'intérieur de ce dossier, placez un fichier Python vide nommé `tut01.py`.

```
📁 tut01
 ▙ tut01.py
```

## Hello world avec Flask

Dans le fichier nommé `tut01.py`, écrivez le code Python suivant :

```Python
from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, world !"


if __name__ == "__main__":
    app.run(debug=True)
```

Le code `tut01.py` est expliqué comme suit :

1. Nous commençons par importer la classe Flask du module flask. Flask est basé sur l'idée de créer une instance de cette classe pour exécuter votre application web.

2. Nous créons une instance d'application Flask nommée `app`.

3. En utilisant le décorateur @app.route("/"), nous définissons une route pour l'URL racine ("/"). Lorsqu'un utilisateur visite l'URL racine de votre application web, Flask invoquera la fonction home().

4. À l'intérieur de la fonction `home()`, nous retournons simplement la chaîne `"Hello, world !"` en tant que réponse. Cette réponse sera renvoyée au navigateur web du client.

5. Enfin, nous vérifions si le script est exécuté directement (non importé en tant que module). Si c'est le cas, nous démarrons le serveur de développement Flask avec `app.run(debug=True)`. L'option `debug=True` active le mode débogage, ce qui est utile pendant le développement car il fournit des messages d'erreur détaillés et recharge automatiquement le serveur lorsque vous apportez des modifications au code.

Vous devriez être en mesure d'accéder à votre site à [localhost:5000](http:/localhost:5000) 🔥

### Exercices

<hr>

#### 1 - Créer la page "À propos"

Modifiez le code ci-dessus pour créer une page "À propos" accessible à [localhost:5000/about](http://localhost:5000/about). Cette page devrait afficher "Tutoriel Flask - routes et pages" en gras.

##### Conseils

💡 N'oubliez pas que vous pouvez utiliser des balises HTML dans la réponse sous forme de chaîne.

## Pages statiques et dynamiques

Dans une application web Flask, vous pouvez créer à la fois des pages statiques et dynamiques pour servir différents types de contenu aux utilisateurs.

### Pages statiques

Les pages statiques sont celles dont le contenu ne change pas ou est le même pour tous les utilisateurs. Elles sont définies par des routes fixes dans votre application Flask. Voici un exemple :

```Python
@app.route("/")
def home():
    return "Ceci est une page statique."
```
Dans cet exemple, le décorateur `@app.route("/")` spécifie que lorsqu'un utilisateur accède à l'URL racine du site web (par exemple, "http://localhost:5000/"), il verra le message "Ceci est une page statique." Les pages statiques sont utiles pour afficher des informations cohérentes à tous les utilisateurs, telles qu'une page d'accueil ou une page "À propos".

Vous pouvez également inclure des balises HTML dans votre réponse pour formater le contenu, comme le montre la deuxième page statique :

```Python
@app.route("/page")
def static_page():
    return "Ceci est une page <b>aussi</b> statique."
```

Cette route, définie par `@app.route("/page")`, affiche le message : "Ceci est une page <b>aussi</b> statique." Elle utilise la balise `<b>` HTML pour mettre en gras le mot "aussi".

Le code fourni est une application Flask de base qui montre comment créer des pages statiques avec Flask. Elle définit deux routes :

1. La route racine ("/") associée à la fonction home, qui affiche un message statique.
2. La route "/page" associée à la fonction static_page, qui affiche un autre message statique avec une mise en forme HTML.


### Pages dynamiques

D'un autre côté, les pages dynamiques peuvent générer du contenu en fonction de l'entrée de l'utilisateur ou d'autres variables. Ces pages ont généralement des routes dynamiques, ce qui signifie que certaines parties de l'URL peuvent changer, affectant le contenu affiché.

Pour créer des pages dynamiques, vous pouvez utiliser des paramètres de route. Par exemple, pour créer une page de profil utilisateur dynamique avec un ID utilisateur en tant que paramètre, vous pourriez définir une route comme ceci :

```Python
@app.route("/utilisateur/<int:id>")
def profil_utilisateur(id):
    return f"Ceci est la page de profil pour l'utilisateur {id}."
```

Dans ce code, la partie `<int:id>` de la route indique que `id` est un paramètre dynamique pouvant prendre une valeur entière. Lorsqu'un utilisateur accède à une URL comme "[localhost:5000/utilisateur/1](http://localhost:5000/utilisateur/1)", le paramètre `id` est transmis à la fonction profil_utilisateur, qui affiche "Ceci est la page de profil pour l'utilisateur 1."

Vous pouvez ajouter des sections variables à une URL en marquant ces sections avec `<nom_variable>`. Votre fonction reçoit ensuite `<nom_variable>` en tant qu'argument de mot-clé. Facultativement, vous pouvez utiliser un convertisseur pour spécifier le type de l'argument comme `<convertisseur:nom_variable>` où le convertisseur peut être l'un des suivants :

| Convertisseur | Description |
|-----------|-------------|
| `string`  | (par défaut) accepte n'importe quel texte sans barre oblique |
| `int`     | accepte des entiers positifs |
| `float`   | accepte des valeurs flottantes positives |
| `path`    | comme `string` mais accepte également des barres obliques |
| `UUID`    | accepte des chaînes UUID |

### Exercices

<hr>

#### 1 - Pages numériques `<URL>`

Créez une page appelée `num` avec une sous-page n'acceptant que des valeurs entières telles que 0, 1, 2, etc. Cette page devrait afficher la représentation en chaîne de caractères de ce nombre.

##### Exigences

👉 L'accès à [localhost:5000/num/1](http://localhost:5000/num/1) devrait afficher :

1

##### Conseils
💡 Utilisez la fonction `str()` pour convertir un `int` en `str` en Python.

##### Que se passe-t-il ?
❔ Que se passe-t-il si vous essayez d'accéder à la page [localhost:5000/int](http://localhost:5000/int) ? Pouvez-vous l'expliquer ? Essayez de résoudre cette erreur en ajoutant une deuxième `@app.route("/num")` avec des instructions sur la manière de l'utiliser correctement.

##### Erreurs
🚨 Si votre page affiche un message de **TypeError**, cela signifie probablement que votre vue ne renvoie pas une chaîne de caractères. Essayez de convertir la sortie en chaîne de caractères avant de la renvoyer.

🚨 Si votre page affiche un message d'**AttributeError**, cela signifie probablement que votre adresse URL n'est pas gérée par la vue correcte. Vérifiez les règles `@app.route()`.

### 2 - Paires

Créez une page appelée `pair` avec une sous-page **x** qui affiche "x est pair" si x est un nombre pair, "x n'est pas pair" si x n'est pas un nombre pair et "x n'est pas valide" si x n'est pas un nombre entier.

##### Exigences

👉 L'accès à [localhost:5000/pair/1](http://localhost:5000/pair/1) devrait afficher :

1 n'est pas pair

👉 L'accès à [localhost:5000/pair/2](http://localhost:5000/pair/2) devrait afficher :

2 est pair

👉 L'accès à [localhost:5000/pair/a](http://localhost:5000/pair/a) devrait afficher :

a n'est pas valide

##### Conseils
💡 Utilisez une déclaration `if` pour renvoyer la réponse appropriée.

💡 Utilisez `x.isdigit()` pour vérifier si une chaîne `str` représente un nombre entier.

💡 Utilisez `int()` pour convertir une chaîne `str` en `int`.

<hr>

### 3 - Page de somme

Créez une page appelée `somme` avec deux sous-pages **x** et **y** qui affiche le résultat de **x + y**.

##### Exigences

👉 L'accès à [localhost:5000/somme/1/1](http://localhost:5000/somme/1/1) devrait afficher :

2

##### Que se passe-t-il ?
❔ Que se passe-t-il si vous essayez d'accéder à la page [localhost:5000/somme/a/b](http://localhost:5000/somme/a/b) ? Essayez de résoudre ce problème en n'autorisant que des sous-pages entières.

<hr>

### 4 - Page de factorielle

Créez une page appelée `factorielle` avec une sous-page entière **x** qui affiche la factorielle de **x**. De plus, si **x** est supérieur à 100, la page devrait afficher "x est trop grand".

##### Exigences

👉 L'accès à [localhost:5000/factorielle/5](http://localhost:5000/factorielle/5) devrait afficher :

120

👉 L'accès à [localhost:5000/factorielle/1000](http://localhost:5000/factorielle/1000) devrait afficher :

1000 est trop grand
