from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from backend.database import get_db
from backend.models.objectrepository import ObjectRepository
from backend.schemas.objectrepository import (
    ObjectRepositoryCreate,
    ObjectRepositoryResponse,
    ObjectRepositoryUpdate
)

router = APIRouter(
    prefix="/object-repository",
    tags=["Object Repository"]
)

@router.get("/", response_model=List[ObjectRepositoryResponse])
async def get_all_objects(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Get all objects from the repository with pagination"""
    objects = db.query(ObjectRepository).offset(skip).limit(limit).all()
    return objects

@router.get("/{object_id}", response_model=ObjectRepositoryResponse)
async def get_object(object_id: int, db: Session = Depends(get_db)):
    """Get a specific object by ID"""
    object = db.query(ObjectRepository).filter(ObjectRepository.id == object_id).first()
    if not object:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Object with ID {object_id} not found"
        )
    return object

@router.post("/", response_model=ObjectRepositoryResponse, status_code=status.HTTP_201_CREATED)
async def create_object(
    object: ObjectRepositoryCreate,
    db: Session = Depends(get_db)
):
    """Create a new object in the repository"""
    # Check if object with same name already exists
    existing_object = db.query(ObjectRepository).filter(
        ObjectRepository.name == object.name
    ).first()
    if existing_object:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Object with name '{object.name}' already exists"
        )

    db_object = ObjectRepository(**object.dict())
    db.add(db_object)
    db.commit()
    db.refresh(db_object)
    return db_object

@router.put("/{object_id}", response_model=ObjectRepositoryResponse)
async def update_object(
    object_id: int,
    object_update: ObjectRepositoryUpdate,
    db: Session = Depends(get_db)
):
    """Update an existing object"""
    db_object = db.query(ObjectRepository).filter(ObjectRepository.id == object_id).first()
    if not db_object:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Object with ID {object_id} not found"
        )

    # Check name uniqueness if name is being updated
    if object_update.name and object_update.name != db_object.name:
        existing_object = db.query(ObjectRepository).filter(
            ObjectRepository.name == object_update.name
        ).first()
        if existing_object:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Object with name '{object_update.name}' already exists"
            )

    for key, value in object_update.dict(exclude_unset=True).items():
        setattr(db_object, key, value)

    db.commit()
    db.refresh(db_object)
    return db_object

@router.delete("/{object_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_object(object_id: int, db: Session = Depends(get_db)):
    """Delete an object from the repository"""
    db_object = db.query(ObjectRepository).filter(ObjectRepository.id == object_id).first()
    if not db_object:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Object with ID {object_id} not found"
        )

    db.delete(db_object)
    db.commit()
    return None