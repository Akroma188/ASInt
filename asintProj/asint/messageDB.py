import pickle
import mess

class messageDB:
    def __init__(self):
        self.name = 'myMessages'

        try:
            f = open('bd_dump'+ self.name, 'rb')
            self.message_database = pickle.load(f)
            f.close()
        except IOError:
            self.message_database = {}

    def addMessage(self, building, user, message):
                message_id = len(self.message_database)
                self.message_database[message_id] = mess.mess(building, user, message, message_id)
                f = open('bd_dump'+self.name, 'wb')
                pickle.dump(self.message_database, f)
                f.close()

    def returnAllMessages(self):
        return list(self.message_database.values())

    def clearAllMessages(self):
        open('bd_dump'+ self.name, "w").close()
        

