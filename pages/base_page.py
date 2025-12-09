from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def click(self, locator):
        """Click element"""
        elem = self.is_clickable(locator)
        elem.click()

    def is_clickable(self,locator):
        """Check if element is clickable"""
        return self.wait.until(ec.element_to_be_clickable(locator))

    def enter_text(self, locator, text):
        """Wait and enter text"""
        elem = self.wait.until(ec.visibility_of_element_located(locator))
        elem.clear()
        elem.send_keys(text)

    def get_text(self, locator):
        """Get the text"""
        return self.wait.until(ec.visibility_of_element_located(locator)).text

    def is_visible(self, locator):
        """Check if element is visible"""
        return self.wait.until(ec.visibility_of_element_located(locator)).is_displayed()

    def open_url(self, url):
        """Open a URL"""
        self.driver.get(url)

    def wait_for_element(self, locator):
        """Explicit wait for any element"""
        return self.wait.until(ec.presence_of_element_located(locator))

    def get_current_url(self):
        """To get the current url of the driver"""
        return self.driver.current_url

    def wait_for_invisibility(self,locator):
        """Wait for element to invisible to proceed"""
        return self.wait.until(ec.invisibility_of_element(locator))

    def get_value(self,locator):
        """Getting value from disabled element"""
        input_element = self.driver.find_element(*locator)
        input_value = self.driver.execute_script("return arguments[0].value;", input_element)
        return input_value
