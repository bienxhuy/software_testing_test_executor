""" Test login usecase.
"""
import pytest
from POM.login_page.login_page_notifications import LoginPageNotifications as Noti


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

    # TC_UC:1_003
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

    # TC_UC:1_004
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
        
    # TC_UC:1_002
    # Verify Login failure with Incorrect Password
    def test_login_with_invalid_password(self, login_page, student_account):
        """ Test login with valid email but invalid password. """
        # Perform login with wrong password
        result = login_page.login(
            email=student_account["email"],
            password="wrong_password123"
        )
        
        # Verify login button was clicked
        assert result == Noti.LOGIN_BUTTON_CLICKED_SUCCESS, f"Login action failed: {result}"
        
        # Verify still on login page (login failed)
        assert login_page.is_still_on_login_page(), "Expected to stay on login page after failed login"
        
        # Verify error message is displayed
        error_message = login_page.get_error_message_email()
        assert error_message is not None, "Expected error message to be displayed"
        assert "500" in error_message or "failed" in error_message.lower(), f"Unexpected error message: {error_message}"
    
    # TC_UC:1_005
    # Verify Login failure when Email field is empty
    def test_login_with_empty_email(self, login_page, student_account):
        """ Test login with empty email field"""
        # Perform login with empty email
        result = login_page.login(
            email="",
            password=student_account["password"]
        )
        
        # Verify login button was clicked
        assert result == Noti.LOGIN_BUTTON_CLICKED_SUCCESS, f"Login action failed: {result}"
        
        # Verify still on login page (login failed)
        assert login_page.is_still_on_login_page(), "Expected to stay on login page after failed login"
        
        # Verify error message is displayed
        error_message = login_page.get_error_message_email()
        assert error_message is not None, "Expected error message to be displayed"
        assert "Tên đăng nhập là bắt buộc" in error_message, f"Expected 'Tên đăng nhập là bắt buộc' in error message, got: {error_message}"
    
    # TC_UC:1_006
    # Verify Login failure when Password field is empty
    def test_login_with_empty_password(self, login_page, student_account):
        """ Test login with empty password field"""
        # Perform login with empty password
        result = login_page.login(
            email=student_account["email"],
            password=""
        )
        
        # Verify login button was clicked
        assert result == Noti.LOGIN_BUTTON_CLICKED_SUCCESS, f"Login action failed: {result}"
        
        # Verify still on login page (login failed)
        assert login_page.is_still_on_login_page(), "Expected to stay on login page after failed login"
        
        # Verify error message is displayed
        error_message = login_page.get_error_message_password()
        assert error_message is not None, "Expected error message to be displayed"
        assert "Mật khẩu là bắt buộc" in error_message, f"Expected 'Mật khẩu là bắt buộc' in error message, got: {error_message}"
    
    # TC_UC:1_007
    # Verify Login failure with Unregistered Email
    def test_login_with_unregistered_email(self, login_page):
        """ Test login with email not registered in system. """
        # Perform login with unregistered email
        result = login_page.login(
            email="unregistered.user@example.com",
            password="anypassword123"
        )
        
        # Verify login button was clicked
        assert result == Noti.LOGIN_BUTTON_CLICKED_SUCCESS, f"Login action failed: {result}"
        
        # Verify still on login page (login failed)
        assert login_page.is_still_on_login_page(), "Expected to stay on login page after failed login"
        
        # Verify error message is displayed in email field
        error_message = login_page.get_error_message_email()
        assert error_message is not None, "Expected error message to be displayed in email field"
        
        # Check for expected user-friendly error message
        assert "Tài khoản không tồn tại" in error_message or "does not exist" in error_message.lower(), \
            f"Expected 'Tài khoản không tồn tại' or 'Account does not exist', but got: {error_message}"

    # TC_UC:1_008
    # Verify account is locked after 5 failed login attempts (Brute-force protection)
    def test_account_locked_after_failed_attempts(self, login_page, student_account):
        """ Test that account is locked after 5 consecutive failed login attempts. """
        max_attempts = 5
        
        # Attempt login 5 times with wrong password
        for attempt in range(1, max_attempts + 1):
            # Perform login with wrong password
            result = login_page.login(
                email=student_account["email"],
                password=f"wrong_password_{attempt}"
            )
            
            # Verify login button was clicked
            assert result == Noti.LOGIN_BUTTON_CLICKED_SUCCESS, f"Login action failed on attempt {attempt}: {result}"
            
            # Verify still on login page
            assert login_page.is_still_on_login_page(), f"Expected to stay on login page after attempt {attempt}"
            
            # On 5th attempt, check for account locked message
            if attempt == max_attempts:
                # Get error message from email field
                error_message = login_page.get_error_message_email()
                # Check for expected account locked message
                assert "Tài khoản đã bị khoá" in error_message or "Account locked" in error_message or "locked due to" in error_message.lower(), \
                    f"Expected account locked message after {max_attempts} attempts, but got: {error_message}"
        
        # Verify that subsequent login attempt is blocked (even with correct password)
        # This should fail if the account is truly locked
        result = login_page.login(
            email=student_account["email"],
            password=student_account["password"]  # Correct password
        )
        
        # Should still be on login page with locked account message
        assert login_page.is_still_on_login_page(), "Account should remain locked even with correct password"
        error_message = login_page.get_error_message_email()
        assert error_message is not None, "Expected locked account message"
        assert "Tài khoản đã bị khoá" in error_message or "Account locked" in error_message or "locked" in error_message.lower(), \
            f"Expected account locked message, but got: {error_message}"
    
    # Class-level fixtures for security testing
    @pytest.fixture(scope="function")
    def sql_injection_payload(self):
        """SQL injection payload for security testing."""
        return "' OR 1=1 --"
    
    @pytest.fixture(scope="function")
    def database_error_keywords(self):
        """List of database-related keywords that should not appear in error messages."""
        return ["sql", "syntax", "database", "query", "mysql", "postgres", "table", "column", "select", "insert"]    
    
    # TC_UC:1_009
    # Verify Login page is secure against SQL Injection.
    def test_sql_injection_protection(self, login_page, sql_injection_payload, database_error_keywords):
        """ Test that login form is protected against SQL injection attacks. """
        # Attempt login with SQL injection in email field
        result = login_page.login(
            email=sql_injection_payload,
            password="123456"
        )
        
        # Verify login button was clicked
        assert result == Noti.LOGIN_BUTTON_CLICKED_SUCCESS, f"Login action failed: {result}"
        
        # CRITICAL: Verify login was NOT successful (no unauthorized access)
        assert login_page.is_still_on_login_page(), "SQL injection should NOT grant access - must stay on login page"
        
        # Verify user was not logged in to any role
        assert not login_page.is_login_successful(timeout=2), "SQL injection should NOT grant any access"
        
        # Get error message
        error_message = login_page.get_error_message_email()
        assert error_message is not None, "Expected error message to be displayed"
        
        # Verify error message is generic (not database error leak)
        # Should NOT contain database error keywords
        error_lower = error_message.lower()
        
        for keyword in database_error_keywords:
            assert keyword not in error_lower, \
                f"Security risk: Error message leaks database information. Found '{keyword}' in: {error_message}"
        
        # Verify error message is user-friendly (not technical error code)
        # Should show generic user-friendly message
        assert "400" not in error_message and "500" not in error_message and "status code" not in error_lower, \
            f"Expected user-friendly error message, but got technical error: {error_message}"

    # TC_UC:2_001
    # Verify user can logout successfully from the system.
    