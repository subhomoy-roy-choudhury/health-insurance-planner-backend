from ..app import mongo

# Access the MongoDB collection
insurance_plan_collection = mongo.db.insurance_plan

def create_insurance_plan(data):
    return insurance_plan_collection.insert_one(data.model_dump())

def find_insurance_plan(filter):
    return insurance_plan_collection.find_one(filter)