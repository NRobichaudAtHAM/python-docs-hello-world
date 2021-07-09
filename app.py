from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "why wont this damn thing work!?!?!?!?"
