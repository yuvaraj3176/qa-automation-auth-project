import pytest
import logging
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def setup_logging():
    logging.basicConfig(
        filename="logs/execution.log",
        filemode="a",
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )
    logging.info("===== Test Execution Started =====")


@pytest.fixture(scope="function")
def driver(request, setup_logging):
    logging.info("Launching Chrome browser")

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)

    # Attach driver to test request
    request.node.driver = driver

    yield driver

    logging.info("Closing browser")
    driver.quit()


# 🔥 Pytest hook: capture screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = getattr(item, "driver", None)

        if driver:
            screenshots_dir = "reports/screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"{screenshots_dir}/{item.name}_{timestamp}.png"

            driver.save_screenshot(screenshot_path)
            logging.error(f"Screenshot captured: {screenshot_path}")
