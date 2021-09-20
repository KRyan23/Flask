#import the flask class - Flask with uppercase at the start indicates a 'class'
import os
from flask import Flask
#Create an instance of the app
app = Flask(__name__)

#use the route decorator to tell the function what url will trigger the function that follows
@app.route("/")

#Create a function called, that just returns the string 'hello world'
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run(
    host=os.environ.get("IP", "0.0.0.0"),
    port=int(os.environ.get("PORT", "5000")),
    debug=True)
    #!Important only have debug=True when you are building and testing the app, set it to false on project submission