#Locators - elements

from selenium.webdriver.common.by import By
from Project2_Orange_HRM.testdata.test_data import Leave_details, Newuser

class LoginPageLocator():
    # login page - elements - locators
    username_locator = (By.XPATH,'//input[@placeholder="Username"]')
    password_locator = (By.XPATH, '//input[@placeholder="Password"]')
    login_button_locator = (By.XPATH, '//button[@type="submit"]')
    error_message_locator = (By.XPATH, '//div[@class="oxd-alert-content oxd-alert-content--error"]')
    forgot_your_password_locator = (By.XPATH,'//p[@class="oxd-text oxd-text--p orangehrm-login-forgot-header"]')
    reset_password_username = (By.XPATH,'//input[@name="username"]')
    reset_password_button = (By.XPATH,'//button[@type="submit"]')
    reset_password_link_message = (By.XPATH,'//h6[@class="oxd-text oxd-text--h6 orangehrm-forgot-password-title"]')

class DashboardPageLocator():
    # dashboard page - elements - locators
    successful_login_locator = (By.XPATH, '//li[@class="oxd-userdropdown"]')
    logout_locator = (By.XPATH,'//a[text()="Logout"]')
    menu_items_locator = {
    "Admin" : (By.XPATH,'//span[text()="Admin"]'),
    "PIM" : (By.XPATH,'//span[text()="PIM"]'),
    "Time" : (By.XPATH,'//span[text()="Time"]'),
    "Recruitment" : (By.XPATH,'//span[text()="Recruitment"]'),
    "Performance" : (By.XPATH,'//span[text()="Performance"]'),
    "MyInfo": (By.XPATH,'//span[text()="My Info"]'),
    "Leave" : (By.XPATH,'//span[text()="Leave"]'),
    "Claim" : (By.XPATH,'//span[text()="Claim"]'),
    "Dashboard" :(By.XPATH,'//span[text()="Dashboard"]')
    }
class AdminPageLocator():
    # admin page - user management - elements - locators
    user_management_locator = (By.XPATH,'//span[text()="User Management "]')
    users_locator =(By.XPATH,'//a[contains(text(),"Users")]')

    # Add user
    adduser_locator = (By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]')
    adduser_userrole_locator = (By.XPATH,'(//div[@class="oxd-select-text oxd-select-text--active"])[1]')
    adduser_userrole_admin = (By.XPATH,'//div[@role="option"][3]')
    adduser_status_locator = (By.XPATH,'(//div[@class="oxd-select-text oxd-select-text--active"])[2]')
    adduser_status_enabled = (By.XPATH,'//div[@role="option"][2]')
    adduser_employee_name = (By.XPATH,'//input[@placeholder="Type for hints..."]')
    adduser_employee_name_searching =(By.XPATH,f'//div[@role="option"]//span[contains(text(),{Newuser.employee_name})]')
    adduser_username_locator = (By.XPATH,'//label[text()="Username"]/following::input[1]')
    adduser_password_locator = (By.XPATH,'//label[text()="Password"]/following::input[1]')
    adduser_confirmpassword_locator = (By.XPATH,'//label[text()="Confirm Password"]/following::input[1]')
    adduser_save = (By.XPATH,'//button[text()=" Save "]')

    # loading spinner locator
    adduser_loading_spinner = (By.XPATH,'//*[@class="oxd-loading-spinner"]')

    # search the user
    search_username_locator = (By.XPATH,'//label[text()="Username"]/following::input[1]')
    search_button_locator = (By.XPATH,'//button[@type="submit"]')
    username_verification = (By.XPATH,'//span[@class="oxd-text oxd-text--span"]')

class MyinfoPageLocator():
    # my info page - - elements - locators
    menu_items_locator = {
        "Personal_Details": (By.XPATH,'//a[text()="Personal Details"]'),
        "Contact_Details": (By.XPATH,'//a[text()="Contact Details"]'),
        "Emergency_Contacts": (By.XPATH,'//a[text()="Emergency Contacts"]'),
        "Dependents": (By.XPATH,'//a[text()="Dependents"]'),
        "Immigration": (By.XPATH,'//a[text()="Immigration"]'),
        "Job": (By.XPATH,'//a[text()="Job"]'),
        "Salary": (By.XPATH,'//a[text()="Salary"]'),
        "Report-to": (By.XPATH,'//a[text()="Report-to"]'),
        "Qualifications": (By.XPATH,'//a[text()="Qualifications"]'),
        "Memberships": (By.XPATH,'//a[text()="Memberships"]')
    }

