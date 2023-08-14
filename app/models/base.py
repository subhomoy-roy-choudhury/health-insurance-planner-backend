from datetime import datetime
from pydantic import BaseModel

class BaseDBModel(BaseModel):
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
