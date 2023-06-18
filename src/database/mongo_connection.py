from pymongo import MongoClient

credentials = {
    "name": "citiSolution",
    "password": "eBJ6YnFxBCGxnOb8"
}


class MongoDbConnection:
    def __init__(self):
        self.client = MongoClient("mongodb+srv://citiSolution:eBJ6YnFxBCGxnOb8@cluster0.nxwf6o8.mongodb.net/")

        self.db = self.client["CitiSolutions"]
        self.collection = self.db["shipment"]

    def insert_shipment(self, payload):
        self.collection.insert_one(payload)

    def put_shipment_by_id(self, payload, _id):
        self.collection.update_one({'_id': _id}, payload)
