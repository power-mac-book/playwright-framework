from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models.testcase import TestCase
from backend.schemas.testcases import TestCaseOut, TestCaseCreate

router = APIRouter(prefix="/testcases", tags=["Test Cases"])

@router.post("/", response_model=TestCaseOut)
def create_testcase(testcase: TestCaseCreate, db: Session = Depends(get_db)):
    # Create new TestCase
    tc = TestCase(
        name=testcase.name,
        description=testcase.description,
        status="pending"  # default status
    )
    db.add(tc)
    db.commit()
    db.refresh(tc)
    return tc

@router.get("/")
def list_testcases(db: Session = Depends(get_db)):
    return db.query(TestCase).all()

@router.get("/{testcase_id}")
def get_testcase(testcase_id: int, db: Session = Depends(get_db)):
    tc = db.query(TestCase).filter(TestCase.id == testcase_id).first()
    if not tc:
        raise HTTPException(404, "Test case not found")
    return tc

@router.put("/{testcase_id}")
def update_testcase(testcase_id: int, name: str = None, description: str = None, tags: str = None, status: str = None, db: Session = Depends(get_db)):
    tc = db.query(TestCase).filter(TestCase.id == testcase_id).first()
    if not tc:
        raise HTTPException(404, "Test case not found")
    if name: tc.name = name
    if description: tc.description = description
    if tags: tc.tags = tags
    if status: tc.status = status
    db.commit()
    db.refresh(tc)
    return tc

@router.delete("/{testcase_id}")
def delete_testcase(testcase_id: int, db: Session = Depends(get_db)):
    tc = db.query(TestCase).filter(TestCase.id == testcase_id).first()
    if not tc:
        raise HTTPException(404, "Test case not found")
    db.delete(tc)
    db.commit()
    return {"message": "Test case deleted"}
