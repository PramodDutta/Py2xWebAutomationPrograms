import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException)



# Selenium 4 - TC

@pytest.mark.smoke
@allure.title("Verify that Login is working in app.vwo.com website")
@allure.description("TC#1 - Simple Login check on vwo.com Website.")
def test_vwologin_negative():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    
    email_input = driver.find_element(By.CSS_SELECTOR, "[name='username']")
    pass_input = driver.find_element(By.CSS_SELECTOR, "[name='password']")
    
    email_input.send_keys("admin@gmail.com")
    pass_input.send_keys("admin")
    
    button_submit_element = driver.find_element(By.ID, "js-login-btn")
    button_submit_element.click()
    
    
    # Fluent Wait ( EW)
    ignore_list = [ElementNotVisibleException, ElementNotSelectableException]
    
    wait = WebDriverWait(driver, timeout=60, poll_frequency=1, ignored_exceptions=ignore_list)
    wait.until(
        EC.visibility_of_element_located((By.ID, "js-notification-box-msg"))
    )
    
    # EW - Checking - t0,0,1,02,......5
    # EW - FW ,  t1, 2, 3, 4, 5
    

    
    error_msg_element = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_msg_element.text)
    assert error_msg_element.text == "Your email, password, IP address or location did not match"
    
    allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType.PNG)
    driver.quit()
