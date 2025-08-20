from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.database import Base, engine 
from backend.routers import results, ai, objectrepository, globalvariable
from backend.api import testcases, testruns

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Playwright AI Test Framework")

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

# Routers
app.include_router(testruns.router)
app.include_router(results.router)
app.include_router(ai.router)
app.include_router(testcases.router)
app.include_router(objectrepository.router)
app.include_router(globalvariable.router)


@app.get("/")
def root():
    return {"message": "Test Framework Backend Running 🚀"}


