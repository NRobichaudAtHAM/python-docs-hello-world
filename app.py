from flask import Flask, url_for, request, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "ya done goofed, this is not a page."

@app.route("/home",methods=['GET', 'POST'])
def homescreen():
    if request.method == 'POST':
        if request.form.get('action1') == 'GREEN':
            greenscreen()
        elif  request.form.get('action2') == 'BLUE':
            bluescreen()
        else:
            pass
    elif request.method == 'GET':
        return render_template('home_page.html', form=form)
    
    return render_template("home_page.html")

@app.route("/green",methods=['GET', 'POST'])
def greenscreen():
    if request.method == 'POST':
        if request.form.get('action1') == 'BLUE':
            bluescreen()
        elif  request.form.get('action2') == 'HOME':
            homescreen()
        else:
            pass
    elif request.method == 'GET':
        return render_template('greenpage.html', form=form)
    
    return render_template("greenpage.html")

@app.route("/blue",methods=['GET', 'POST'])
def bluescreen():
    if request.method == 'POST':
        if request.form.get('action1') == 'GREEN':
            greenscreen()
        elif  request.form.get('action2') == 'HOME':
            homescreen()
        else:
            pass
    elif request.method == 'GET':
        return render_template('bluepage.html', form=form)
    
    return render_template("bluepage.html")

#with app.test_request_context():