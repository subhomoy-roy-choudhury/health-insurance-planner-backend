from pydantic import Enum
from .base import BaseDBModel
from typing import List
from bson.objectid import ObjectId

class MemberType(str, Enum):
    ADULT = 'adult'
    CHILD = 'child'

class Member(BaseDBModel):
    type: MemberType
    age: int
    plan: ObjectId

class Plan(BaseDBModel):
    user_id: str
    insurance_plan: ObjectId
    add_to_cart: bool = False
    payment: str = 'PENDING'