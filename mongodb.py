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

def get_collection_length(collection):
    col = client[os.environ['DATABASE']][collection]
    return (col.count_documents({}))

def get_filtered_collection_length(collection, query_key, query_value):
    col = client[os.environ['DATABASE']][collection]
    return (col.count_documents({ query_key : query_value }))

def insert_record(collection, target, reason):
    col = client[os.environ['DATABASE']][collection]
    record_to_insert = { 'user': target, 'reason' : reason }
    total_callout = get_filtered_collection_length(collection , 'user', target)
    if (total_callout == 5):
        doc = col.find().sort('_id', 1).limit(1)
        for record in doc:
            col.delete_one({ '_id' : record['_id']})
        col.insert_one(record_to_insert)
    else:
        col.insert_one(record_to_insert)

def get_all_records_value(collection, query_key, query_value, db_key):
    col = client[os.environ['DATABASE']][collection]
    query = { query_key : query_value }
    doc = col.find(query, {'_id': 0, db_key: 1}).sort('_id', 1)
    return_string = ''
    for value in doc:
        return_string += value['reason'] + '\n'
    return(return_string)