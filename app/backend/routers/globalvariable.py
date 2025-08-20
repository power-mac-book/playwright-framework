from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models.globalvariable import GlobalVariable
from backend.schemas.globalvariable import GlobalVariableCreate, GlobalVariableUpdate, GlobalVariableResponse
from typing import List

router = APIRouter(prefix="/global-variables", tags=["Global Variables"])

@router.post("/", response_model=GlobalVariableResponse)
def create_variable(variable: GlobalVariableCreate, db: Session = Depends(get_db)):
    # Check if variable with same key exists
    if db.query(GlobalVariable).filter(GlobalVariable.key == variable.key).first():
        raise HTTPException(
            status_code=400,
            detail=f"Variable with key '{variable.key}' already exists"
        )
    
    db_var = GlobalVariable(**variable.dict())
    db.add(db_var)
    db.commit()
    db.refresh(db_var)
    return db_var

@router.get("/", response_model=List[GlobalVariableResponse])
def list_variables(db: Session = Depends(get_db)):
    return db.query(GlobalVariable).all()

@router.get("/{var_id}", response_model=GlobalVariableResponse)
def get_variable(var_id: int, db: Session = Depends(get_db)):
    var = db.query(GlobalVariable).filter(GlobalVariable.id == var_id).first()
    if not var:
        raise HTTPException(status_code=404, detail="Variable not found")
    return var

@router.put("/{var_id}", response_model=GlobalVariableResponse)
def update_variable(var_id: int, variable: GlobalVariableUpdate, db: Session = Depends(get_db)):
    db_var = db.query(GlobalVariable).filter(GlobalVariable.id == var_id).first()
    if not db_var:
        raise HTTPException(status_code=404, detail="Variable not found")
    for key, value in variable.dict().items():
        setattr(db_var, key, value)
    db.commit()
    db.refresh(db_var)
    return db_var

@router.delete("/{var_id}")
def delete_variable(var_id: int, db: Session = Depends(get_db)):
    db_var = db.query(GlobalVariable).filter(GlobalVariable.id == var_id).first()
    if not db_var:
        raise HTTPException(status_code=404, detail="Variable not found")
    db.delete(db_var)
    db.commit()
    return {"detail": "Variable deleted successfully"}
