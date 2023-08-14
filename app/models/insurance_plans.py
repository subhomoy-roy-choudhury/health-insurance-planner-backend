from pydantic import BaseModel

class AgeRange(BaseModel):
    min: int
    max: int

class InsurancePlan(BaseModel):
    adult: int
    children: int
    age_range: AgeRange
    tier: int
    premium: float
    amount: float
    
