from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class SearchBar(Page):
    SELECT = (By.ID, "searchDropdownBox")
    SEARCH_BAR = (By.ID, "twotabsearchtextbox")

    def select_department(self, department):
        select = Select(self.find_element(*self.SELECT))
        select.select_by_visible_text(department)

    def search_for_product(self, product):
        self.input_text(product, *self.SEARCH_BAR, enter=True)