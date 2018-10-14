import Pyro4
from dbUI import *



#requesting access to database object
data = Pyro4.Proxy('PYRO:obj_9e91c0b6ad534999b070a83e6863f09b@localhost:64415')

#init of the interface with the accessed database
UI = dbUI(data.database)
while not UI.user_input() :
        pass
UI.db.file.close()



# def main():
    

#     while not UI.interface.user_input() :
#         pass
#     UI.interface.db.file.close()

# if __name__ == "__main__":
#     main()
