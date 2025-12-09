# POM - Admin Page
import time

from Project2_Orange_HRM.pages.locators import AdminPageLocator, ClaimPageLocator
from Project2_Orange_HRM.pages.base_page import BasePage
from Project2_Orange_HRM.testdata.test_data import Newuser

class AdminPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    def adduser(self):
        # Click add user
        self.click(AdminPageLocator.adduser_locator)

    def fill_adduser_form(self):
        # Filling the add user form
        self.click(AdminPageLocator.adduser_userrole_locator)
        self.click(AdminPageLocator.adduser_userrole_admin)
        self.enter_text(AdminPageLocator.adduser_employee_name,Newuser.employee_name)
        self.click(AdminPageLocator.adduser_employee_name_searching)
        self.click(AdminPageLocator.adduser_status_locator)
        self.click(AdminPageLocator.adduser_status_enabled)
        self.enter_text(AdminPageLocator.adduser_username_locator,Newuser.new_username)
        self.enter_text(AdminPageLocator.adduser_password_locator,Newuser.password)
        self.enter_text(AdminPageLocator.adduser_confirmpassword_locator,Newuser.password)
        self.click(AdminPageLocator.adduser_save)
        self.wait_for_element(AdminPageLocator.adduser_loading_spinner)
        self.wait_for_invisibility(AdminPageLocator.adduser_loading_spinner)


    def user_search(self,new_username):
        # Searching the user in User Management
        self.click(AdminPageLocator.user_management_locator)
        self.click(AdminPageLocator.users_locator)
        self.enter_text(AdminPageLocator.search_username_locator,new_username)
        self.click(AdminPageLocator.search_button_locator)
        record_found = self.get_text(AdminPageLocator.username_verification)
        #print(record_found)
        if record_found == "(1) Record Found":
            return True
        else:
            return False