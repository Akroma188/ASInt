import Pyro4
import dbUI
from bookDB import *


db = bookDB()


daemon = Pyro4.Daemon()

#registering database object and passing it through
uri = daemon.register(db)
print(uri)

daemon.requestLoop()