import json
from pymongo import MongoClient

data_path_1 = "data/F01705150050.json"
data_path_2 = "data/F01705150090.json"

client = MongoClient("127.0.0.1", 27017)
db = client.kubeless
collection = client.kubeless.events

with open(data_path_1) as json_file: 
    data_1 = json.load(json_file) 

with open(data_path_2) as json_file: 
    data_2 = json.load(json_file) 

post_id_1 = collection.insert_one(data_1)
post_id_2 = collection.insert_one(data_2)

print(post_id_1.inserted_id)
print(post_id_2.inserted_id)
