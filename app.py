from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug="True")

"""
NOTES:
Flask = framework for running dynamic websites

@app is a decorator for running certain methods when a certain URL is given
"/" represents base url

By convention, Flask directory's should have static/ and templates/ for
non-html and html files respectively.
Within static/, ppl add css/, javascript/, images/, etc. sub-directories.

render_template(str:filepath) lets you render an html file located in templates/
You can use this function to pass variables into html file (ask gpt to explain this)

Important: Python files (like app.py) should be within main directory (Never in sub-directories.)

Type flask run in terminal to load up app server. Make sure to be in main directory.
"""