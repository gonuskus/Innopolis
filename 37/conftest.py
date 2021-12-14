import pytest
from fixtures.browser_setup import Browser

site_url = "https://qacoursemoodle.innopolis.university/"


# @pytest.fixture(scope="session")
@pytest.fixture(scope="session")
def app():
    browser = Browser(base_url=site_url)
    yield browser
    browser.wd.quit()

# @pytest.fixture(scope="function")
# def pages():
#     page_api = BrowserPages(base_url=site_url)
#     yield page_api
#     page_api.client.close_session()
