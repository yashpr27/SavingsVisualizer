from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

"""
Flask = framework for running dynamic websites
@app is a decorator for running certain methods when a certain URL is given
"/" represents base url
"""