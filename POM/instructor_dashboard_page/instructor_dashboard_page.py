from POM.base_page import BasePage
from POM.instructor_dashboard_page.instructor_dashboard_page_locators import InstructorDashboardPageLocators as Locator
from POM.instructor_dashboard_page.instructor_dashboard_page_notifications import InstructorDashboardPageNotifications as Noti
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InstructorDashboardPage(BasePage):
  
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    # Check if create project button is visible
    def is_create_project_button_visible(self, timeout=10):
        """Check if the create project button is visible on the instructor dashboard."""
        try:
            button = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, Locator.CREATE_PROJECT_BUTTON))
            )
            return button.is_displayed()
        except:
            return False
    
    # Click create project button
    def click_create_project_button(self, timeout=10):
        """Click the create project button to navigate to create project form."""
        try:
            button = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, Locator.CREATE_PROJECT_BUTTON))
            )
            button.click()
            return Noti.CREATE_PROJECT_BUTTON_VISIBLE
        except Exception as e:
            return f"Error clicking create project button: {str(e)[:50]}"
