# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
import random

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
stalphabet = ['A', 'C', 'D', 'F', 'G', 'I', 'K', 'L',
              'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W']

states = {
    'A': ["Alabama", "Alaska", "Arizona", "Arkansas"],
    'C': ["California", "Connecticut"],
    'D': ["Delaware"],
    'F': ["Florida"],
    'G': ["Georgia"],
    'H': ["Hawaii"],
    'I': ["Idaho", "Illinois", "Indiana", "Iowa"],
    'K': ["Kansas", "Kentucky"],
    'L': ["Louisiana"],
    'M': ["Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana"],
    'N': ["Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota"],
    'O': ["Ohio", "Oklahoma", "Oregon"],
    'P': ["Pennsylvania"],
    'R': ["Rhode Island"],
    'S': ["South Carolina", "South Dakota"],
    'T': ["Tennessee", "Texas"],
    'U': ["Utah"],
    'V': ["Vermont", "Virginia"],
    'W': ["Washington", "West Virginia", "Wisconsin", "Wyoming"]
}

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/disneymovies', methods=['GET', 'POST'])
def disneymovies():
    if request.method == 'POST':
        R = random.randint(0, 25)
        randomletter = alphabet[R]
        return render_template("disneymovies.html", randomletter=randomletter)


@app.route('/disneyresults', methods=['GET', 'POST'])
def disneyresults():
    if request.method == 'POST':
        movie = request.form['movie']
        print(movie[0])
        return "Hello"


@app.route('/colors', methods=['GET', 'POST'])
def colors():
    if request.method == 'POST':
        R = random.randint(0, 25)
        randomletter = alphabet[R]
        return render_template("colors.html", randomletter=randomletter)


@app.route('/colorsresults', methods=['GET', 'POST'])
def colorsresults():
    if request.method == 'POST':
        colors = request.form['colors']
        print(colors[0])
        return "Hello"


@app.route('/countries', methods=['GET', 'POST'])
def countries():
    if request.method == 'POST':
        R = random.randint(0, 25)
        randomletter = alphabet[R]
        return render_template("countries.html", randomletter=randomletter)


@app.route('/countriesresults', methods=['GET', 'POST'])
def countriesresults():
    if request.method == 'POST':
        countries = request.form['countries']
        print(countries[0])
        return "Hello"


@app.route('/fruits', methods=['GET', 'POST'])
def fruits():
    if request.method == 'POST':
        R = random.randint(0, 25)
        randomletter = alphabet[R]
        return render_template("fruits.html", randomletter=randomletter)


@app.route('/fruitsresults', methods=['GET', 'POST'])
def fruitsresults():
    if request.method == 'POST':
        fruits = request.form['fruits']
        print(fruits[0])
        return "Hello"


@app.route('/musicalartists', methods=['GET', 'POST'])
def musicalartists():
    if request.method == 'POST':
        R = random.randint(0, 25)
        randomletter = alphabet[R]
        return render_template("musical_artists.html", randomletter=randomletter)


@app.route('/musicalartistsresults', methods=['GET', 'POST'])
def musicalartistsresults():
    if request.method == 'POST':
        musicalartists = request.form['musicalartists']
        print(musicalartists[0])
        return "Hello"


@app.route('/USStates', methods=['GET', 'POST'])
def US_States():
    if request.method == 'POST':
        st = random.randint(0, 18)
        randomletter = stalphabet[st]
        return render_template("US_States.html", randomletter=randomletter)


@app.route('/USStatesresults', methods=['GET', 'POST'])
def USStatesresults():
    if request.method == 'GET':
        return "Error"
    else:
        X = request.form['states']
        state = states[X[0]]
        for any in state:
            if any == X:
                return "Correct"
        return "Not correct"

