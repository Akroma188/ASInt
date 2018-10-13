import os
import pickle


if os.path.isfile('backup.p') is True:
        with open('backup.p', 'rb') as f:
            database = pickle.load(f)
            f.close()
        print('Files were backed up. \n')
        print(database)


# print(os.path.isfile('C:/Users/Dinis.PC-DINIS/Desktop/Cadeiras/ASInt/Lab3/backup.p'))


# list2=[]
# list1=[1]

# for x in list2[:-1]:
#     print(x)