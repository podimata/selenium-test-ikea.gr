import unittest
from selenium import webdriver
import page
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time


class SearchYoutube(unittest.TestCase):

    def setUp(self):
        options = FirefoxOptions()
        # options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=options)
        self.driver.get("https://www.ikea.gr/")

    def test_ikea_reject_cookies(self):
        main_page = page.MainPage(self.driver)
        time.sleep(1)
        main_page.ikea_reject_cookies()
        self.assertFalse(main_page.cookies_window_exists())

    def test_ikea_menu(self):
        main_page = page.MainPage(self.driver)
        time.sleep(1)
        main_page.ikea_reject_cookies()
        main_page.ikea_menu()
        self.assertTrue(main_page.menu_exists())

    def test_ikea_offers(self):
        main_page = page.MainPage(self.driver)
        time.sleep(1)
        main_page.ikea_reject_cookies()
        main_page.ikea_menu()
        main_page.ikea_offers()
        self.assertTrue(main_page.check_link_offers())

    def test_ikea_search(self):
        main_page = page.MainPage(self.driver)
        time.sleep(1)
        main_page.ikea_reject_cookies()
        main_page.ikea_search()
        self.assertTrue(main_page.search_results_page())

    def test_classification_products(self):
        main_page = page.MainPage(self.driver)
        time.sleep(1)
        main_page.ikea_reject_cookies()
        main_page.ikea_search()
        main_page.classification_products()

    def test_product_choice(self):
        main_page = page.MainPage(self.driver)
        time.sleep(1)
        main_page.ikea_reject_cookies()
        main_page.ikea_search()
        main_page.choice_table()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
