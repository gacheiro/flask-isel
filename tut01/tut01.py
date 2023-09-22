from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, world!"


@app.route("/about")
def about():
    return "<b>Flask Tutorial - routes and pages</b>"


@app.route("/<page>")
@app.route("/<page>/<subpage>")
def dynamic_page(page, subpage=None):
    page = page.upper()
    subpage = subpage.upper()
    if subpage == None:
        return f"You are accessing page <b>{page}</b>."
    else:
        return (f"You are accessing page <b>{page}</b>, \
                  subpage <b>{subpage}</b>.")


@app.route("/num/<int:x>")
def num(x):
    return str(x)


@app.route("/even/<x>")
def even(x):
    if not x.isdigit():
        return f"{x} is not valid"
    elif int(x) % 2 == 0:
        return f"{x} is even"
    else:
        return f"{x} is not even"


@app.route("/sum/<int:x>/<int:y>")
def sum(x, y):
    return str(x + y)


@app.route("/fat/<int:x>")
def fat(x):
    if x > 100:
        return f"{x} is too big"

    f = 1
    for i in range(1, x + 1):
        f = f * i
    return str(f)


if __name__ == "__main__":
    app.run(debug=True)
