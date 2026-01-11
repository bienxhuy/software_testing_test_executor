from POM.notifications.login_page_notifications import LoginPageNotifications as Noti
from POM.pages.base_page import BasePage
from POM.locators.login_page_locators import LoginPageLocators as el  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.go_to_url(self.BASE_URL + "/login")

    # Input methods
    def enter_email(self, email):
        return self.safe_send_keys(
            el.EMAIL_INPUT,
            keys=email,
            element="Email Input",
            success_message=Noti.EMAIL_INPUT_SUCCESS,
        )

    def enter_password(self, password):
        return self.safe_send_keys(
            el.PASSWORD_INPUT,
            keys=password,
            element="Password Input",
            success_message=Noti.PASSWORD_INPUT_SUCCESS,
        )

    # Button clicks
    def click_login_button(self):
        return self.safe_click(
            el.LOGIN_BUTTON,
            element="Login Button",
            success_message=Noti.LOGIN_BUTTON_CLICKED_SUCCESS,
        )

    # Action for full login
    def login(self, email, password):
        email_result = self.enter_email(email)
        if email_result != Noti.EMAIL_INPUT_SUCCESS:
            return email_result
        
        password_result = self.enter_password(password)
        if password_result != Noti.PASSWORD_INPUT_SUCCESS:
            return password_result
        
        return self.click_login_button()

    # Verification method to check if login was successful
    def is_login_successful(self, timeout=5):
        """Check if login was successful by verifying URL change."""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: "/login" not in driver.current_url
            )
            return True
        except:
            return False

    def is_logged_in_as_student(self, timeout=5):
        """Check if logged in as student by verifying URL contains /student/dashboard."""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: "/student/dashboard" in driver.current_url
            )
            return True
        except:
            return False

    def is_logged_in_as_instructor(self, timeout=5):
        """Check if logged in as instructor by verifying URL contains /instructor/dashboard."""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: "/instructor/dashboard" in driver.current_url
            )
            return True
        except:
            return False

    def is_logged_in_as_admin(self, timeout=5):
        """Check if logged in as admin by verifying URL contains /admin."""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: "/admin" in driver.current_url
            )
            return True
        except:
            return False

    def get_error_message_email(self, timeout=3):
        """Get error message email text if displayed."""
        try:
            error_element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, el.ERROR_MESSAGE_EMAIL))
            )
            return error_element.text
        except TimeoutException:
            return None
    
    def get_error_message_password(self, timeout=3):
        """Get error message password text if displayed."""
        try:
            error_element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, el.ERROR_MESSAGE_PASSWORD))
            )
            return error_element.text
        except TimeoutException:
            return None

    def is_still_on_login_page(self):
        """Check if still on login page (login failed)."""
        return "/login" in self.driver.current_url