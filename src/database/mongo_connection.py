from pymongo import MongoClient

credentials = {
    "name": "citiSolution",
    "password": "eBJ6YnFxBCGxnOb8"
}


class MongoDbConnection:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.client = MongoClient("mongodb+srv://citiSolution:eBJ6YnFxBCGxnOb8@cluster0.nxwf6o8.mongodb.net/")

        self.db = self.client["CitiSolutions"]
        self.collection = self.db["shipment"]

    def insert_shipment(self, payload):
        self.collection.insert_one(payload)

    def put_shipment_by_id(self, payload, _id):
        self.collection.update_one({'_id': _id}, payload)

    def get_historic_shipments(self):
        return self.collection.find()

    def find_by_params(self, params):
        data = self.collection.find_one(params)
        if data:
            self.remove_id_field(dict(data))
            return data

    @staticmethod
    def remove_id_field(data):
        del data['_id']
