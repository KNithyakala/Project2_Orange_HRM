# POM - Dashboard Page

from Project2_Orange_HRM.pages.locators import DashboardPageLocator
from Project2_Orange_HRM.pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    def logout(self):
        try:
            # Logout
            self.click(DashboardPageLocator.successful_login_locator)
            self.click(DashboardPageLocator.logout_locator).click()
            return True
        except:
            return False

    def click_admin(self):
        # To click Admin menu
        self.is_visible(DashboardPageLocator.menu_items_locator["Admin"])
        self.click(DashboardPageLocator.menu_items_locator["Admin"])

    def click_myinfo(self):
        # To click Myinfo menu
        self.is_visible(DashboardPageLocator.menu_items_locator["MyInfo"])
        self.click(DashboardPageLocator.menu_items_locator["MyInfo"])

    def click_leave(self):
        # To click Leave menu
        self.is_visible(DashboardPageLocator.menu_items_locator["Leave"])
        self.click(DashboardPageLocator.menu_items_locator["Leave"])

    def click_claim(self):
        # To click Leave menu
        self.is_visible(DashboardPageLocator.menu_items_locator["Claim"])
        self.click(DashboardPageLocator.menu_items_locator["Claim"])

    def verify_menu_item(self,menu_name,expected_url):
        # To verify menu items
        locator = DashboardPageLocator.menu_items_locator[menu_name]

        # Check Visibility
        self.is_visible(locator)

        # Check Clickability
        self.is_clickable(locator)

        # Click the menu item
        self.click(locator)

        # Verify Navigation URL
        assert expected_url in self.get_current_url(), f"URL is not match for {menu_name}. Expected: {expected_url}, But displayed {self.get_current_url}"

