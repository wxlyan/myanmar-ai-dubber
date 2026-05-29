from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Myanmar AI Dubber is running!"
