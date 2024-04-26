import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver


# Selenium 4 - TC

@pytest.mark.smoke
@allure.title("Verify that Login is working in app.vwo.com website")
@allure.description("TC#1 - Simple Login check on vwo.com Website.")
def test_vwo_login_positive():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    
    # Login Scenario - Run our Login multiple times with Excel File Data.
    
    allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType.PNG)
    driver.quit()
