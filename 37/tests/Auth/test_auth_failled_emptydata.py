from models.auth import AuthUserData
from tools.diction_constant import ERROR_MSG_USERNAME_TEXT, ERROR_MSG_PASSWORD_TEXT, ERROR_MSG_EMAIL_TEXT
import time


def test_auth_failled_empty_username(app):
    app.open_page("/login/signup.php?")
    new_user_data = AuthUserData().random_new_user()
    new_user_data.username = None
    app.login.registration(new_user_data)
    time.sleep(3)
    assert app.login.error_registration_username_text() == ERROR_MSG_USERNAME_TEXT, 'Check error message'



def test_auth_failled_empty_password(app):
    app.open_page("/login/signup.php?")
    new_user_data = AuthUserData().random_new_user()
    new_user_data.password = None
    app.login.registration(new_user_data)
    time.sleep(3)
    assert app.login.error_registration_password_text() == ERROR_MSG_PASSWORD_TEXT, 'Check error message'


def test_auth_failled_empty_email(app):
    app.open_page("/login/signup.php?")
    new_user_data = AuthUserData().random_new_user()
    new_user_data.email = None
    app.login.registration(new_user_data)
    time.sleep(3)
    assert app.login.error_registration_email_text() == ERROR_MSG_EMAIL_TEXT, 'Check error message'
