import logging

import pytest
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
    ),
    parser.addoption(
        "--username",
        action="store",
        default="fobiw39468@homedepinst.com",
        help="enter username",
    ),
    parser.addoption(
        "--password",
        action="store",
        default="Password11",
        help="enter password",
    )


@pytest.fixture()
def login(app, request):
    if app.get_url() != app.base_url:
        app.open_main_page()
    if not app.page.check_auth():
        login = request.config.getoption("--username")
        password = request.config.getoption("--password")
        user_data = UserData(login=login, password=password)
        app.login.authentication(user_data)
