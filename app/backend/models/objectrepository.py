from sqlalchemy import Column, Integer, String, Text, DateTime, func
from backend.database import Base

class ObjectRepository(Base):
    __tablename__ = "object_repository"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)   # e.g. "Login Button"
    description = Column(Text, nullable=True)                 # optional description
    locator_type = Column(String(50), nullable=False)         # e.g. "xpath", "css", "id"
    locator_value = Column(Text, nullable=False)              # actual locator string
    application = Column(String(255), nullable=True)          # app/page it belongs to
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
