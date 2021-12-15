from models.login import UserData
from tools.diction_constant import USER_NAME


def test_login_success(app):
    app.open_page("/login/index.php")
    user_data = UserData(login='super_qa_2021',
                         password='Password11!')
    app.login.authentication(user_data)
    assert app.page.login_name_text() == USER_NAME, \
        'Check name after authorization'
    app.page.logout_user()
