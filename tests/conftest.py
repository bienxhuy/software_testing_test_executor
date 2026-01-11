import pytest
from selenium import webdriver
from POM.login_page.login_page import LoginPage


# This is a pytest fixture that provides the base URL for tests
# Base URL of the frontend application
@pytest.fixture(scope="session")
def frontend_base_url():
    return "http://fe:3000" 


# This is a pytest fixture that initializes a driver instance for testing
# Provides a driver instance to the tests
@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")  # Required for Docker
    options.add_argument("--disable-dev-shm-usage")  # Avoids issues with shared memory in Docker
    options.add_argument("--disable-gpu")  # Disable GPU in headless mode
    _driver = webdriver.Chrome(options=options)
    _driver.maximize_window()
    yield _driver
    _driver.quit()


# Account fixtures for different user roles
@pytest.fixture(scope="session")
def student_account():
    """Provides a valid student account for testing."""
    return {
        "email": "alexander.nguyen@student.pose.edu",
        "password": "123456"
    }


@pytest.fixture(scope="session")
def instructor_account():
    """Provides a valid instructor account for testing."""
    return {
        "email": "michael.roberts@pose.edu",
        "password": "123456"
    }


@pytest.fixture(scope="session")
def admin_account():
    """Provides a valid admin account for testing."""
    return {
        "email": "david.thompson@pose.edu",
        "password": "123456"
    }    


# Page object fixtures - return initialized page objects
@pytest.fixture
def login_page(driver):
    """Returns initialized LoginPage. Use when you need a fresh login page."""
    return LoginPage(driver)


# Action fixtures - perform actions to establish state
@pytest.fixture
def logged_in_student(login_page, student_account):
    """Logs in as student. Use when test requires authenticated student session."""
    login_page.login(student_account["email"], student_account["password"])
    if not login_page.is_logged_in_as_student():
        raise RuntimeError("Failed to establish logged-in student state")


@pytest.fixture
def logged_in_instructor(login_page, instructor_account):
    """Logs in as instructor. Use when test requires authenticated instructor session."""
    login_page.login(instructor_account["email"], instructor_account["password"])
    if not login_page.is_logged_in_as_instructor():
        raise RuntimeError("Failed to establish logged-in instructor state")


@pytest.fixture
def logged_in_admin(login_page, admin_account):
    """Logs in as admin. Use when test requires authenticated admin session."""
    login_page.login(admin_account["email"], admin_account["password"])
    if not login_page.is_logged_in_as_admin():
        raise RuntimeError("Failed to establish logged-in admin state")
