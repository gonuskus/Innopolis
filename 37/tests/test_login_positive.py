# from models.login_page import UserData
import logging


def test_login_positive(app):
    """
        1. Open login page
        2. Input login data
        3. Press Login button
        4. Assert
    """
    # api_fabr.actions.common.api_login_with(organizer, debug=True)
    logging.info(f"Шаг 1 выполнен  для test_login_positive")
    app.pages.login_page.ViewLoginPage.open_login_page()
    pass
    '''user_data = UserData(login='super_qa_2021',
                             password='Password11!')
        app.login.authentication(user_data)
        print("Step4 - Assert")
        assert app.page.login_name_text() == Users.user
        #pass
        app.page.logout_user()'''
