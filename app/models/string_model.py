from pydantic import BaseModel, Field

class StringUpdate(BaseModel):
    new_string: str = Field(..., min_length=1, max_length=100) 