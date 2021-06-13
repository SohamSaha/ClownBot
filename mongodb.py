import os
import pymongo
from pymongo.common import SERVER_SELECTION_TIMEOUT

conn_str = os.environ['CONNECTION_STRING']

client = pymongo.MongoClient(conn_str, SERVER_SELECTION_TIMEOUT-5000)

def get_value(collection, query_key, query_value, db_key):
    col = client[os.environ['DATABASE']][collection]
    query = { query_key : query_value }
    doc = col.find(query, {'_id': 0, db_key: 1})

    for value in doc:
        return (value)

def get_size(collection):
    db = client[os.environ['DATABASE']]
    col = db[collection]
    return (col.count_documents({}))