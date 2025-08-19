# app/schemas/testcase.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TestCaseBase(BaseModel):
    name: str
    description: Optional[str] = None

class TestCaseCreate(TestCaseBase):
    pass

class TestCaseUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None

class TestCaseOut(TestCaseBase):
    id: int
    status: str
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
