""" Test manage projects usecase.
"""
import pytest
from POM.instructor_dashboard_page.instructor_dashboard_page import InstructorDashboardPage


class TestManageProjects:
    """Test class for manage projects functionality."""
    
    # Class-level fixture for InstructorDashboardPage
    @pytest.fixture
    def instructor_dashboard(self, logged_in_instructor, driver):
        """Returns InstructorDashboardPage instance for logged-in instructor."""
        return InstructorDashboardPage(driver)
    
    # TC_UC:4_001
    # Verify Instructor is redirected to "Manage Projects" interface immediately after login.
    def test_instructor_redirected_to_manage_projects_after_login(self, instructor_dashboard, driver):
        """ Test that instructor sees manage projects interface after logging in. """
  
        # Verify instructor is on the manage projects page
        # Check that the "Tạo dự án mới" (Create Project) button is visible
        assert instructor_dashboard.is_create_project_button_visible(), \
            "Expected 'Tạo dự án mới' button to be visible on instructor dashboard after login"
        
        # Verify we're on the correct URL (instructor dashboard)
        assert "/instructor" in driver.current_url, \
            f"Expected to be on instructor dashboard page, but current URL is: {driver.current_url}"
    
    # TC_UC:4_003
    # Verify "Create Project" button navigates to the Create Project form correctly.
    def test_create_project_button_navigates_to_create_form(self, instructor_dashboard, driver):
        """ Test that clicking Create Project button navigates to create project form. """
        
        # Step 1: Click on "Tạo dự án mới" button
        instructor_dashboard.click_create_project_button()
        
        # Verify system redirects to Create Project Screen
        assert "/instructor/project/create" in driver.current_url, \
            f"Expected to be redirected to create project page, but current URL is: {driver.current_url}"
