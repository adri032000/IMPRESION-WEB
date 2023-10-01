import os
import json
import pymongo
from flask import Flask
from flask import request
app = Flask(__name__)


client = pymongo.MongoClient("mongodb+srv://alejadri48:NDsDezjMsaU7uzWe@cluster0.kcsmyip.mongodb.net/?retryWrites=true&w=majority")
db = client['db_ADRIANA']
collection = db['Adriana_Raquetas']


@app.route('/')
def get():
    nombre = collection.find()
    response = []
    for document in nombre:
        document['_id'] = str(document['_id'])
        response.append(document)
    return json.dumps(response)
if __name__ == '__main__':
    app.run()