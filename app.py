from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Server is up!"

@app.route("/nds")
def say_hello():
    return "Hello, World!"
