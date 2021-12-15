import logging
import os
import time

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
        driver = ChromeDriverManager().install()
        #self.wd = webdriver.Chrome(driver, options=options)
        self.wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.login = LoginPage(self)
        self.page = MainPage(self)
        self.base_url = base_url

    def open_page(self, open_url):
        #open_page_url = self.base_url + open_url
        logger.info(f'Open {self.base_url}{open_url}')
        self.wd.get(self.base_url+open_url)

    def destroy(self):
        logger.info('Quit app')
        self.wd.quit()

    def get_url(self):
        return self.wd.current_url

    def page_has_loaded(self, wait_time=5) -> bool:
        """
        Waiting for the page to load.
        """
        timestamp = time.time() + wait_time
        while time.time() < timestamp:
            page_state = self.wd.execute_script('return document.readyState;')
            if page_state == 'complete':
                logger.info(f'Page {self.get_url()} is load')
                return True
            time.sleep(0.5)
        logger.info(f"Error, page {self.get_url()} isn't load")
        return False

    @staticmethod
    def create_dir_for_report(dir_name):
        if not os.path.exists(dir_name):
            logger.info(f'Create dir {dir_name}')
            os.makedirs(dir_name)
