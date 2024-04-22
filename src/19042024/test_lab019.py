import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType


# Selenium 4

@pytest.mark.smoke
@allure.title("Verify that Login is working in app.vwo.com website")
@allure.description("TC#1 - Simple Login check on vwo.com Website.")
def test_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    
    
    # <input
    # type="email"
    # class="text-input W(800%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi"
    # >
    
    # XPath
    
    #  //input[@id='login-username']
    #  //input[@name="username"]
    #  //input[@class="text-input W(800%)"] - Not Recom.
    #  //input[@type="email"] - Not Recom.
    #  //input[@data-qa="hocewoqisi"] - Custom A
    
    
    
    
    
    make_appoitnment_btn = driver.find_element(By.XPATH, "//input[@name='username']")
    make_appoitnment_btn.send_keys("admin")
    
    allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType.PNG)
    
   
    driver.quit()
