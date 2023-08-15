from app.database import get_db
from typing import List
from bson.objectid import ObjectId

from ..models.user_plans import UserPlan, Member

# Access the MongoDB collection
db = get_db()
user_plan_collection = db.user_plan
members_collection = db.members


def create_user_plan(data):
    user_plan = user_plan_collection.insert_one(UserPlan(**data).model_dump())
    members = list(
        map(lambda x: {**x, "user_plan": user_plan.inserted_id}, data["members"])
    )
    created_members = create_members(members)
    return user_plan, create_members


def create_members(members: List[Member]):
    return members_collection.insert_many(members)


def find_user_plans(filters: str):
    return user_plan_collection.find(filters)


def add_to_cart(plan_id: str):
    return user_plan_collection.update_one(
        {"_id": ObjectId(plan_id)}, {"$set": {"add_to_cart": True}}
    )

def verify_payment(plan_id: str):
    return user_plan_collection.update_one(
        {"_id": ObjectId(plan_id)}, {"$set": {"payment": "SUCCESS"}}
    )