from pages.main_page import MainPage
from pages.search_bar import SearchBar
from pages.result_page import ResultPage
from pages.product_page import ProductPage


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.search_bar = SearchBar(self.driver)
        self.result_page = ResultPage(self.driver)
        self.product_page = ProductPage(self.driver)
