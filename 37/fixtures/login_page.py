import logging

from locators.login_page import Authorization
from models.login import UserData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

logger = logging.getLogger()


class LoginPage:
    def __init__(self, app):
        self.app = app

    def _password_input(self):
        return self.app.wd.find_element(*Authorization.PASSWORD_INPUT)

    def _login_input(self):
        element = (
            WebDriverWait(self.app.wd, 10).until(
                EC.presence_of_element_located(
                    Authorization.LOGIN_INPUT))
        )
        return element

    def _login_button(self):
        return self.app.wd.find_element(*Authorization.LOGIN_BUTTON)

    def authentication(self, user: UserData, submit=True):
        logger.info(f'Try to login with login: {user.login} and password: '
                    f'{user.password}')
        self.sign_button_click()
        if user.login is not None:
            self._login_input().send_keys(user.login)
        if user.password is not None:
            self._password_input().send_keys(user.password)
        if submit:
            self._submit_login().click()
