# Flask Tutorial - Routes and pages


## Project structure

```
📁 tut01
 ▙ tut01.py
```

## Hello world in Flask

```Python
from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, world!"


if __name__ == "__main__":
    app.run(debug=True)
```

### Exercices

<hr>

#### 1 - Create "about" page

Modify the code above to create an "about" page accesible at [localhost:5000/about](http://localhost:5000/about). This page should display "Flask Tutorial - routes and pages" in bold.

##### Tips

💡 Remeber that you can use HTML tags.

## Static and dynamic pages

```Python
from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    return f"This is a static page."


@app.route("/page")
def static_page():
    return f"This is <b>also</b> a static page."


if __name__ == "__main__":
    app.run(debug=True)
```

```Python
@app.route("/<page>")
@app.route("/<page>/<subpage>")
def dynamic_page(page, subpage=None):
    if subpage == None:
        return f"You are accessing page {page}."
    else:
        return f"You are accessing page {page}, subpage {subpage}."
```

### Exercises

<hr>

#### 1 - Display page names in **bold** and in UPPERCASE

Modify the `dynamic_page` view to display the `page` and the `subpage` names in UPPERCASE and in **bold**.

##### Requirements

👉 Acessing [localhost:5000/flask/routes](http://localhost:5000/flask/routes) should display:

You are accessing page **FLASK**, subpage **ROUTES**.

##### Tips
💡 Use Python to covert a `str` to uppercase.

<hr>

#### 2 - Numerical pages `<URL>`

Create a page called `num` with a subpage that only accepts integer values such as 0, 1, 2, etc. This page should display the string representation of this number.

##### Requirements

👉 Accessing [localhost:5000/num/1](http://localhost:5000/num/1) should display:

1

##### Tips
💡 Use the `str()` function to convert an `int` to `str` in Python.

##### What happens?
❔ What happens if you try to access the page [localhost:5000/int](http://localhost:5000/int)? Can you explain it? Try to solve this error by adding a second `@app.route("/int")` with instructions on how to use it correctly.

##### Errors
🚨 If your page shows a **TypeError** message, it probably means that your view is not returning a `str`. Try converting the output to `str` before returning it.

🚨 If your page shows an **AttributeError** message, it probably means that your URL address is not being handled by the correct view. Check the `@app.route()` rules.


<hr>

#### 3 - Even

Create a page called `even` with a subpage **x** and displays "x is even" if x is an even number, "x is not even" if x is not an even number and "x is not valid" if x is not an integer.

##### Requirements

👉 Acessing [localhost:5000/even/1](http://localhost:5000/even/1) should display:

1 is not even

👉 Acessing [localhost:5000/even/2](http://localhost:5000/even/2) should display:

2 is even

👉 Accessing [localhost:5000/even/a](http://localhost:5000/even/a) should display:

a is not valid

##### Tips
💡 Use an `if` statement to return the correct response.

💡 Use `x.isdigit()` to check if a `str` represents an integer number.

💡 Use `int()` to convert a `str` to `int`.

<hr>

#### 4 - Sum page

Create a page called `sum` with two subpages **x** and **y** that displays the result of **x + y**.

##### Requirements

👉 Accessing [localhost:5000/sum/1/1](http://localhost:5000/sum/1/1) should display:

2

##### What happens?
❔ What happens if you try to access the page [localhost:5000/sum/a/b](http://localhost:5000/sum/a/b)? Try to solve this issue by only allowing integer subpages.

<hr>

#### 5 - Factorial page

Create a page called `fat` with an integer subpage **x** that displays the factorial of **x**. Also, if **x** is greater than 100, the page should display "x is too big".

##### Requirements

👉 Accessing [localhost:5000/fat/5](http://localhost:5000/fat/5) should display:

120

👉 Accessing [localhost:5000/fat/1000](http://localhost:5000/fat/1000) should display:

1000 is too big
