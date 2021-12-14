from selenium.webdriver.common.by import By


class ViewLoginPageLocators:
    LOGIN_BUTTON = (By.ID, 'loginbtn')
    LOGIN_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')
