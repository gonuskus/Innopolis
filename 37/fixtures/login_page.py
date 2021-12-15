import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.login_page import Authorization, Registration
from models.login import UserData

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

    def sign_button_click(self):
        self._login_button().click()

    def _submit_login(self):
        return self.app.wd.find_element(*Authorization.SUBMIT_BUTTON)

    def authentication(self, user: UserData, submit=True):
        logger.info(f'Try to login with login: {user.login} and password: '
                    f'{user.password}')
        #self.sign_button_click()
        if user.login is not None:
            self._login_input().send_keys(user.login)
        if user.password is not None:
            self._password_input().send_keys(user.password)
        if submit:
            self._login_button().click()

    def error_auth_text(self):
        return self.app.wd.find_element(*Authorization.ERROR_AUTH_TEXT).text

    def helper_login(self):
        return self.app.wd.find_elements(*Authorization.LOGIN_HELPER_TEXT)

    def registration(self, user_data: UserData):
        logger.info(f'Try to login with login: {user_data.username} and password: '
                    f'{user_data.password}')
        if user_data.username is not None:
            self._registration_login_input().send_keys(user_data.username)
        if user_data.password is not None:
            self._registration_password_input().send_keys(user_data.password)
        if user_data.email is not None:
            self._registration_email_input().send_keys(user_data.email)
            self._registration_email_dublicate_input().send_keys(user_data.email)
        if user_data.firstname is not None:
            self._registration_firstname_input().send_keys(user_data.firstname)
        if user_data.surname is not None:
            self._registration_surname_input().send_keys(user_data.surname)
        self._registration_login_button().click()
        logger.info(f'Sended data for registration')


    def _registration_login_input(self):
        return self.app.wd.find_element(*Registration.LOGIN_INPUT)

    def _registration_password_input(self):
        return self.app.wd.find_element(*Registration.PASSWORD_INPUT)

    def _registration_email_input(self):
        return self.app.wd.find_element(*Registration.EMAIL_INPUT)

    def _registration_email_dublicate_input(self):
        return self.app.wd.find_element(*Registration.EMAIL_DUPLICATE_INPUT)

    def _registration_firstname_input(self):
        return self.app.wd.find_element(*Registration.FIRSTNAME_INPUT)

    def _registration_surname_input(self):
        return self.app.wd.find_element(*Registration.SURNAME_INPUT)

    def _registration_login_button(self):
        return self.app.wd.find_element(*Registration.REGISTRATION_BUTTON)

    def success_registration_text(self):
        return self.app.wd.find_element(*Registration.REGISTRATION_SUCCESS_TEXT).text

    def error_registration_text(self):
        return self.app.wd.find_element(*Registration.REGISTRATION_SUCCESS_TEXT).text

    def error_registration_username_text(self):
        return self.app.wd.find_element(*Registration.ERROR_MSG_USERNAME_TEXT).text

    def error_registration_password_text(self):
        return self.app.wd.find_element(*Registration.ERROR_MSG_PASSWORD_TEXT).text

    def error_registration_email_text(self):
        return self.app.wd.find_element(*Registration.ERROR_MSG_EMAIL_TEXT).text
