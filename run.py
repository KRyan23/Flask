#import the flask class - Flask with uppercase at the start indicates a 'class', render_template is needed to allow you import a html file in this case index.html
import os
from flask import Flask, render_template
#Create an instance of the app
app = Flask(__name__)

#use the route decorator to tell the function what url will trigger the function that follows
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")

#Create a function called, that just returns the string 'hello world'
def index():
    return render_template("index.html")
#render_template expects to see a folder in the same directory as the run.py file with a name 'templates' and from there access any html files

if __name__ == "__main__":
    app.run(
    host=os.environ.get("IP", "0.0.0.0"),
    port=int(os.environ.get("PORT", "5000")),
    debug=True)
    #!Important only have debug=True when you are building and testing the app, set it to false on project submission

# Put the following code in a html file and this will create a new template, try this as next elarning step
#
# {% extends "base.html" %}
# {% block content %}
#    <h1>Come Work With Us!</h1>
# {% endblock %}
#
# Then just update the index.html with the new page link in the <li> section