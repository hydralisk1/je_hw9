from pages.base_page import Page
from selenium.webdriver.common.by import By


class ProductPage(Page):
    NAV_MENUS = (By.CSS_SELECTOR, "a.nav-a.nav-hasArrow > span.nav-a-content")
    MEGA_MENU = (By.CSS_SELECTOR, "div.mega-menu")

    def open_product_page(self, product_no):
        self.open_page(f"https://www.amazon.com/gp/product/{product_no}")

    def hover_over_new_arrivals(self):
        new_arrivals = self.find_elements(*self.NAV_MENUS)[4]
        self.hover_over_element(new_arrivals)

    def verify_deals(self):
        self.wait_for_element_appear(*self.MEGA_MENU)


