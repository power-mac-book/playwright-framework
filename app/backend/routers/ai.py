from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/ai", tags=["ai"])

class Prompt(BaseModel):
    prompt: str

@router.post("/generate-test")
def generate_test(req: Prompt):
    # Stub: return a basic Playwright test. Later, wire an LLM.
    code = f"""from playwright.sync_api import Page

def test_generated(page: Page):
    page.goto("https://example.com")
    page.click("text=Sign in")
    page.fill("input[type=email]", "user@example.com")
    page.fill("input[type=password]", "secret")
    page.click("button[type=submit]")
    assert page.url == "https://example.com/dashboard"
"""
    return {"code": code}
