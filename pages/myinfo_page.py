# POM - MyInfo Page

from Project2_Orange_HRM.pages.locators import MyinfoPageLocator
from Project2_Orange_HRM.pages.base_page import BasePage


class MyinfoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_menu_item(self, menu_name, expected_url):
        # To verify menu items of MyInfo Page
        locator = MyinfoPageLocator.menu_items_locator[menu_name]

        # Check Visibility
        self.is_visible(locator)

        # Check Clickability
        self.is_clickable(locator)

        # Click the menu item
        self.click(locator)

        # Verify Navigation URL
        assert expected_url in self.get_current_url(), f"URL is not match for {menu_name}. Expected: {expected_url}, But displayed {self.get_current_url}"

