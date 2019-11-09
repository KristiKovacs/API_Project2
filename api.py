import flask
from flask import request, jsonify


app = flask.Flask(__name__)
app.config["DEBUG"] = True

#Creating some test data for my catalog

novels = [
    {'id': 0,
     'title': 'Hound of the Baskervilles',
     'author': 'Arthur Conan Doyle',
     'yr_published': '1901'},
    {'id': 1,
     'title': 'The Hangman\'s Daughter',
     'author': 'Oliver Potzsch',
     'yr_published': '2008'},
    {'id': 2,
     'title': 'And Then There Were None',
     'author': 'Agatha Christie',
     'yr_published': '1939'},
    {'id': 3,
     'title': 'Whose Body?',
     'author': 'Dorothy L. Sayers',
     'yr_published': '1923'},
    {'id': 4,
     'title': 'The Red House Mystery',
     'author': 'A. A. Milne',
     'yr_published': '1922'},
    {'id': 5,
     'title': 'The Cuckoo\'s Calling',
     'author': 'Stieg Larsson',
     'yr_published': '2005'},
    {'id': 6,
     'title': 'In the Woods',
     'author': 'Tana French',
     'yr_published': '2007'},
     {'id': 7,
      'title': 'The Lovely Bones',
      'author': 'Alice Sebold',
      'yr_published': '2002'},
     {'id': 8,
      'title': 'One of Us is Lying',
      'author': 'Karen M. McManus',
      'yr_published': '2017'},
     {'id': 9,
      'title': 'The Woman in Cabin 10',
      'author': 'Ruth Ware',
      'yr_published': '2016'},
     {'id': 10,
      'title': 'One for the Money',
      'author': 'Janet Evanovich',
      'yr_published': '1994'},
]


#My URL Path / mapped to my function 'home'
@app.route('/', methods=['GET'])
def home():
    return "<h1>Analyzing Archives</h1><p>This site is a test API for Murder Mystery novels, both classic and new.</p>"

@app.route('/api/novels/all', methods=['GET'])
def api_all():
    return jsonify(novels)

@app.route('/api/novels', methods=['GET'])
def api_id():
    #This checks an ID in the URL, if yes then assign to a variable, if not show error
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error! No ID provided, please give an ID number between 0 - 10."
    #Created an empty list for my results
    results = []

    #This loops through and matches results for the ID #
    for book in novels:
        if book['id'] == id:
            results.append(book)

    return jsonify(results)

app.run()
