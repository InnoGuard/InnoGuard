import pymongo

Client = pymongo.MongoClient("mongodb://localhost:27017/")
db = Client["Database"]

browser_responses = db["browser_responses"]
text_responses = db["text_responses"]
racy_image_responses = db["racy_image_responses"]

