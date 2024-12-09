import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from utilities.ui_actions import UiActions


class HomePage(UiActions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    img_logo = (By.CSS_SELECTOR, "img[src='/images/Toolsqa.jpg']")
    url_homePage = "https://demoqa.com/books"
    btn_singIn = (By.ID, "login")

    # Actions
    def navi_to_homepage(self):
        self.driver.get(self.url_homePage)

    def is_logo_displayed(self):
        return self.is_element_visible(self.img_logo)

    def navi_to_login(self):
        self.navi_to_homepage()
        self.click_action(self.btn_singIn)
