import logging
import pytest
import os

from Project2_Orange_HRM.pages.claim_page import ClaimPage
from Project2_Orange_HRM.pages.login_page import LoginPage
from Project2_Orange_HRM.pages.dashboard_page import DashboardPage
from Project2_Orange_HRM.pages.admin_page import AdminPage
from Project2_Orange_HRM.pages.myinfo_page import MyinfoPage
from Project2_Orange_HRM.pages.leave_page import LeavePage
from Project2_Orange_HRM.tests.excelreader import ExcelDataProvider
from Project2_Orange_HRM.testdata.test_data import Newuser, Menu_items, Myinfo_menu_items

@pytest.mark.usefixtures("setup")
class TestLogin:
    # Test case 1 - Validate login functionality using multiple sets of credentials
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_case1(self,base_url):
        # Initialize data provider
        root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        test_data_path = os.path.join(root_path,"testdata","test_data_login.xlsx")
        data_provider = ExcelDataProvider(test_data_path)
        test_cases = data_provider.get_test_data()  # [(test_id,username,password)]
        # Opening Orange HRM
        self.driver.get(base_url)
        # Initialize page object - Login
        login_page = LoginPage(self.driver)
        dashboard_page = DashboardPage(self.driver)

        for test_id, username, password in test_cases:
            # Perform login
            login_page.login(username,password)

            # Check result and write to Excel
            if login_page.is_login_successful():
                dashboard_page.logout()
                data_provider.write_result(test_id, "PASS")
            elif login_page.is_login_failed():
                data_provider.write_result(test_id, "FAIL")
            else:
                data_provider.write_result(test_id, "ERROR")

        data_provider.close()

    # Test case 2 - Verify that the home URL is accessible
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_case2(self,base_url):
            try:
                # Opening Orange HRM
                self.driver.get(base_url)
                assert self.driver.current_url == base_url, f"Expected {base_url}, but got {self.driver.current_url}."
                logging.info("Orange HRM application is opened correctly.")

            except Exception as e:
                logging.error(f"Expected {base_url}, but got {self.driver.current_url}. Got error {e}")
                raise

    # Test case 3 - Validate presence of login fields
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_case3(self,base_url):
            try:
                # Opening Orange HRM
                self.driver.get(base_url)
                # Initialize page object - Login
                login_page = LoginPage(self.driver)
                assert login_page.field_verification(), f"Username and Password fields are not visible."
                logging.info("Username and Password are visible.")

            except Exception as e:
                logging.error(f"Got error:{e}")
                raise

    # Test case 4 - Verify visibility and clickability of main menu items after login
    @pytest.mark.regression
    def test_case4(self,base_url,test_credentials):
            try:
                # Opening Orange HRM
                self.driver.get(base_url)
                # Initialize page object - Login
                login_page = LoginPage(self.driver)
                # Perform Login
                login_page.login(test_credentials["username"], test_credentials["password"])
                # Initialize page object - Dashboard
                dashboard_page = DashboardPage(self.driver)
                # Verifying Menu Items visibility and clickability
                for menu_name, expected_url in Menu_items.expectedurls.items():
                    dashboard_page.verify_menu_item(menu_name,expected_url)
                    self.driver.back() # Go back to verify next menu item

                logging.info("Menu items are displayed as expected.")

            except Exception as e:
                logging.error(f"Got error:{e}")
                raise

    # Test case 5 - Create a new user and validate login
    @pytest.mark.regression
    def test_case5(self,base_url,test_credentials):
        try:
            # Opening Orange HRM
            self.driver.get(base_url)
            # Initialize page object - Login
            login_page = LoginPage(self.driver)
            # Perform Login
            login_page.login(test_credentials["username"], test_credentials["password"])
            # Initialize page object - Dashboard
            dashboard_page = DashboardPage(self.driver)
            # Clicking Admin menu
            dashboard_page.click_admin()
            # Initialize page object - Admin
            admin_page = AdminPage(self.driver)
            # Adding New user
            admin_page.adduser()
            admin_page.fill_adduser_form()
            # Logout - admin
            dashboard_page.logout()
            # Perform login with newly add user
            login_page.login(Newuser.new_username,Newuser.password)

            assert login_page.is_login_successful(), f"Newly add user is not able to login."
            logging.info("Newly add user is able to login.")
            # Logout - New user
            dashboard_page.logout()

        except Exception as e:
            logging.error(f"Got error:{e}")
            raise

    # Test Case 6 - Validate presence of the newly created user in the admin user list
    @pytest.mark.regression
    def test_case6(self,base_url,test_credentials):
        try:
            # Opening Orange HRM
            self.driver.get(base_url)
            # Initialize page object - Login
            login_page = LoginPage(self.driver)
            # Perform Login
            login_page.login(test_credentials["username"],test_credentials["password"])
            # Initialize page object - Dashboard
            dashboard_page = DashboardPage(self.driver)
            # Clicking Admin Menu
            dashboard_page.click_admin()
            # Initialize page object - Admin
            admin_page = AdminPage(self.driver)
            # Searching newly add user (test_case5)
            record_found = admin_page.user_search(Newuser.new_username)
            # Verifying newly add user in user list
            assert record_found, f"Newly added user is not found in user listing."
            logging.info("Newly added user is found in user listing.")

        except Exception as e:
            logging.error(f"Got error:{e}")
            raise

    # Test case 7 - Verify "Forgot Password" link functionality
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_case7(self,base_url,test_credentials):
            try:
                # Opening Orange HRM
                self.driver.get(base_url)
                # Initialize page object - Login
                login_page = LoginPage(self.driver)
                # Verifying "Forgot Password" link functionality
                message=login_page.verify_forgot_your_password_link(test_credentials["username"])
                assert "Reset Password link sent successfully" in message, f"Reset password link is not sent."
                logging.info("Reset Password link is working as expected.")

            except Exception as e:
                logging.error(f"Got error:{e}")
                raise

    # Test case 8 - Validate the presence of menu items under “My Info”
    @pytest.mark.regression
    def test_case8(self,base_url,test_credentials):
            try:
                # Opening Orange HRM
                self.driver.get(base_url)
                # Initialize page object - Login
                login_page = LoginPage(self.driver)
                # Perform Login
                login_page.login(test_credentials["username"], test_credentials["password"])
                # Initialize page object - Dashboard
                dashboard_page = DashboardPage(self.driver)
                # Clicking Myinfo menu
                dashboard_page.click_myinfo()
                # Initialize page object - Myinfo
                myinfo_page = MyinfoPage(self.driver)
                # Verifying the menu items under "My Info"
                for menu_name, expected_url in Myinfo_menu_items.expectedurls.items():
                    myinfo_page.verify_menu_item(menu_name, expected_url)
                logging.info("Menu items in Myinfo Page are working as expected.")

            except Exception as e:
                logging.error(f"Got error:{e}")
                raise

    # Test case 9 - Assign leave to an employee and verify assignment
    @pytest.mark.regression
    def test_case9(self,base_url,test_credentials):
            try:
                # Opening Orange HRM
                self.driver.get(base_url)
                # Initialize page object - Login
                login_page = LoginPage(self.driver)
                # Perform Login
                login_page.login(test_credentials["username"], test_credentials["password"])
                # Initialize page object - Dashboard
                dashboard_page = DashboardPage(self.driver)
                # Clicking Leave Menu
                dashboard_page.click_leave()
                # Initialize page object - Leave
                leave_page = LeavePage(self.driver)
                # Clicking Assign Leave under Leave menu
                leave_page.click_assign_leave()
                # Leave form filling
                leave_page.fill_leave_form()
                # verifying record creation
                record_found = leave_page.verify_leave_list()
                assert record_found, "Leave is not submitted successfully."
                logging.info("Leave is submitted successfully.")

            except Exception as e:
                logging.error(f"Got error:{e}")
                raise

    # Test case 10 - Initiate a claim request
    @pytest.mark.regression
    def test_case10(self,base_url):
            try:
                # Opening Orange HRM
                self.driver.get(base_url)
                # Initialize page object - Login
                login_page = LoginPage(self.driver)
                # Perform Login
                login_page.login(Newuser.new_username,Newuser.password)
                # Initialize page object - Dashboard
                dashboard_page = DashboardPage(self.driver)
                # Clicking Claim Menu
                dashboard_page.click_claim()
                # Initialize page object - Claim
                claim_page = ClaimPage(self.driver)
                # Clicking Submit Claim button
                claim_page.click_submit_claim()
                # Creating claim request
                claim_page.create_claim_request()
                # Adding the expenses
                claim_page.add_expenses()
                # Submitting claim and getting reference id
                ref_id_submit_claim=claim_page.submit_claim()
                print(ref_id_submit_claim)

                # Searching claim reference id in my claims page
                record_found=claim_page.verify_claim_record(ref_id_submit_claim)

                # Verify claim record
                assert record_found, f"Claim is not submitted"

            except Exception as e:
                logging.error(f"Got error:{e}")
                raise