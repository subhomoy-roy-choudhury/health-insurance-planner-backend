import pymongo
from pymongo import MongoClient


def get_db():
    client = MongoClient(
        host="mongodb",
        # port=27020,
        username="root",
        password="rootpassword",
        authSource="admin",
    )
    # mongodb://localhost:27017/?retryWrites=true&serverSelectionTimeoutMS=5000&connectTimeoutMS=10000
    db = client["health_insurance_planner"]
    return db
