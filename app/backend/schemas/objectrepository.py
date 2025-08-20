from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ObjectRepositoryBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    locator_type: str = Field(..., min_length=1, max_length=50)
    locator_value: str = Field(..., min_length=1)
    application: Optional[str] = Field(None, max_length=255)

class ObjectRepositoryCreate(ObjectRepositoryBase):
    pass

class ObjectRepositoryUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    locator_type: Optional[str] = Field(None, min_length=1, max_length=50)
    locator_value: Optional[str] = Field(None, min_length=1)
    application: Optional[str] = Field(None, max_length=255)

class ObjectRepositoryResponse(ObjectRepositoryBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True