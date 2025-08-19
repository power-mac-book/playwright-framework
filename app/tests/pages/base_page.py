from playwright.sync_api import Page
from tests.utils.ai_heal import smart_click, smart_fill

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url)

    # “AI-healable” actions (wraps raw actions with fallback heuristics)
    def click(self, selector: str, hint_text: str | None = None):
        smart_click(self.page, selector, hint_text)

    def fill(self, selector: str, value: str, hint_label: str | None = None):
        smart_fill(self.page, selector, value, hint_label)
