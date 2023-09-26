from flask import Flask, jsonify


app = Flask(__name__)


# Hello world in Flask

## Exercice 1
@app.route("/about")
def about():
    return "<b>Flask Tutorial - routes and pages</b>"

# Static and dynamic pages
@app.route("/user/")
@app.route("/user/<int:id>")
def user_profile(id=None):
    if id is None:
        return "This is the default profile page."
    else:
        return f"This is the profile page for user {id}."


## Exercice 1
@app.route("/num")
@app.route("/num/<int:x>")
def num(x=None):
    if x is None:
        return ("Please provide an integer number.<br>Ex. usage: "
                "<a href='http://localhost:5000/num/42'>"
                "http://localhost:5000/num/42</a>")
    return str(x)


## Exercice 2
@app.route("/even/<x>")
def even(x):
    if not x.isdigit():
        return f"{x} is not valid"
    elif int(x) % 2 == 0:
        return f"{x} is even"
    else:
        return f"{x} is not even"


## Exercice 3
@app.route("/sum/<int:x>/<int:y>")
def sum(x, y):
    return str(x + y)


## Exercice 4
@app.route("/fat/<int:x>")
def fat(x):
    if x > 100:
        return f"{x} is too big"

    f = 1
    for i in range(1, x + 1):
        f = f * i
    return str(f)


# View return types
@app.route("/list")
def return_list():
    my_list = [1, 2, 3, 4, 5]
    return jsonify(my_list)


@app.route("/dict")
def return_dict():
    my_dict = {"name": "John",
               "age": 30,
               "city": "New York"}
    return jsonify(my_dict)


## Exercice 1
@app.route("/")
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Flask Tutorial | Routes and pages</title>
    </head>
    <body>
        Hello, world!
    </body>
    </html>
    """
    return html_content


if __name__ == "__main__":
    app.run(debug=True)
