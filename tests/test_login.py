import csv
import logging
import pytest
from pages.login_page import LoginPage


def load_login_data():
    with open("testdata/login_data.csv", newline="") as file:
        return list(csv.DictReader(file))


@pytest.mark.parametrize("data", load_login_data())
def test_login_localhost(driver, data):
    logging.info("Starting localhost login test")

    driver.get("http://localhost:8000/login.html")

    login_page = LoginPage(driver)
    login_page.enter_username(data["username"])
    login_page.enter_password(data["password"])
    login_page.click_login()

    if data["expected"] == "success":
        assert "Login Successful" in login_page.get_success_message()
    else:
        assert data["expected"] in login_page.get_error_message()
