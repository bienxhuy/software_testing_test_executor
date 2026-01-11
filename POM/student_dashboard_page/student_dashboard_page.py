from POM.student_dashboard_page.student_dashboard_page_notifications import StudentDashboardPageNotifications as Noti
from POM.base_page import BasePage
from POM.student_dashboard_page.student_dashboard_page_locators import StudentDashboardPageLocators as el
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class StudentDashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    # Logout method
    def logout(self):
        """Click logout button to log out from student dashboard."""
        # Open menu first if necessary
        self.safe_click(
          el.MENU_BUTTON,
          element="Menu Button",
          success_message=Noti.MENU_BUTTON_CLICKED_SUCCESS,
        )
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
    
    # Check if confirmation dialog appears
    def is_logout_confirmation_dialog_displayed(self, timeout=3):
        """Check if confirmation dialog is displayed after clicking logout."""
        try:
            dialog = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, el.LOGOUT_CONFIRMATION_DIALOG))
            )
            return dialog.is_displayed()
        except TimeoutException:
            return False
    
    # Confirm logout in dialog
    def confirm_logout(self):
        """Click confirm button in logout confirmation dialog."""
        return self.safe_click(
            el.LOGOUT_CONFIRM_BUTTON,
            element="Confirm Button",
            success_message="Confirm button clicked successfully",
        )
    
    # Cancel logout in dialog
    def cancel_logout(self):
        """Click cancel button in logout confirmation dialog."""
        return self.safe_click(
            el.LOGOUT_CANCEL_BUTTON,
            element="Cancel Button",
            success_message="Cancel button clicked successfully",
        )
