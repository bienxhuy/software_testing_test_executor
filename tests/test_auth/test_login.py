""" Test login usecase.
"""
import pytest
from POM.pages.login_page import LoginPage
from POM.notifications.login_page_notifications import LoginPageNotifications as Noti


@pytest.fixture(scope="function")
def student_account():
    """ Provides a valid student account for testing. """
    return {
        "email": "alexander.nguyen@student.pose.edu",
        "password": "123456"
    }

# TC_UC:1_001
def test_student_login(driver, student_account):
    """ Test student login with valid credentials. """
    login_page = LoginPage(driver)

    # Perform login
    result = login_page.login(
        email=student_account["email"],
        password=student_account["password"]
    )

    # Assert login action completed successfully
    assert result == Noti.LOGIN_BUTTON_CLICKED_SUCCESS, f"Login action failed: {result}"
    
    # Verify logged in as student by checking URL
    assert login_page.is_logged_in_as_student(), "Login verification failed: Not redirected to student dashboard"