from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from backend.database import get_db
from backend.models.testrun import TestRun
from backend.models.testcase import TestCase
import datetime

router = APIRouter(prefix="/testruns", tags=["Test Runs"])

@router.post("/")
def start_test_run(testcase_id: int, db: Session = Depends(get_db)):
    tc = db.query(TestCase).filter(TestCase.id == testcase_id).first()
    if not tc:
        raise HTTPException(404, "Test case not found")

    run = TestRun(testcase_id=testcase_id, status="running")
    db.add(run)
    db.commit()
    db.refresh(run)
    return run

@router.put("/{run_id}/finish")
def finish_test_run(run_id: int, status: str, logs: str = None, db: Session = Depends(get_db)):
    run = db.query(TestRun).filter(TestRun.id == run_id).first()
    if not run:
        raise HTTPException(404, "Run not found")

    run.status = status
    run.finished_at = datetime.datetime.utcnow()
    run.logs = logs
    db.commit()
    db.refresh(run)
    return run

@router.get("/")
def list_runs(db: Session = Depends(get_db)):
    return db.query(TestRun).all()
