import unittest
from selenium import webdriver
import page
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time

class SearchYoutube(unittest.TestCase):

    def setUp(self):
        options = FirefoxOptions()
        options.add_argument("--headless")
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
        self.assertTrue(main_page.check_link_prosfores())


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
