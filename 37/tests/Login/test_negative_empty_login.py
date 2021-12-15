from models.login import UserData
from tools.diction_constant import ERROR_LOGIN

def test_negative_empty_login(app):
    app.open_page("/login/index.php")
    user_data = UserData(login=None, password='password')
    app.login.authentication(user_data)
    assert app.login.error_auth_text() == ERROR_LOGIN, \
        'Check error message'
