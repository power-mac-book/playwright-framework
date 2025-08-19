# app/routers/testcases.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from backend.database import get_db
from backend.models.testcase import TestCase
from app.schemas.testcase import TestCaseCreate, TestCaseUpdate, TestCaseOut

router = APIRouter(prefix="/testcases", tags=["TestCases"])

@router.post("/", response_model=TestCaseOut)
def create_testcase(test: TestCaseCreate, db: Session = Depends(get_db)):
    db_test = TestCase(name=test.name, description=test.description)
    db.add(db_test)
    db.commit()
    db.refresh(db_test)
    return db_test

@router.get("/", response_model=List[TestCaseOut])
def list_testcases(db: Session = Depends(get_db)):
    return db.query(TestCase).all()

@router.get("/{test_id}", response_model=TestCaseOut)
def get_testcase(test_id: int, db: Session = Depends(get_db)):
    test = db.query(TestCase).filter(TestCase.id == test_id).first()
    if not test:
        raise HTTPException(status_code=404, detail="TestCase not found")
    return test

@router.put("/{test_id}", response_model=TestCaseOut)
def update_testcase(test_id: int, update: TestCaseUpdate, db: Session = Depends(get_db)):
    test = db.query(TestCase).filter(TestCase.id == test_id).first()
    if not test:
        raise HTTPException(status_code=404, detail="TestCase not found")
    for field, value in update.dict(exclude_unset=True).items():
        setattr(test, field, value)
    db.commit()
    db.refresh(test)
    return test

@router.delete("/{test_id}")
def delete_testcase(test_id: int, db: Session = Depends(get_db)):
    test = db.query(TestCase).filter(TestCase.id == test_id).first()
    if not test:
        raise HTTPException(status_code=404, detail="TestCase not found")
    db.delete(test)
    db.commit()
    return {"detail": "TestCase deleted"}
