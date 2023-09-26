from flask import Flask, jsonify


app = Flask(__name__)

# Hello world avec Flask

## Exercice 1
@app.route("/about")
def about():
    return "<b>Tutoriel Flask - routes et pages</b>"


# Pages statiques et dynamiques
@app.route("/utilisateur/")
@app.route("/utilisateur/<int:id>")
def profil_utilisateur(id=None):
    if id is None:
        return "Ceci est la page de profil par défaut."
    else:
        return f"Ceci est la page de profil pour l'utilisateur {id}."


## Exercice 1
@app.route("/num")
@app.route("/num/<int:x>")
def num(x):
    if x is None:
        return ("Veuillez fournir un nombre entier.<br>Exemple d'utilisation : "
                "<a href='http://localhost:5000/num/42'>"
                "http://localhost:5000/num/42</a>")
    return str(x)


## Exercice 2
@app.route("/pair/<x>")
def pair(x):
    if not x.isdigit():
        return f"{x} n'est pas valide"
    elif int(x) % 2 == 0:
        return f"{x} est pair"
    else:
        return f"{x} n'est pas pair"


## Exercice 3
@app.route("/somme/<int:x>/<int:y>")
def somme(x, y):
    return str(x + y)


## Exercice 4
@app.route("/factorielle/<int:x>")
def factorielle(x):
    if x > 100:
        return f"{x} est trop grand 💣"

    f = 1
    for i in range(1, x + 1):
        f = f * i
    return str(f)


# Types de retours de vues
@app.route("/liste")
def retourner_liste():
    ma_liste = [1, 2, 3, 4, 5]
    return jsonify(ma_liste)


@app.route("/dictionnaire")
def retourner_dictionnaire():
    mon_dictionnaire = {"nom": "Guillaume",
                        "âge": 38,
                        "ville": "Rouen"}
    return jsonify(mon_dictionnaire)


## Exercice 1
@app.route('/')
def home_html():
    html_content = """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Flask Tutorial | Routes and pages</title>
    </head>
    <body>
        Hello, world !
    </body>
    </html>
    """
    return html_content


if __name__ == "__main__":
    app.run(debug=True)
