# import flask
#
# app = flask.Flask(__name__)
# app.config['DEBUG'] =True
# @app.route('/',methods=['GET'])
# def home():
#     return "<h1>This is the title</h1><p> This is where the content starts</p>"
# app.run()
# ##########################################
# import flask
# from flask import request, jsonify
# app = flask.Flask(__name__)
# app.config["DEBUG"] =True
# books = [
#     {'id': 0,
#      'title': 'A Fire Upon the Deep',
#      'author': 'Vernor Vinge',
#      'first_sentence': 'The coldsleep itself was dreamless.',
#      'year_published': '1992'},
#     {'id': 1,
#      'title': 'The Ones Who Walk Away From Omelas',
#      'author': 'Ursula K. Le Guin',
#      'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
#      'published': '1973'},
#     {'id': 2,
#      'title': 'Dhalgren',
#      'author': 'Samuel R. Delany',
#      'first_sentence': 'to wound the autumnal city.',
#      'published': '1975'}
# ]
#
# @app.route('/home',methods=['GET'])
# def home():
#     return "<h1>This is the title</h1><p> This is where the content starts</p>"
# @app.route('/api/v1/resources/books/all',methods=['GET'])
# def api_all():
#     return jsonify(books)
#
# @app.route('/api/v1/resources/books',methods=['GET'])
# def app_id():
#     if 'id' in request.args:
#         id =int(request.args['id'])
#     else:
#         print 'please provide the argid'
#     results = []
#     for book in books:
#         if book['id'] == id:
#             results.append(book)
#     return jsonify(results)
#
#
# app.run()
from flask import Flask, request,redirect, url_for
app = Flask(__name__)


@app.route('/home')
def homepage():
    return "This is a homepage"

@app.route('/sucess/<name>')
def sucess(name):
    return "Welcome %s" %name

@app.route('/login',methods=['POST','GET'])
def loginpage():
    if request.method=='POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user=request.args.get('nm')
        return redirect(url_for('sucess',name=user))


if __name__ == '__main__':
    app.run(debug=True)