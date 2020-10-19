from bson.json_util import dumps
from bson.objectid import ObjectId
from datetime import datetime
from os import environ
from pymongo import MongoClient
from urllib import parse

DB_HOST = environ.get("DB_HOST") or "mongo"
DB_PORT = environ.get("DB_PORT") or 27017
DB_NAME = environ.get("DB_NAME") or "kubeless"
COLLECTION_NAME = environ.get("COLLECTION_NAME") or "events"

def get_mongo_collection(db_name, collection_name):
  client = MongoClient(DB_HOST, DB_PORT)
  db = client[str(db_name)]
  collection = db[str(collection_name)]
  return collection

def put_event(event, context):
  data = event["data"]
  collection = get_mongo_collection(DB_NAME, COLLECTION_NAME)
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
      collection = get_mongo_collection(DB_NAME, COLLECTION_NAME)
      get_doc = collection.find_one({"_id": {"$eq": object_id}})
      doc_by_id = get_doc
  except Exception as e:
    print(dumps({"severity": "warn", "message": repr(e), "timestamp": datetime.timestamp(datetime.utcnow())}))
    doc_by_id = {"status": "error", "message": "doc not found."}
  return dumps(doc_by_id)
