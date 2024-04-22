import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType


# Selenium 4

@pytest.mark.smoke
@allure.title("Verify that Login is working in Cura website")
@allure.description("TC#1 - Simple Login check on CURA katalong Website.")
def test_vwologin_negative_tc():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    
    make_appoitnment_btn = driver.find_element(By.LINK_TEXT, "Make Appointment")
    make_appoitnment_btn.click()
    
    allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType.PNG)
    
    print(driver.current_url)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login", "Assertion Fail Message #1 - Error Matching the URLs"
    
    username = driver.find_element(By.NAME,"username")
    username.send_keys("John Doe")
    
    password = driver.find_element(By.ID, "txt-password")
    password.send_keys("ThisIsNotAPassword")
    
    submit_btn = driver.find_element(By.ID, "btn-login")
    submit_btn.click()
    
    allure.attach(driver.get_screenshot_as_png(), name="appointment-screenshot", attachment_type=AttachmentType.PNG)
    
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment", "Assertion Fail Message #2 - Error wrong URL(appointment)"
    
    # // a[ @ id = 'btn-make-appointment'] - 1 unique elemnt
   
   
    driver.quit()
