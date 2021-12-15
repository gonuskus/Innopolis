from selenium.webdriver.common.by import By


class MainPage:
    LOGIN = (By.CLASS_NAME, 'login')
    LOGIN_NAME = (By.CLASS_NAME, 'usertext')
    LOGOUT = (By.XPATH, "//a[contains(text(),'Выход')]")
