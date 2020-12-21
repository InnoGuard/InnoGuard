import pymongo
import libs.Constants
Client = pymongo.MongoClient(libs.Constants.MONGODB)
db = Client["Database"]

users = db["users"]
browser_responses = db["browser_responses"]
text_responses = db["text_responses"]
racy_image_responses = db["racy_image_responses"]
