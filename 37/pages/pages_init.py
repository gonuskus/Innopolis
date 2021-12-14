from pages.LoginPage.login_page import ViewLoginPage


class BrowserPages:
    """
    Класс-инициализатор для объектов страниц Фабрикант (новая архитектура)
    """

    def __init__(self, browser):
        self.login_page = ViewLoginPage(browser)
        self.main_page = MainPage(browser)
