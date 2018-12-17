from os import environ
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import requests
import botDB

app = Flask(__name__)


@app.route('/add_bot', methods=['POST'])
def chat():
    if(request.is_json):
        bots = botDB.botDB()
        building = request.json["building"]
        bots.addBot(str(building))
        return 'Bot added success'



