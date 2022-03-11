import random
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from programs.passgen import passgen
from programs.wiki_search import wiki_search

# app instance
app=Flask(__name__)

# secret for flask_wtf
app.config['SECRET_KEY'] = "soooo secret"

# form class
class InputForm(FlaskForm):
    name = StringField("How many chars?", validators=[DataRequired()])
    submit = SubmitField("Generate")

@app.route('/')
def index():
    text = open('dane/xd.txt').read()
    return render_template("index.html", text=text)

@app.route('/xd')
def xd():
    return render_template("xd.html")

@app.route('/flaga-dla-ukrainy')
def ukr():
    ukrainian = random.choice(['Ukrainian Falcons', 'Ukrainian Levkoy', 'Ukrainian alphabet'])
    from_wiki = wiki_search(ukrainian).encode('utf-8').decode()
    return render_template("ukr.html", to_page = from_wiki)

@app.route('/password', methods=['GET', 'POST'])
def password():
    ready_pass = None
    name = None
    form = InputForm()
    if form.validate_on_submit():
        name = int(form.name.data)
        ready_pass = passgen(name) # ???(name).encode('utf-8').decode()
        form.name.data = ''

    return render_template("pass.html", 
        password=ready_pass,
        name = name,
        form = form)

if __name__=="__main__":
    app.run()
