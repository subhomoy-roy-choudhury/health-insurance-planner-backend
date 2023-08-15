import pymongo
from pymongo import MongoClient

def get_db():
    client = MongoClient(host='localhost',
                         port=27020, 
                         username='root', 
                         password='rootpassword',
                        authSource="admin")
    db = client["health_insurance_planner"]
    return db