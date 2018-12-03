from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import requests


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("authentication.html")
    #return '<h1> Hello Heroku World </h1>'


@app.route('/API/asint/user/initialPage', methods=['POST', 'GET'])
def add_Book():
    if request.method == "GET":
        code=str(request.args['code'])
        payload = {'client_id':'570015174623322', 'client_secret':'DQOfZ+r5iWJjQluFun6JVzH83xyVnRCGj8AJS48zBDbH/T77KvCdq4jEYUE5gWp/qck495O3hQyAR256puWmBw==',
                    'redirect_uri':'https://asint.herokuapp.com/API/asint/user/initialPage', 'code':code, 'grant_type':'authorization_code'}
        r = requests.post('https://fenix.tecnico.ulisboa.pt/oauth/access_token', params=payload)
        #content = r.text
        content = r.json()
        return render_template("initialPage.html", content=content)
