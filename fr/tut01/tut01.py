from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    return "Ceci est une page statique."


@app.route("/page")
def static_page():
    return "Ceci est une page <b>aussi</b> statique."


# Exercise 1
@app.route("/about")
def about():
    return "<b>Tutoriel Flask - routes et pages</b>"


@app.route("/utilisateur/<int:id>")
def profil_utilisateur(id):
    return f"Ceci est la page de profil pour l'utilisateur {id}."


# Exercise 1
@app.route("/num/<int:x>")
def num(x):
    return str(x)


# Exercise 2
@app.route("/pair/<x>")
def pair(x):
    if not x.isdigit():
        return f"{x} n'est pas valide"
    elif int(x) % 2 == 0:
        return f"{x} est pair"
    else:
        return f"{x} n'est pas pair"


# Exercise 3
@app.route("/somme/<int:x>/<int:y>")
def somme(x, y):
    return str(x + y)


# Exercise 4
@app.route("/factorielle/<int:x>")
def factorielle(x):
    if x > 100:
        return f"{x} est trop grand 💣"

    f = 1
    for i in range(1, x + 1):
        f = f * i
    return str(f)


if __name__ == "__main__":
    app.run(debug=True)
