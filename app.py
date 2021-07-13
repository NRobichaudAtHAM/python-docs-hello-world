from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "ya done goofed, this is not a page."

@app.route("/home")
def homescreen():
    return render_template("home_page.html")

@app.route("/blue")
def bluescreen():
    return render_template("bluepage.html")

@app.route("/home")
def greenscreen():
    return render_template("greenpage.html")

#with app.test_request_context():