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
calphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'W']
palphabet = ['C', 'E', 'H', 'J', 'M', 'N', 'P', 'S', 'U', 'V']
falphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'W']
colalphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'K',
             'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
presalphabet = ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'L', 'M', 'R', 'T', 'U', 'W', 'Z']

presidentsdict = {
    'A': ["Abraham Lincoln", "Andrew Jackson", "Andrew Johnson"],
    'B': ["Barack Obama", "Benjamin Harrison"],
    'C': ["Calvin Coolidge", "Chester Alan Arthur"],
    'D': ["Donald J. Trump", "Dwight David Eisenhower"],
    'F': ["Franklin Delano Roosevelt", "Franklin Pierce"],
    'G': ["George Washington", "George Herbert Walker Bush", "George W. Bush", "Gerald Rudolph Ford Jr", "Grover Cleveland"],
    'H': ["Harry S Truman", "Herbert Clark Hoover"],
    'J': ["James Abram Garfield", "John Adams", "James Buchanan", " James Earl Carter", "James Madison", "James Monroe", "John Fitzgerald Kennedy", "Joseph R. Biden", "John Quincy Adams", "John Tyler", "James Knox Polk"],
    'L': ["Lyndon Baines Johnson"],
    'M': ["Martin Van Buren", "Millard Fillmore"],
    'R': ["Richard Milhous Nixon", "Ronald Wilson Reagan", "Rutherford Birchard Hayes"],
    'T': ["Theodore Roosevelt", "Thomas Jefferson"],
    'U': ["Ulysses Simpson Grant"],
    'W': ["Warren Gamaliel Harding", "William Henry Harrison", "William Jefferson Clinton", "William Howard Taft", "William McKinley", "Woodrow Wilson"],
    'Z': ["Zachary Taylor"]
}
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

