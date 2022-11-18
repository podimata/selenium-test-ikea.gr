from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from locator import MainPageLocators


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    def ikea_reject_cookies(self):
        reject_cookies = WebDriverWait(self.driver, 10).until(
             EC.presence_of_element_located(MainPageLocators.REJECT_COOKIES)
        )
        reject_cookies.click()

    def cookies_window_exists(self):
        try:
            time.sleep(2)
            el = self.driver.find_element(*MainPageLocators.ELEMENT)
            opacity = el.value_of_css_property("opacity")
            return opacity == 1
        except NoSuchElementException as e:
            return False

    def ikea_menu(self):
        menu = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.MENU)
        )
        menu.click()

    def menu_exists(self):
        try:
            self.driver.find_element(*MainPageLocators.MENU_EXISTS)
            return True
        except NoSuchElementException as e:
            return False

    def ikea_offers(self):
        offers = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.OFFERS)
        )
        offers.click()

    def check_link_offers(self):
        return "Προσφορές" in self.driver.title

    def ikea_search(self):
        search = self.driver.find_element(*MainPageLocators.FILL_FORM)
        search.clear()
        search.send_keys("τραπέζι")
        search.send_keys(Keys.RETURN)
        time.sleep(3)

    def search_results_page(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(MainPageLocators.RESULTS)
            )
            return True
        except NoSuchElementException as e:
            return False

    def classification_products(self):
        product = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.CLASSIFICATION)
        )
        product.click()
        for option in self.driver.find_elements(*MainPageLocators.LIST):
            if option.text == "Τιμή αύξουσα":
                option.click()
                break

    def choice_table(self):
        choice_table = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.CHOICE_TABLE)
        )
        choice_table.click()
























