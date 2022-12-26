import environ
import pymongo
from pymongo import MongoClient

env = environ.Env()
environ.Env.read_env()

connection_string = env('URL_STRING_CONNECTION_DB')

client = pymongo.MongoClient(connection_string)
db = client['Ratatouille']

collection_name = db["Product"]

med_details = collection_name.find({})
# Print on the terminal
for r in med_details:
    print(r['name'])

print('hola')