# POM - Claim Page
import time

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from Project2_Orange_HRM.pages.locators import ClaimPageLocator
from Project2_Orange_HRM.pages.base_page import BasePage
from Project2_Orange_HRM.testdata.test_data import Claims_details


class ClaimPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    def click_submit_claim(self):
        self.click(ClaimPageLocator.submit_claim_locator)

    def create_claim_request(self):
        self.click(ClaimPageLocator.event_locator)
        self.click(ClaimPageLocator.event_option)
        self.click(ClaimPageLocator.currency_locator)
        self.click(ClaimPageLocator.currency_option)
        self.click(ClaimPageLocator.create_button_locator)

    def add_expenses(self):
        self.wait_for_invisibility(ClaimPageLocator.loading_spinner)
        self.click(ClaimPageLocator.expenses_add_button)
        self.click(ClaimPageLocator.expense_type)
        self.click(ClaimPageLocator.expense_type_option)
        self.enter_text(ClaimPageLocator.date_locator, Claims_details.claim_date)
        self.enter_text(ClaimPageLocator.amount_locator,Claims_details.amount)
        self.click(ClaimPageLocator.save_button_locator)

    def submit_claim(self):
        self.wait_for_invisibility(ClaimPageLocator.loading_spinner)
        self.click(ClaimPageLocator.submit_button_locator)
        return self.get_value(ClaimPageLocator.reference_id_locator)

    def verify_claim_record(self,ref_id):
        self.click(ClaimPageLocator.my_claims_locator)
        self.wait_for_invisibility(ClaimPageLocator.loading_spinner)
        self.enter_text(ClaimPageLocator.my_claims_reference_id,ref_id)
        self.click(ClaimPageLocator.my_claims_reference_id_option)
        self.click(ClaimPageLocator.search_button_locator)
        record = self.get_text(ClaimPageLocator.record_locator)
        if record == "(1) Record Found":
            return True
        else:
            return False





