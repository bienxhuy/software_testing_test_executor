""" Test logout usecase.
"""
from POM.student_dashboard_page.student_dashboard_page import StudentDashboardPage


class TestLogout:
    """Test class for logout-related tests."""
    
    # TC_UC:2_001
    # Verify user can logout successfully from the system.
    def test_student_logout_with_confirmation(self, logged_in_student, driver):
        """ Test student logout with confirmation dialog. """
        # Initialize dashboard page (student is already logged in)
        dashboard = StudentDashboardPage(driver)
        
        # Click logout button
        result = dashboard.logout()
        assert result == "Logout button clicked successfully", f"Logout click failed: {result}"
        
        # Verify confirmation dialog appears
        assert dashboard.is_logout_confirmation_dialog_displayed(), \
            "Expected confirmation dialog to appear after clicking logout, but no dialog was found. "
        
        # Confirm logout in the dialog
        confirm_result = dashboard.confirm_logout()
        assert "successfully" in confirm_result.lower(), f"Confirm button click failed: {confirm_result}"
        
        # Verify redirect to login page
        assert dashboard.is_logout_successful(), "Expected redirect to login page after confirming logout"
        
        # Verify user session is terminated (cannot access dashboard)
        driver.get(dashboard.BASE_URL + "/student/dashboard")
        # Should redirect back to login if session terminated
        assert "/login" in driver.current_url, "Session should be terminated - accessing dashboard should redirect to login"
