from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from utilities.ui_actions import UiActions


class LoginPage(UiActions):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    txt_userName = (By.ID, "userName")
    txt_password = (By.ID, "password")
    btn_login = (By.ID, "login")
    elm_user_info = (By.ID, "userName-value")

    def login_action(self, email, password):
        self.fill_action(self.txt_userName, email)
        self.fill_action(self.txt_password, password)
        self.click_action(self.btn_login)

    def get_user_name(self):
        self.is_element_visible(self.elm_user_info)
        return self.get_text(self.elm_user_info)
