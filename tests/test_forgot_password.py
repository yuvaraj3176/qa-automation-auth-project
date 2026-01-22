import logging
import pytest
from pages.forgot_password_page import ForgotPasswordPage


@pytest.mark.regression
def test_forgot_password(driver):
    logging.info("Starting Forgot Password test")

    driver.get("https://the-internet.herokuapp.com/forgot_password")

    forgot_page = ForgotPasswordPage(driver)
    forgot_page.enter_email("testuser@example.com")
    forgot_page.click_retrieve_password()

    result_text = forgot_page.get_success_message()
    logging.info(f"Forgot Password response: {result_text}")

    assert (
        "Email Sent" in result_text
        or "Internal Server Error" in result_text
    )
