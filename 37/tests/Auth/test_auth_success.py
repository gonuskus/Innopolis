from models.login import UserData
from models.auth import AuthUserData
from tools.diction_constant import SUCCESS_REGISTRATION_MSG


def test_auth_success(app):
    app.open_page("/login/signup.php?")
    new_user_data = AuthUserData().random_new_user()
    app.login.registration(new_user_data)
    app.open_page("/login/index.php")
    user_data = UserData(login=new_user_data.username,
                         password=new_user_data.password)
    app.login.authentication(user_data)
    assert app.login.success_registration_text() == SUCCESS_REGISTRATION_MSG, \
        'Check error message'
