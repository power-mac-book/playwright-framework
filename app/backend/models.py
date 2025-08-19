# app/models/test_result.py
from sqlalchemy import Column, Integer, String, Text
from backend.database import Base

class TestResult(Base):
    __tablename__ = "test_results"

    id = Column(Integer, primary_key=True, index=True)
    test_name = Column(String(255), nullable=False)       # Name of the test
    nodeid = Column(String(255), nullable=False)          # Pytest node identifier
    status = Column(String(50), nullable=False)           # passed / failed / skipped
    execution_time = Column(String(50), nullable=False)   # Store as string (or Float if numeric seconds)
    screenshot = Column(Text, nullable=True)              # Base64 image or file path
    error_message = Column(Text, nullable=True)           # Error trace if failed

    
class TestCase(Base):
    __tablename__ = "test_cases"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String(50), default="draft")  # draft, active, archived
    tags = Column(String(255), nullable=True)     # comma separated tags