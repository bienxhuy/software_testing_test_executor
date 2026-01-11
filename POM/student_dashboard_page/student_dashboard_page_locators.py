class StudentDashboardPageLocators:
    # Menu Button
    MENU_BUTTON = "//button[@aria-label='Menu' or @aria-label='Open menu' or contains(@class, 'menu-button')] | /html/body/div/header/div/div[2]/button[2]"
    # Buttons
    LOGOUT_BUTTON = "//div[text()='Đăng xuất']"
    # Confirmation dialog (generic patterns for modal/dialog detection)
    LOGOUT_CONFIRMATION_DIALOG = "//div[contains(@class, 'modal') or contains(@class, 'dialog') or contains(@role, 'dialog') or contains(@class, 'confirm')]"
    LOGOUT_CONFIRM_BUTTON = "//button[contains(text(), 'Xác nhận') or contains(text(), 'Confirm') or contains(text(), 'OK') or contains(text(), 'Yes')]"
    LOGOUT_CANCEL_BUTTON = "//button[contains(text(), 'Hủy') or contains(text(), 'Cancel') or contains(text(), 'No')]"
