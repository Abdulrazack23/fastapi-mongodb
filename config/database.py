from pymongo import MongoClient

client =MongoClient("mongodb+srv://admin:Zack1234..@cluster0.cszc2uw.mongodb.net/?retryWrites=true&w=majority")

db= client.test_db
collection_name=db["test_db"]

