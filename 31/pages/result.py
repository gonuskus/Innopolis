from selenium.webdriver.common.by import By


class YaRuResultPage:

    def __init__(self, browser):
        self.browser = browser

    def link_div_count(self):
        link_divs = self.browser.find_elements(By.CSS_SELECTOR, '.OrganicTitleContentSpan')
        print(len(link_divs))
        return len(link_divs)
