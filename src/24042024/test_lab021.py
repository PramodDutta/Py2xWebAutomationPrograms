import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By


# Selenium 4 - TC

@pytest.mark.smoke
@allure.title("Verify that Login is working in app.vwo.com website")
@allure.description("TC#1 - Simple Login check on vwo.com Website.")
def test_vwologin_negative():
    driver = webdriver.Chrome()
    # driver.implicitly_wait(5) - Webdriver to wait for all the elements
    # time.sleep(5) - time.sleep(15) #-> Thread.sleep() , Python Int  wait.
    driver.get("https://app.vwo.com")
    
    # e1, e2 , e3 ->
    # Tell Webdriver to wait for the 5 to Load
    # All the elements.
    # What if the e1,e2,e3 < 3, then 2 wasted.
    
    
    email_input = driver.find_element(By.CSS_SELECTOR, "[name='username']")
    pass_input = driver.find_element(By.CSS_SELECTOR, "[name='password']")
    
    email_input.send_keys("admin@gmail.com")
    pass_input.send_keys("admin")
    
    button_submit_element = driver.find_element(By.ID, "js-login-btn")
    button_submit_element.click()
    
    # Python - Int - It is super bad practice - time.sleep(5) - Worst type of Wait.
    # Webdriver
    
    time.sleep(5) # This is Python Int who is waiting, Python Execution Halt.
    
    error_msg_element = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_msg_element.text)
    assert error_msg_element.text == "Your email, password, IP address or location did not match"
    
    allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType.PNG)
    driver.quit()
