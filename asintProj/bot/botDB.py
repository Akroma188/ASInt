import pickle
import bot

class botDB:
    def __init__(self):
        self.name = 'myBots'

        try:
            f = open('bd_dump'+ self.name, 'rb')
            self.bot_database = pickle.load(f)
            f.close()
        except IOError:
            self.bot_database = {}

    def addBot(self, building):
                bot_id = len(self.bot_database)
                self.bot_database[bot_id] = bot.bot(building, bot_id)
                f = open('bd_dump'+self.name, 'wb')
                pickle.dump(self.bot_database, f)
                f.close()

    def returnAllBots(self):
        return list(self.bot_database.values())

