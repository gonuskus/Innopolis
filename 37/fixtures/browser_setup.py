import logging

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.pages_init import BrowserPages
logger = logging.getLogger()


class Browser:
    """
    Класс инициализации объекта веб-драйвера
    """
    def __init__(self, browser, base_url):
        self.pages = BrowserPages(self)
        self.base_url = base_url
        self.wd = self.driver_setup( browser=browser)

    @staticmethod
    def driver_setup():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(20)
        return driver

