from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
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

    def check_link_prosfores(self):
        return "Προσφορές" in self.driver.title

























    # def ikea_search(self):
    #     search = WebDriverWait(self.driver, 10).until(
    #          EC.presence_of_element_located((By.XPATH, "//input[@class='searchInput']"))
    #     )
    #     search.send_keys("τραπέζι")






