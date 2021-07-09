from flask import Flask
app = Flask(__name__)

@app.route("/index")
def index():
    return "ya done goofed, this is not a page."

@app.route("/test_page")
def test_page():
    return "this is a test page!"
