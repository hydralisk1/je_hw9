from pages.base_page import Page
from selenium.webdriver.common.by import By


class ResultPage(Page):
    SEARCH_RESULT = (By.CSS_SELECTOR, "span.a-color-state")

    def verify_result(self, item):
        item = f'"{item}"'
        self.verify_text(item, *self.SEARCH_RESULT)
