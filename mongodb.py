import os
import pymongo
from pymongo.common import SERVER_SELECTION_TIMEOUT

conn_str = os.environ['CONNECTION_STRING']

client = pymongo.MongoClient(conn_str, SERVER_SELECTION_TIMEOUT-5000)

def get_link(database, query_key, query_value):
    db = client[os.environ['DATABASE']]
    col = db[database]
    query = { query_key : query_value }
    doc = col.find(query, {'_id': 0, 'link': 1})

    for picture in doc:
        return (picture)