countriesdict = {
    'A': ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia" "Australia", "Austria", "Arzerbaijan"],
    'B': ["Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegonia", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi"],
    'C': ["Cote d'Ivoire", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo", "Costa Rica", "Croatia", "Cuba", "Cypurs", "Czechia"],
    'D': ["Democratic Republic of Congo", "Denmark", "Djibouti", "Dominica", "Dominican Republic"],
    'E': ["Ecuador", "Egypt", "El Salvador", "Equitorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia"],
    'F': ["Fiji", "Finland", "France"],
    'G': ["Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana"],
    'H': ["Haiti", "Holy See", "Honduras", "Hungary"],
    'I': ["Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Isreal", "Italy"],
    'J': ["Jamaica", "Japan", "Jordan"],
    'K': ["Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan"],
    'L': ["Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg"],
    'M': ["Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar"],
    'N': ["Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia", "Norway"],
    'O': ["Oman"],
    'P': ["Pakistan", "Palau", "Palestine State", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal"],
    'Q': ["Qatar"],
    'R': ["Romania", "Russia", "Rwanda"],
    'S': ["Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria"],
    'T': ["Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu"],
    'U': ["Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States of America", "Uruguay", "Uzbekistan"],
    'V': ["Vanuatu", "Venezuela", "Vietnam"],
    'Y': ["Yemen"],
    'Z': ["Zambia", "Zimbabwe"]
}


planetsdict = {
    'C': ["Ceres"],
    'E': ["Earth", "Eris"],
    'H': ["Haumea"],
    'J': ["Jupiter"],
    'M': ["Makemade", "Mars", "Mercury"],
    'N': ["Neptune"],
    'P': ["Pluto"],
    'S': ["Saturn"],
    'U': ["Uranus"],
    'V': ["Venus"]
}


fruitsdict = {
    'A': ["Acerola", "Apple", "Apricots", "Avocado"],
    'B': ["Banana", "Blackberries", "Blackcurrant", "Blueberries", "Breadfruit"],
    'C': ["Cantaloupe", "Carambola", "Cherimoya", "Cherries", "Clementine", "Coconut Meat", "Cranberries", "Custard-Apple"],
    'D': ["Date Fruit", "Durian"],
    'E': ["Elderberries"],
    'F': ["Feijoa", "Figs"],
    'G': ["Gooseberries", "Grapefruit", "Grapes", "Guava"],
    'H': ["Honeydew Melon"],
    'J': ["Java-Plum", "Jujube Fruit"],
    'K': ["Kiwifruit", "Kumquat"],
    'L': ["Lemon", "Longan", "Loquat", "Lychee"],
    'M': ["Mandarin", "Mango", "Mangosteen", "Mulberries"],
    'N': ["Nectarine"],
    'O': ["Olives", "Orange"], 
    'P': ["Papaya", "Passion fruit", "Peaches", "Pear", "Persimmon", "Pitaya", "Pineapple", "Pitanga", "Plantain", "Plums", "Pomegranate", "Prickly Pear", "Prunes", "Pummelo"],
    'Q': ["Quince"],
    'R': ["Raspberries", "Rhubarb", "Rose-Apple"],
    'S': ["Sapodilla", "Sapote", "Sousop", "Strawberries", "Sugar-Apple"],
    'T': ["Tamarind", "Tangerine"],
    'W': ["Watermelon"]
}

colorsdict = {
    'A': ["Amber", "Aqua", "Auburn", "Apricot"],
    'B': ["Beige", "Black", "Blue", "Bronze", "Bronze", "Burgundy"],
    'C': ["Charcoal", "Chocolate", "Cobalt", "Cyan", "Crimson", "Cream", "Copper"],
    'D': ["Dandelion", "Dark blue", "Denim"],
    'E': ["Ecru", "Emerald green"],
    'F': ["Forest green", "Fuchsia"],
    'G': ["Gold", "Green", "Grey"],
    'I': ["Indigo", "Ivory"],
    'J': ["Jade"],
    'K': ["Khaki", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan"],
    'L': ["Lavender", "Lemon", "Lilac", "Lime green"],
    'M': ["Magenta", "Maroon", "Mauve", "Mint green", "Moss green", "Mustard"],
    'N': ["Navy blue"],
    'O': ["Olive", "Orange"],
    'P': ["Peach", "Pink", "Powder blue", "Purple", "Prussian blue", "Purple"],
    'Q': ["Quartz"],
    'R': ["Red", "Rose", "Royal blue", "Ruby"],
    'S': ["Salmon pink", "Sandy brown", "Saapphire", "Scarlet", "Shocking pink", "Silver", "Sky blue"],
    'T': ["Tan", "Tangerine", "Turquoise"],
    'V': ["Violet"],
    'W': ["White"],
    'Y': ["Yellow"]
}
# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

pres = random.randint(0, 21)
randomletter5 = presalphabet[pres]
@app.route('/presidents', methods=['GET', 'POST'])
def presidents():
    if request.method == 'POST':
        return render_template("presidents.html", randomletter5=randomletter5)
@app.route('/presidentsresults', methods=['GET', 'POST'])
def presidentsresults():
    if request.method == 'GET':
        return "Error"
    else:
        C = request.form['presidents']
        if C[0] == randomletter5:
            president = presidentsdict[C[0]]
            for pres in president:
                if pres == C:
                    return "Correct"
        return "Not correct"


col = random.randint(0, 21)
randomletter4 = colalphabet[col]
@app.route('/colors', methods=['GET', 'POST'])
def colors():
    if request.method == 'POST':
        return render_template("colors.html", randomletter4=randomletter4)
@app.route('/colorsresults', methods=['GET', 'POST'])
def colorsresults():
    if request.method == 'GET':
        return "Error"
    else:
        B = request.form['colors']
        if B[0] == randomletter4:
            color = colorsdict[B[0]]
            for col in color:
                if col == B:
                    return "Correct"
        return "Not correct"

co = random.randint(0, 20)
randomletter3 = calphabet[co]
@app.route('/countries', methods=['GET', 'POST'])
def countries():
    if request.method == 'POST':
        return render_template("countries.html", randomletter3=randomletter3)
@app.route('/countriesresults', methods=['GET', 'POST'])
def countriesresults():
    if request.method == 'GET':
        return "Error"
    else:
        A = request.form['countries']
        if A[0] == randomletter3:
            country = countriesdict[A[0]]
            for c in country:
                if c == A:
                    return "Correct"
        return "Not correct"


fr = random.randint(0, 19)
randomletter2 = falphabet[fr]

@app.route('/fruits', methods=['GET', 'POST'])
def fruits():
    if request.method == 'POST':
        return render_template("fruits.html", randomletter2=randomletter2)
@app.route('/fruitsresults', methods=['GET', 'POST'])
def fruitsresults():
    if request.method == 'GET':
        return "Error"
    else:
        Z = request.form['fruits']
        if Z[0] == randomletter2:
            fruit = fruitsdict[Z[0]]
            for f in fruit:
                if f == Z:
                    return "Correct"
        return "Not correct"


pl = random.randint(0,9)
randomletter1 = palphabet[pl]
@app.route('/planets', methods=['GET', 'POST'])
def planets():
    if request.method == 'POST':
        return render_template("planets.html", randomletter1=randomletter1)
@app.route('/planetsresults', methods=['GET', 'POST'])
def planetsresults():
    if request.method == 'GET':
        return "Error"
    else:
        Y = request.form['planets']
        if Y[0] == randomletter1:
            planet = planetsdict[Y[0]]
            for p in planet:
                if p == Y:
                    return "Correct"
        return "Not correct"


st = random.randint(0, 18)
randomletter = stalphabet[st]
@app.route('/USStates', methods=['GET', 'POST'])
def US_States():
    if request.method == 'POST':
        return render_template("US_States.html", randomletter=randomletter)

@app.route('/USStatesresults', methods=['GET', 'POST'])
def USStatesresults():
    if request.method == 'GET':
        return "Error"
    else:
        X = request.form['states']
        if X[0] == randomletter:
            state = states[X[0]]
            for s in state:
                if s == X:
                    return "Correct"
        return "Not correct"

