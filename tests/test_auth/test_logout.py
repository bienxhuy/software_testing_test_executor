""" Test logout usecase.
"""
import pytest
from POM.student_dashboard_page.student_dashboard_page import StudentDashboardPage
from POM.student_dashboard_page.student_dashboard_page_notifications import StudentDashboardPageNotifications as Noti
import time


class TestLogout:
    """Test class for logout-related tests."""
    
    # Class-level fixture for StudentDashboardPage
    @pytest.fixture
    def student_dashboard(self, logged_in_student, driver):
        """Returns StudentDashboardPage instance for logged-in student."""
        return StudentDashboardPage(driver)
    
    # TC_UC:2_001
    # Verify user can logout successfully from the system.
    def test_student_logout_with_confirmation(self, student_dashboard, driver):
        """ Test student logout with confirmation dialog. """
        # Click logout button
        result = student_dashboard.logout()
        assert result == Noti.LOGOUT_BUTTON_CLICKED_SUCCESS, f"Logout click failed: {result}"
        
        # Verify confirmation dialog appears
        assert student_dashboard.is_logout_confirmation_dialog_displayed(), \
            "Expected confirmation dialog to appear after clicking logout, but no dialog was found. "
        
        # Confirm logout in the dialog
        confirm_result = student_dashboard.confirm_logout()
        assert "successfully" in confirm_result.lower(), f"Confirm button click failed: {confirm_result}"
        
        # Verify redirect to login page
        assert student_dashboard.is_logout_successful(), "Expected redirect to login page after confirming logout"
        
        # Verify user session is terminated (cannot access dashboard)
        driver.get(student_dashboard.BASE_URL + "/student/dashboard")
        # Should redirect back to login if session terminated
        assert "/login" in driver.current_url, "Session should be terminated - accessing dashboard should redirect to login"
    
    # TC_UC:2_002
    # Verify user cannot access Dashboard via browser Back button after logging out.
    def test_cannot_access_dashboard_after_logout_using_back_button(self, student_dashboard, driver):
        """ Test that user cannot return to dashboard using browser back button after logout. """
        # Store dashboard URL for verification
        dashboard_url = driver.current_url
        
        # Perform logout
        result = student_dashboard.logout()
        assert result == Noti.LOGOUT_BUTTON_CLICKED_SUCCESS, f"Logout click failed: {result}"
        
        # Verify redirect to login page after logout (has built-in wait)
        assert student_dashboard.is_logout_successful(timeout=15), f"Expected redirect to login page after logout. Current URL: {driver.current_url}"
        
        # Simulate clicking browser back button
        driver.back()
        time.sleep(2)
        
        # Verify still NOT on dashboard (should remain on login or redirect to login)
        current_url = driver.current_url
        assert current_url != dashboard_url, \
            f"Expected not to be on dashboard after using back button, but still on: {current_url}"
