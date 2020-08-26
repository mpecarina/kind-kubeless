from datetime import datetime
from pymongo import MongoClient
from urllib import parse
from bson.json_util import dumps
from bson.objectid import ObjectId

client = MongoClient("mongo", 27017)
db = client.kubeless
collection = client.kubeless.events

def put_event(event, context):
  data = event["data"]
  query = collection.insert_one(data)
  resp = str(f"data inserted successfully with id: {query.inserted_id}")
  return resp

def get_event(event, context):
  query_str = event["extensions"]["request"].query_string

  try:
    doc_id = dict(parse.parse_qsl(query_str))["id"]
  except KeyError as e:
    print(dumps({"severity": "error", "message": repr(e), "timestamp": datetime.timestamp(datetime.utcnow())}))
    return dumps({"status": "error", "message": "url parameter value required for id"})

  try: 
      object_id = ObjectId(doc_id) or None
      get_doc = collection.find_one({"_id": {"$eq": object_id}})
      doc_by_id = get_doc
  except Exception as e:
    print(dumps({"severity": "warn", "message": repr(e), "timestamp": datetime.timestamp(datetime.utcnow())}))
    doc_by_id = {"status": "error", "message": "doc not found."}
  return dumps(doc_by_id)
