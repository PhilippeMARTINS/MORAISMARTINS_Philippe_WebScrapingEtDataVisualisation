from imghdr import tests
from flask import Flask
#import json, time
import pymongo 
from pymongo import MongoClient
import pandas as pd
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

con = MongoClient("localhost",27017)
test = list(con["Sneakers"]["Reebok"].find({},{"_id":0}))

class Showdb(Resource):
    def get(self):
        return test


api.add_resource(Showdb, '/')

if __name__ == '__main__':
    app.run(port=80, debug=True)