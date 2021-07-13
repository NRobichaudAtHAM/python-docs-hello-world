from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "ya done goofed, this is not a page."

@app.route("/home")
def homescreen(name=None):
    return render_template("home_page.html", name=name)

@app.route("/blue")
def bluescreen(name=None):
    return render_template("bluepage.html", name=name)

@app.route("/green")
def greenscreen(name=None):
    return render_template("greenpage.html", name=name)

#with app.test_request_context():