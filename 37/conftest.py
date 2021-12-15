import pytest
import logging
from fixtures.application import Application
from models.login import UserData

logger = logging.getLogger()


@pytest.fixture(scope="session")
def app(request):
    base_url = request.config.getoption("--base-url")
    fixture = Application(base_url)
    fixture.wd.implicitly_wait(10)
    fixture.wd.maximize_window()
    yield fixture
    fixture.destroy()


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://qacoursemoodle.innopolis.university",
        help="enter base_url",
    )
