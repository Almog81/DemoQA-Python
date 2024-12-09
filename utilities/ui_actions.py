import time

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UiActions:
    def __init__(self, driver, wait_time=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_time)

    def fill_action(self, locator, text):
        self.scrollIntoView(locator)
        field = self.wait.until(EC.visibility_of_element_located(locator))
        field.clear()
        field.send_keys(text)

    def click_action(self, locator):
        self.scrollIntoView(locator)
        button = self.wait.until(EC.element_to_be_clickable(locator))
        button.click()

    def drop_down_select(self, locator, text):
        field = self.wait.until(EC.visibility_of_element_located(locator))
        field.send_keys(text)

    def is_element_visible(self, locator):
        try:
            elem = self.wait.until(EC.visibility_of_element_located(locator))
            ActionChains(self.driver).scroll_to_element(elem).perform()
            return True
        except TimeoutException:
            return False

    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def scrollIntoView(self, locator):
        elem = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elem)