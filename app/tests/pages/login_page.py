from .base_page import BasePage
from tests.utils.config import ORANGE_HRM

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # primary selectors
        self.user = "input[name='username']"
        self.passw = "input[name='password']"
        self.submit = "button[type='submit']"

    def open(self):
        self.goto(ORANGE_HRM)

    def login(self, username: str, password: str):
        self.fill(self.user, username, hint_label="Username")
        self.fill(self.passw, password, hint_label="Password")
        self.click(self.submit, hint_text="Login")
