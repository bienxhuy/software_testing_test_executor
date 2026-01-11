class StudentDashboardPageLocators:
    # Menu Button - exact path with fallback
    MENU_BUTTON = "/html/body/div[1]/header/div/div[2]/button[2] | //header/div/div[2]/button[2]"
    # Logout button - exact XPath
    LOGOUT_BUTTON = "/html/body/div[2]/div/div[4]"
    # Confirmation dialog (generic patterns for modal/dialog detection)
    LOGOUT_CONFIRMATION_DIALOG = "//div[contains(@class, 'modal') or contains(@class, 'dialog') or contains(@role, 'dialog') or contains(@class, 'confirm')]"
    LOGOUT_CONFIRM_BUTTON = "//button[contains(text(), 'Xác nhận') or contains(text(), 'Confirm') or contains(text(), 'OK') or contains(text(), 'Yes')]"
    LOGOUT_CANCEL_BUTTON = "//button[contains(text(), 'Hủy') or contains(text(), 'Cancel') or contains(text(), 'No')]"
