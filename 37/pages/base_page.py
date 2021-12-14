from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains


class BasePage:
    """
    Общий класс для всех объектов страниц
    """

    def __init__(self, browser: 'browser_setup.Browser'):
        self.browser = browser
        self.timeout = 20
        self.action_chains = ActionChains(self.browser.wd)

    """
       Методы поиска элемента
       """

    def find(self, locator, timeout: int = None):
        self.wait_for_ready_state_complete()
        try:
            return self.wait_present(locator, timeout)
        except TimeoutException:
            raise NoSuchElementException(f"Не удалось найти локатор '{locator}'")
