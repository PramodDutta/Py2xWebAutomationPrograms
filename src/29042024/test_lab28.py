import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By



@pytest.mark.smoke
@allure.title("Verify that Login is working in app.vwo.com website")
@allure.description("TC#1 - Simple Login check on vwo.com Website.")
def test_vwologin_negative():
    driver = webdriver.Chrome()
    driver.get("https://flipkart.com")
    driver.maximize_window()
    search_input = driver.find_element(By.NAME,"q")
    #search_input = driver.find_element(By.XPATH,"//input[@name='q']")
    search_input.send_keys("AC")
    
    svg_list = driver.find_elements(By.XPATH,"//*[name()='svg']")
    svg_list[0].click()
    
    time.sleep(5)
    
    
    
    allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType.PNG)
    driver.quit()
