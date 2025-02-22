from flask import Flask, render_template, request
import os
app = Flask(__name__)

# turns on debug mode, allows app to refresh w changes w/o having to reboot server
os.environ['FLASK_ENV'] = 'development'
os.environ['FLASK_DEBUG'] = '1'

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        print(request.form)
        return "Form Submitted!!"



"""
NOTES:
Flask = framework for running dynamic websites

@app is a decorator for running certain methods when a certain http address is supplied
"/" represents https method
methods attr = allows for specifying what type of HTTPS request (GET, POST, etc.) that 
               a certain http address can handle

               
By convention, Flask directory's should have static/ and templates/ for
non-html and html files respectively.
Within static/, ppl add css/, javascript/, images/, etc. sub-directories.

render_template(str:filepath) lets you render an html file located in templates/
You can use this function to pass variables into html file (ask gpt to explain this)

Important: Python files (like app.py) should be within main directory (Never in sub-directories.)

Type flask run in terminal to load up app server. Make sure to be in main directory.
"""