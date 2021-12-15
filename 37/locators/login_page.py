from selenium.webdriver.common.by import By


class Authorization:
    LOGIN_BUTTON = (By.ID, 'loginbtn')
    LOGIN_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')
    ERROR_AUTH_TEXT = (By.XPATH, '//*[@class="alert alert-danger"]')

class Registration:
    LOGIN_INPUT = (By.ID, 'id_username')
    PASSWORD_INPUT = (By.ID, 'id_password')
    EMAIL_INPUT = (By.ID, 'id_email')
    EMAIL_DUPLICATE_INPUT = (By.ID, 'id_email2')
    FIRSTNAME_INPUT = (By.ID, 'id_firstname')
    SURNAME_INPUT = (By.ID, 'id_lastname')
    REGISTRATION_BUTTON = (By.ID, 'id_submitbutton')
    REGISTRATION_SUCCESS_TEXT = (By.XPATH, '//h2')
    ERROR_MSG_EMAIL_TEXT = (By.ID, 'id_error_email2')
    ERROR_MSG_EMAIL_UPLICATE_TEXT = (By.ID, 'id_error_email')
    ERROR_MSG_USERNAME_TEXT = (By.ID, 'id_error_username')
    ERROR_MSG_PASSWORD_TEXT = (By.ID, 'id_error_password')

