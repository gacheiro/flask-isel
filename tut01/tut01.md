# Flask Tutorial - Routes and pages

[Flask](https://flask.palletsprojects.com/en/2.3.x/) is a popular micro web framework for Python that allows you to quickly build web applications. In this tutorial, we'll walk through the process of creating a simple "Hello, world!" page using Flask, and defining static and dynamic pages in a Flask web application.

## Getting Started

Before you begin, make sure you have Flask installed. If it's not installed, you can install the latest version `2.3.3` using pip:

```bash
pip install Flask==2.3.3
```

Now, let's dive into the code.

## Project structure

Make sure you create an empty folder named `tut01`. Inside that folder, place an empty Python file named `tut01.py`.

```
📁 tut01
 ▙ tut01.py
```

## Hello world in Flask

In a file named `tut01.py`, write the following Python code:

```Python
from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, world!"


if __name__ == "__main__":
    app.run(debug=True)
```

The code `tut01.py` is explained as:

1. We start by importing the Flask class from the flask module. Flask is built around the idea of creating an instance of this class to run your web application.

2. We create a Flask application instance named `app`.

3. Using the @app.route("/") decorator, we define a route for the root URL ("/"). When a user visits the root URL of your web application, Flask will invoke the home() function.

4. Inside the `home()` function, we simply return the string `"Hello, world!"` as the response. This response will be sent back to the client's web browser.

5. Finally, we check if the script is being run directly (not imported as a module). If it is, we start the Flask development server with `app.run(debug=True)`. The `debug=True` option enables debug mode, which is useful during development as it provides detailed error messages and auto-reloads the server when you make code changes.

You should be able to access your site at [localhost:5000](http:/localhost:5000) 🔥

### Exercices

<hr>

#### 1 - Create "about" page

Modify the code above to create an "about" page accesible at [localhost:5000/about](http://localhost:5000/about). This page should display "Flask Tutorial - routes and pages" in bold.

##### Tips

💡 Remeber that you can use HTML tags in the string response.

## Static and dynamic pages

In a Flask web application, you can create both static and dynamic pages to serve different types of content to users.

### Static pages

Static pages are those whose content doesn't change or is the same for all users. They are defined by fixed routes in your Flask application. Here's an example:

```Python
@app.route("/")
def home():
    return "This is a static page."
```
In this example, the `@app.route("/")`` decorator specifies that when a user accesses the root URL of the website (e.g., "http://localhost:5000/"), they will see the message "This is a static page." Static pages are useful for displaying consistent information to all users, such as a homepage or an "About" page.

You can also include HTML tags within your response to format the content, as shown in the second static page:

```Python
@app.route("/page")
def static_page():
    return "This is <b>also</b> a static page."
```

This route, defined by `@app.route("/page")`, displays the message: "This is <b>also</b> a static page." It uses the \<b\> HTML tag to make the word "also" bold.

The provided code is a basic Flask application that demonstrates how to create static pages using Flask. It defines two routes:

1. The root route ("/") mapped to the home function, which displays a static message.
2. The "/page" route mapped to the `static_page` function, which displays another static message with HTML formatting.


### Dynamic pages

Dynamic pages, on the other hand, can generate content based on user input or other variables. These pages typically have dynamic routes, meaning that part of the URL can change, affecting the displayed content.

To create dynamic pages, you can use route parameters. For example, to create a dynamic user profile page with a user ID as a parameter, you could define a route like this:

```Python
@app.route("/user/<int:id>")
def user_profile(id):
    return f"This is the profile page for user {id}."
```

In this code, the `<int:id>` part of the route indicates that `id` is a dynamic parameter that can take an integer value. When a user accesses a URL like "[localhost:5000/user/1](http://localhost:5000/user/1)", the `id` parameter is passed to the `user_profile` function, and it displays "This is the profile page for user 1."

You can add variable sections to a URL by marking sections with `<variable_name>`. Your function then receives the `<variable_name>` as a keyword argument. Optionally, you can use a converter to specify the type of the argument like `<converter:variable_name>` where converter is one of the followings:

| converter | description |
|-----------|-------------|
| `string`  | (default) accepts any text without a slash |
| `int`     | accepts positive integers |
| `float`   | accepts positive floating point values |
| `path`    | like `string` but also accepts slashes |
| `UUID`    | accepts UUID strings |

### Exercises

<hr>

#### 1 - Numerical pages `<URL>`

Create a page called `num` with a subpage that only accepts integer values such as 0, 1, 2, etc. This page should display the string representation of this number.

##### Requirements

👉 Accessing [localhost:5000/num/1](http://localhost:5000/num/1) should display:

1

##### Tips
💡 Use the `str()` function to convert an `int` to `str` in Python.

##### What happens?
❔ What happens if you try to access the page [localhost:5000/int](http://localhost:5000/int)? Can you explain it? Try to solve this error by adding a second `@app.route("/num")` with instructions on how to use it correctly.

##### Errors
🚨 If your page shows a **TypeError** message, it probably means that your view is not returning a `str`. Try converting the output to `str` before returning it.

🚨 If your page shows an **AttributeError** message, it probably means that your URL address is not being handled by the correct view. Check the `@app.route()` rules.


<hr>

#### 2 - Even

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

#### 3 - Sum page

Create a page called `sum` with two subpages **x** and **y** that displays the result of **x + y**.

##### Requirements

👉 Accessing [localhost:5000/sum/1/1](http://localhost:5000/sum/1/1) should display:

2

##### What happens?
❔ What happens if you try to access the page [localhost:5000/sum/a/b](http://localhost:5000/sum/a/b)? Try to solve this issue by only allowing integer subpages.

<hr>

#### 4 - Factorial page

Create a page called `fat` with an integer subpage **x** that displays the factorial of **x**. Also, if **x** is greater than 100, the page should display "x is too big".

##### Requirements

👉 Accessing [localhost:5000/fat/5](http://localhost:5000/fat/5) should display:

120

👉 Accessing [localhost:5000/fat/1000](http://localhost:5000/fat/1000) should display:

1000 is too big
