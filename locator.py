from selenium.webdriver.common.by import By

class MainPageLocators(object):
    REJECT_COOKIES = (By.CSS_SELECTOR, ".nvcookies__button.nvcookies__button--primary.consent-reject")
    ELEMENT = (By.CSS_SELECTOR, "#required-cc")
    MENU = (By.CSS_SELECTOR, ".burgerBtn")
    MENU_EXISTS = (By.CSS_SELECTOR, "div.burger.open")
    OFFERS = (By.LINK_TEXT, "Προσφορές")
