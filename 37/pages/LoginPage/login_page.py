from pages.base_page import BasePage
from locators.login_page import ViewLoginPageLocators

class ViewLoginPage(BasePage, ViewLoginPageLocators):
    """
     Объект страницы просмотра процедуры 600001
     """

    def open_login_page(self):
        self.browser.wd.get(self.browser.base_url + f"/login/index.php")
        self.wait_for_ready_state_complete()
        self.browser.asserts.assert_text_present_on_page("Forgotten your username or password?")

    """
    Методы получения данных из элементов
    """

    def get_procedure_draft_id(self):
        self.wait_for_ready_state_complete()
        return self.get_element_attribute(locator=self.PROCEDURE_FOOTER_PUBLISH, attribute='href').split("/")[-1]

    """
    Методы проверки содержимого полей
    """

    def check_organizer_name(self, organizer_name):
        self.browser.asserts.assert_element_visible(self._generate_procedure_organizer_name(organizer_name))

    """
    Методы кнопок боковой панели
    """
    def click_to_create_proposal(self):
        self.smart_click(self.GREEN_PROPOSAL_BUTTON)
        self.wait_for_ready_state_complete()
