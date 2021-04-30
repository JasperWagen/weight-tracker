import pymongo

mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")

weight_tracker = mongo_client["weight_tracker"]

weights = weight_tracker["weights"]


def insert(date_and_weight):
    x = weights.insert_one(date_and_weight)


def get_all():
    return [x for x in weights.find({}).sort("date-stamp")]
