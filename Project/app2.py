import pymongo

uri = "mongodb://mrd198:12051998d@ds335957.mlab.com:35957/c4e32thuvien"
client = pymongo.MongoClient(uri)
# db = client.c4e32thuvien
collection = client.sach

def get_all():
    return list(collection.find())

def insert_data_book(name,price):
    collection.insert_data_book({'name':name,'price':price})