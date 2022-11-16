from selenium.webdriver.common.by import By


class MainPageLocators(object):
    REJECT_COOKIES = (By.CSS_SELECTOR, ".nvcookies__button.nvcookies__button--primary.consent-reject")
    ELEMENT = (By.ID, "#required-cc")
    MENU = (By.CSS_SELECTOR, ".burgerBtn")
    MENU_EXISTS = (By.CSS_SELECTOR, "div.burger.open")
    OFFERS = (By.LINK_TEXT, "Προσφορές")
    FILL_FORM = (By.XPATH, "//input[@class='searchInput']")
    RESULTS = (By.CSS_SELECTOR, ".mainTitle h1")
    CLASSIFICATION = (By.CSS_SELECTOR, ".filters .cnt .filerWrp .itm.sorting .dd.list-parameter-element i.icon")
    LIST = (By.CSS_SELECTOR, ".ddList ul li")

