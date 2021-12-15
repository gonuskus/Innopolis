import logging

from fixtures.login_page import LoginPage
from fixtures.main_page import MainPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

logger = logging.getLogger()


class Application:
    def __init__(self, base_url):
        logger.setLevel('INFO')
        options: Options = Options()
        options.headless = True
        self.wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.login = LoginPage(self)
        self.page = MainPage(self)
        self.base_url = base_url

    def open_page(self, open_url):
        logger.info(f'Open {self.base_url}{open_url}')
        self.wd.get(self.base_url + open_url)

    def destroy(self):
        logger.info('Quit app')
        self.wd.quit()

    def get_url(self):
        return self.wd.current_url
