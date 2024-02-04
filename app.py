from pymongo import MongoClient

import json

#with open('resume.json', 'r') as archivo:
#    cvData = json.load(archivo)

MONGO_URI = 'mongodb://localhost'

client = MongoClient(MONGO_URI)

db = client['cv']

collection = db['data']


#for ob in cvData:
#    collection.insert_one(ob)