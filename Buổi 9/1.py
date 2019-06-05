import pymongo
uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'
client = pymongo.MongoClient(uri)
db = client.c4e
collection = db.posts
collection.insert_one({
    "title":"Code, code nữa, code mãi",
    "author":"Nguyễn Đức",
    "content":"Những dòng code nhìn đau mắt thật, nhưng mà nó thú vị lắm =)))"})