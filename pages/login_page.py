# POM - Login Page

from Project2_Orange_HRM.pages.locators import LoginPageLocator, DashboardPageLocator
from Project2_Orange_HRM.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    def field_verification(self):
        # Field Verification - Username and Password
        try:
            self.is_visible(LoginPageLocator.username_locator)
            self.is_visible(LoginPageLocator.password_locator)
            return True
        except:
            return False

    def login(self,username,password):
        # Fill the credentials
        self.enter_text(LoginPageLocator.username_locator,username)
        self.enter_text(LoginPageLocator.password_locator,password)
        self.click(LoginPageLocator.login_button_locator)

    def is_login_successful(self):
        try:
            # Check for successful login element
            self.is_visible(DashboardPageLocator.successful_login_locator)
            return True
        except:
            return False

    def is_login_failed(self):
        try:
            # Check for error message on failed login
            self.get_text(LoginPageLocator.error_message_locator)
            return True
        except:
            return False

    def verify_forgot_your_password_link(self,username):
        # Verification of forgot your password follow
        self.click(LoginPageLocator.forgot_your_password_locator)
        self.enter_text(LoginPageLocator.reset_password_username,username)
        self.click(LoginPageLocator.reset_password_button)
        return self.get_text(LoginPageLocator.reset_password_link_message)
