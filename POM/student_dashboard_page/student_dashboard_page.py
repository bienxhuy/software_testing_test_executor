from POM.student_dashboard_page.student_dashboard_page_notifications import StudentDashboardPageNotifications as Noti
from POM.base_page import BasePage
from POM.student_dashboard_page.student_dashboard_page_locators import StudentDashboardPageLocators as el
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time


class StudentDashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    # Menu method
    def open_menu(self):
        """Click menu button to open the navigation menu."""
        try:
            # Find and click menu button
            menu_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, el.MENU_BUTTON))
            )
            menu_button.click()
            
            # Wait for the portal div[2] to appear with logout button
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[2]"))
            )
            
            # Wait for logout button to be clickable
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, el.LOGOUT_BUTTON))
            )
            
            return Noti.MENU_BUTTON_CLICKED_SUCCESS
            
        except Exception as e:
            return f"Error opening menu: {str(e)[:50]}"
    
    # Logout method
    def logout(self):
        """Click logout button to log out from student dashboard."""
        # First, try to find logout button WITHOUT opening menu
        # Maybe logout is directly visible on page
        try:
            logout_elements = self.driver.find_elements(By.XPATH, el.LOGOUT_BUTTON)
            if logout_elements:
                for elem in logout_elements:
                    if elem.is_displayed():
                        print("DEBUG: Found visible logout button without opening menu!")
                        elem.click()
                        time.sleep(2)  # Wait longer for logout action
                        return Noti.LOGOUT_BUTTON_CLICKED_SUCCESS
        except:
            pass
        
        # If not found, try opening menu
        menu_result = self.open_menu()
        if menu_result != Noti.MENU_BUTTON_CLICKED_SUCCESS:
            return menu_result
                
        # Try multiple click strategies on logout button
        try:
            logout_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, el.LOGOUT_BUTTON))
            )
            
            # Strategy 1: Normal Selenium click
            logout_button.click()
            time.sleep(1)
            
            # Check if logout initiated
            if "/login" in self.driver.current_url:
                return Noti.LOGOUT_BUTTON_CLICKED_SUCCESS
            
            # Strategy 2: JavaScript click if normal didn't work
            self.driver.execute_script("arguments[0].click();", logout_button)
            time.sleep(2)
            
            return Noti.LOGOUT_BUTTON_CLICKED_SUCCESS
            
        except Exception as e:
            return f"Error clicking logout: {str(e)[:50]}"
    
    # Verification method to check if logout was successful
    def is_logout_successful(self, timeout=10):
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
