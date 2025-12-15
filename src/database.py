FLASK_PORT_NUMBER=5002
import pymongo

mongo_url="mongodb://localhost:27017"
mongo_client= pymongo.MongoClient(mongo_url)

database='prediction'
db=mongo_client[database]
import pickle
import pandas as pd
import json

class Obj:

    @staticmethod
    def load_json_data():
        return pd.read_csv("heart.csv")

    @staticmethod
    def load_model():
        with open("model.pkl", "rb") as f:
            model = pickle.load(f)
        return model