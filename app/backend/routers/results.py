# app/routers/results.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend import models, database
from pydantic import BaseModel

router = APIRouter(
    prefix="/results",
    tags=["results"]
)

# ✅ Define schema inline since you don't have schemas module
class TestResultIn(BaseModel):
    test_name: str
    nodeid: str
    status: str
    execution_time: str
    screenshot: str | None = None
    error_message: str | None = None


@router.post("/", response_model=dict)
def create_result(result: TestResultIn, db: Session = Depends(database.get_db)):
    db_result = models.TestResult(
        test_name=result.test_name,
        nodeid=result.nodeid,
        status=result.status,
        execution_time=result.execution_time,
        screenshot=result.screenshot,
        error_message=result.error_message
    )
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return {"message": "Result stored successfully", "id": db_result.id}


@router.get("/", response_model=list[dict])
def get_results(db: Session = Depends(database.get_db)):
    results = db.query(models.TestResult).all()
    return [
        {
            "id": r.id,
            "test_name": r.test_name,
            "nodeid": r.nodeid,
            "status": r.status,
            "execution_time": r.execution_time,
            "screenshot": r.screenshot,
            "error_message": r.error_message
        }
        for r in results
    ]
