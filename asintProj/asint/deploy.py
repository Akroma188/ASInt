from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import requests
import messageDB


app = Flask(__name__)
test = True
m_DB = messageDB.messageDB()

@app.route('/')
def index():
    return render_template("authentication.html")
        #return '<h1> Hello Heroku World </h1>'

# @app.route('/msg', methods=['POST'])
# def chat():
#     if(request.is_json):
#         nl = request.json["str"]
#         return jsonify(str(nl))

@app.route('/msg', methods=['POST'])
def chat():
    if(request.is_json):
        building = request.json["building"]
        message = request.json["message"]
        user = request.json["user"]
        return jsonify({'user':str(user), 'building':str(building), 'msg':str(message)})


# Bot will send request here
@app.route('/bot', methods=['POST'])
def chatBot():
    if(request.is_json):
        building = request.json["building"]
        message = request.json["message"]
        user = request.json["user"]
        m_DB.addMessage(str(building), str(user), str(message))
        return'success'

# jquery on html will send request here to get the messages in the db
@app.route('/reqinterval', methods=['POST'])
def reqBot():
    if(request.is_json):
        if len(m_DB.message_database) > 0:
            messages = m_DB.returnAllMessages()
            building = messages[0].building
            messa = messages[0].message
            user = messages[0].user
            m_DB.message_database.pop(0)
            return jsonify({'user':str(user), 'building':str(building), 'msg':str(messa)})
        else:
            return 'no messagge in DB'
    else:
        return 'no request'





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
