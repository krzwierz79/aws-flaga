import random
from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from programs.passgen import passgen
from programs.wiki_search import wiki_search
from programs.friends_game import read_riddle
from programs.ffriends import read_ffriend

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

@app.route('/draft-dla-ukrainy', methods=['GET', 'POST'])
def draft():    
    # answer = None
    show = None
    if request.method == 'POST':
        if request.form['submit_button'] == 'Do Something':
            pass # do something
        elif request.form['submit_button'] == 'Do Something Else':
            pass # do something else
        else:
            pass # unknown
    elif request.method == 'GET':
        entry, mean_1, mean_2, answer = read_riddle()
        return render_template("ukr-draft.html",
        entry = entry,
        mean_1 = mean_1, 
        mean_2 = mean_2,
        answer = answer,
        show = show)


@app.route('/flaga-dla-ukrainy')
def ukr():
    ukrainian = random.choice(['Ukrainian Falcons', 'Ukrainian Levkoy', 'Ukrainian alphabet'])
    from_wiki = wiki_search(ukrainian).encode('utf-8').decode()
    pl_word, ua_word, pl_mean, ua_mean = read_ffriend('/var/www/flaga/dane/ffriends_pl_ua.csv')
    return render_template("ukr.html", 
    to_page = from_wiki,
    pl_word = pl_word, 
    ua_word = ua_word, 
    pl_mean = pl_mean, 
    ua_mean = ua_mean)

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
