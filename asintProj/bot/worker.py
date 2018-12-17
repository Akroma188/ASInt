import time
import sys
import requests
import botDB
from datetime import datetime


#INTERVAL = 60 * 60 * 6  # tweet every 6 hours
INTERVAL = 5  # every 5 seconds, for testing
bots = botDB.botDB()
while True:
    # db = bots.returnAllBots()
    # for bot in db:
    #payload = {'user':str(bot.id), 'building':str(bot.building), 'message':str(datetime.now())}
    payload = {'user':'bot 1', 'building':'central', 'message':str(datetime.now())}
    r = requests.post('https://asint.herokuapp.com/bot', json=payload)
    print(r)
    
    time.sleep(INTERVAL)
