from pydantic import BaseModel
from .base import BaseDBModel

class AgeRange(BaseModel):
    min: int
    max: int

class InsurancePlan(BaseDBModel):
    adult: int
    children: int
    age_range: AgeRange
    tier: int
    premium: float
    amount: float
