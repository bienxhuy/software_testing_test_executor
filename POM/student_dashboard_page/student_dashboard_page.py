from POM.student_dashboard_page.student_dashboard_page_notifications import StudentDashboardPageNotifications as Noti
from POM.base_page import BasePage
from POM.student_dashboard_page.student_dashboard_page_locators import StudentDashboardPageLocators as el
from selenium.webdriver.support.ui import WebDriverWait


class StudentDashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # Assuming the student dashboard URL is /student/dashboard
        # No need to navigate here, student should already be on dashboard after login
    
    # Logout method
    def logout(self):
        """Click logout button to log out from student dashboard."""
        return self.safe_click(
            el.LOGOUT_BUTTON,
            element="Logout Button",
            success_message=Noti.LOGOUT_BUTTON_CLICKED_SUCCESS,
        )
    
    # Verification method to check if logout was successful
    def is_logout_successful(self, timeout=5):
        """Check if logout was successful by verifying redirect to login page."""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: "/login" in driver.current_url
            )
            return True
        except:
            return False
