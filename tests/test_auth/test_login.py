""" Test login usecase.
"""
import pytest
from POM.notifications.login_page_notifications import LoginPageNotifications as Noti


class TestAuth:
    """Test class for authentication-related tests."""

    # TC_UC:1_001
    def test_student_login(self, login_page, student_account):
        """ Test student login with valid credentials. """
        # Perform login
        result = login_page.login(
            email=student_account["email"],
            password=student_account["password"]
        )
        
        # Verify login action completed
        assert result == Noti.LOGIN_BUTTON_CLICKED_SUCCESS, f"Login action failed: {result}"
        
        # Verify actual login success
        assert login_page.is_logged_in_as_student(), "Login verification failed: Not redirected to student dashboard"

    # TC_UC:1_002
    def test_instructor_login(self, login_page, instructor_account):
        """ Test instructor login with valid credentials. """
        # Perform login
        result = login_page.login(
            email=instructor_account["email"],
            password=instructor_account["password"]
        )
        
        # Verify login action completed
        assert result == Noti.LOGIN_BUTTON_CLICKED_SUCCESS, f"Login action failed: {result}"
        
        # Verify actual login success
        assert login_page.is_logged_in_as_instructor(), "Login verification failed: Not redirected to instructor dashboard"

    # TC_UC:1_003
    def test_admin_login(self, login_page, admin_account):
        """ Test admin login with valid credentials. """
        # Perform login
        result = login_page.login(
            email=admin_account["email"],
            password=admin_account["password"]
        )
        
        # Verify login action completed
        assert result == Noti.LOGIN_BUTTON_CLICKED_SUCCESS, f"Login action failed: {result}"
        
        # Verify actual login success
        assert login_page.is_logged_in_as_admin(), "Login verification failed: Not redirected to admin dashboard"