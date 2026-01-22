from selenium.webdriver.common.by import By
from utils.wait_utils import wait_for_element_visible


class ForgotPasswordPage:

    def __init__(self, driver):
        self.driver = driver

    email_input = (By.ID, "email")
    retrieve_button = (By.ID, "form_submit")
    success_heading = (By.TAG_NAME, "h1")

    def enter_email(self, email):
        field = wait_for_element_visible(self.driver, self.email_input)
        field.clear()
        field.send_keys(email)

    def click_retrieve_password(self):
        wait_for_element_visible(self.driver, self.retrieve_button).click()

    def get_success_message(self):
        return wait_for_element_visible(self.driver, self.success_heading).text
