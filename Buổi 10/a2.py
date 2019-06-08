import pymongo

uri = 'mongodb://c4e:12345678Abc@ds231307.mlab.com:31307/c4e'
client = pymongo.MongoClient(uri)
db = client.c4e
collection = db.ntduc

def get_all():
    return list(collection.find())

def insert(model,daily,image,year):
    db.ntduc.insert_one({'Model':model,'Daily':daily,'Image':image,'Year':year})