class LeavePageLocator():

    # leave page - - elements - locators
    more_menu_locator = (By.XPATH,'//span[text()="More "]')
    assign_leave_locator = (By.XPATH,'//a[text()="Assign Leave"]')
    leave_employee_name_locator= (By.XPATH,'//input[@placeholder="Type for hints..."]')
    leave_employee_name_searching = (By.XPATH,
                                     f'//div[@role="option"]//span[contains(text(),{Leave_details.employee_name})]')
    leave_type_locator = (By.XPATH,'//label[text()="Leave Type"]/following::div[1]')
    leave_type_option = (By.XPATH,'//div[@role="option"][4]')

    from_date_locator = (By.XPATH,'//label[text()="From Date"]/following::input[1]')
    to_date_locator = (By.XPATH, '//label[text()="To Date"]/following::input[1]')

    assign_locator = (By.XPATH,'//button[@type="submit"]')
    confirm_leave_locator = (By.XPATH,'//div[@role="document"]//p[text()="Confirm Leave Assignment"]')
    ok_button_locator= (By.XPATH,'//button[text()=" Ok "]')

    leave_list_locator = (By.XPATH,'//a[text()="Leave List"]')
    leave_list_employee_name_locator = (By.XPATH,'//input[@placeholder="Type for hints..."]')
    leave_list_employee_name_searching = (By.XPATH,
                                     f'//div[@role="option"]//span[contains(text(),{Leave_details.employee_name})]')

    show_leave_with_status = (By.XPATH,'//label[text()="Show Leave with Status"]/following::div[1]')
    show_leave_with_status_option = (By.XPATH,'//div[@role="option"][3]')
    search_locator = (By.XPATH,'//button[@type="submit"]')
    employee_verification = (By.XPATH, '//span[@class="oxd-text oxd-text--span"]')


class ClaimPageLocator():
    #claim page - elements - locators
    submit_claim_locator = (By.XPATH,'//a[text()="Submit Claim"]')
    event_locator = (By.XPATH,'(//div[@class="oxd-select-text-input"])[1]')
    event_option = (By.XPATH,'//div[@role="option"][3]') #Medical Reimbursement
    currency_locator = (By.XPATH,'(//div[@class="oxd-select-text-input"])[2]')
    currency_option = (By.XPATH,'//div[@role="option"][63]') # Indian rupee
    create_button_locator = (By.XPATH,'//button[@type="submit"]')

    # claim no
    reference_id_locator = (By.XPATH,'//label[text()="Reference Id"]/following::input[1]')

    # loading spinner locator
    loading_spinner = (By.XPATH,'//*[@class="oxd-loading-spinner"]')

    # adding expenses locator
    expenses_add_button = (By.XPATH,'(//button[@class="oxd-button oxd-button--medium oxd-button--text"])[1]')
    expense_type = (By.XPATH,'//div[@class="oxd-select-text-input"]')
    expense_type_option = (By.XPATH,'//div[@role="option"][4]') # option - Planned Surgery
    date_locator = (By.XPATH,'//label[text()="Date"]/following::input[1]')
    amount_locator = (By.XPATH,'//label[text()="Amount"]/following::input[1]')
    save_button_locator = (By.XPATH,'//button[@type="submit"]') # adding expenses saving

    # claim submission
    submit_button_locator = (By.XPATH,'//button[text()=" Submit "]')

    # My claims
    my_claims_locator = (By.XPATH,'//a[text()="My Claims"]')
    my_claims_reference_id = (By.XPATH,'//label[text()="Reference Id"]/following::input[1]')
    my_claims_reference_id_option =(By.XPATH,'//div[@role="option"][1]')
    search_button_locator = (By.XPATH,'//button[text()=" Search "]')
    record_locator = (By.XPATH, '(//span[@class="oxd-text oxd-text--span"])[1]')

