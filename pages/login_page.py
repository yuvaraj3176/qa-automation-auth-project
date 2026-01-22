from selenium.webdriver.common.by import By
from utils.wait_utils import wait_for_element_visible


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    login_button = (By.TAG_NAME, "button")
    error_message = (By.ID, "error")
    success_message = (By.ID, "success")

    def enter_username(self, username):
        field = wait_for_element_visible(self.driver, self.username_input)
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = wait_for_element_visible(self.driver, self.password_input)
        field.clear()
        field.send_keys(password)

    def click_login(self):
        wait_for_element_visible(self.driver, self.login_button).click()

    def get_error_message(self):
        return wait_for_element_visible(self.driver, self.error_message).text

    def get_success_message(self):
        return wait_for_element_visible(self.driver, self.success_message).text
