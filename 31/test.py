import pytest
from pages.result import YaRuResultPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.search import YaRuSearchPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_search(browser):
    word = 'Python'
    search_page = YaRuSearchPage(browser)
    search_page.load()
    search_page.search(word)
    result_page = YaRuResultPage(browser)
    assert result_page.link_div_count() > 0
    
