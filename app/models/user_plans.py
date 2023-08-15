from enum import Enum
from .base import BaseDBModel
from typing import List, Optional

class MemberType(str, Enum):
    ADULT = 'adult'
    CHILD = 'child'

class Member(BaseDBModel):
    type: List[MemberType]
    age: int
    user_plan: str

class UserPlan(BaseDBModel):
    user_id: str
    insurance_plan: str
    add_to_cart: bool = False
    payment: Optional[str] = 'PENDING'