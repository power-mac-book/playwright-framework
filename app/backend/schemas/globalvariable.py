from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class GlobalVariableBase(BaseModel):
    key: str = Field(..., min_length=1, max_length=255)
    value: str = Field(..., min_length=1)
    description: Optional[str] = None

class GlobalVariableCreate(GlobalVariableBase):
    pass

class GlobalVariableUpdate(BaseModel):
    key: Optional[str] = Field(None, min_length=1, max_length=255)
    value: Optional[str] = None
    description: Optional[str] = None

class GlobalVariableResponse(GlobalVariableBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True