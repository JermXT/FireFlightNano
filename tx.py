from pymongo import MongoClient

class MongoDB:
    def __init__(self,ip, port=27017):
        self.client = MongoClient(ip, port)
    def accessDB(self, database='fireflight'):
        self.db = self.client[database]


a = MongoDB('localhost')
a.accessDB()

gps = a.db.gpsdatas
print(gps.find_one())

