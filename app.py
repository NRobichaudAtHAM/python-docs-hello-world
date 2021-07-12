from flask import Flask, url_for, request, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "ya done goofed, this is not a page."

@app.route("/home")
def homescreen():
    return render_template("home_page.html")

#with app.test_request_context():