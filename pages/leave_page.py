# POM - Leave Page
import time

from Project2_Orange_HRM.pages.locators import LeavePageLocator
from Project2_Orange_HRM.pages.base_page import BasePage
from Project2_Orange_HRM.testdata.test_data import Leave_details

class LeavePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_assign_leave(self):
        # Click Assign Leave
        self.click(LeavePageLocator.assign_leave_locator)

    def fill_leave_form(self):
        # Filling the Leave form with necessary details
        self.wait_for_element(LeavePageLocator.assign_locator)
        self.enter_text(LeavePageLocator.leave_employee_name_locator,Leave_details.employee_name)
        self.click(LeavePageLocator.leave_employee_name_searching)
        self.click(LeavePageLocator.leave_type_locator)
        self.click(LeavePageLocator.leave_type_option)
        self.enter_text(LeavePageLocator.from_date_locator,Leave_details.From_date)
        self.click(LeavePageLocator.to_date_locator)
        #time.sleep(5)
        self.click(LeavePageLocator.assign_locator)
        self.click(LeavePageLocator.confirm_leave_locator)
        self.click(LeavePageLocator.ok_button_locator)

    def verify_leave_list(self):
        self.click(LeavePageLocator.leave_list_locator)
        self.enter_text(LeavePageLocator.leave_list_employee_name_locator,Leave_details.employee_name)
        self.click(LeavePageLocator.leave_list_employee_name_searching)
        self.click(LeavePageLocator.show_leave_with_status)
        self.click(LeavePageLocator.show_leave_with_status_option)
        self.click(LeavePageLocator.search_locator)
        record_found= self.get_text(LeavePageLocator.employee_verification)
        if "Records Found" in record_found:
            return True
        else:
            return False
