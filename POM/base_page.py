from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from dotenv import load_dotenv
import os


# Load environment variables from a .env file if present
load_dotenv()


# BasePage class    
class BasePage: 
    def __init__(self, driver):
        self.driver = driver
        self.BASE_URL = os.getenv("FRONTEND_BASE_URL", "http://localhost:3000")

    # This method safely clicks an element, waiting for it to be clickable
    def safe_click(self, locator, success_message, element="element", timeout=10):
        if not locator:
            return f"No locator for '{element}'"

        # Wait for the element to be clickable and click it
        try:
            element_object = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, locator))
            )
            element_object.click()
            return success_message

        except TimeoutException:
            return (f"Timeout while waiting for "
                    f"'{element}' to be clickable")

        except Exception as e:
            return (f"Error clicking '{element}'")

    # This method safely sends keys to an element, waiting for it to be clickable
    def safe_send_keys(self, locator, keys, success_message, element="element", timeout=10):
        if not locator:
            return f"No locator for '{element}'"

        # Wait for the element to be clickable and send keys to it
        try:
            element_object = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, locator))
            )
            element_object.clear()  # Clear existing text before sending keys
            element_object.send_keys(keys)
            return success_message

        except TimeoutException:
            return (f"Timeout while waiting for "
                    f"'{element}' to be clickable")

        except Exception as e:
            return (f"Error sending keys to '{element}'")
          
    # This method navigates to a specified URL
    def go_to_url(self, url):
        try:
            self.driver.get(url)
            return f"Navigated to URL: {url}"
        except Exception as e:
            return f"Error navigating to URL: {url}"
