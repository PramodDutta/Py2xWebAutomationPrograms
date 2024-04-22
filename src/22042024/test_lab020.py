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
    
    # //*[@id='btn-make-WQass12132'] - 1 - Fast?
    # //*[@id='btn-make-appointment'] - This is called * wild card ,
    # Find id = btn-make-app in All the TagNames, this will be a Slow xpath
    # //a[@id='btn-make-WQass12132'] - 2
    
    
    # // Find * where id = btn----
    
    make_app_btn = driver.find_element(By.XPATH,"//a[text()='Make Appointment']")
    # text() -> Exact Match
    
    # Partial Text() - contains()
    # //a[contains(text(),'Make Appointment')]
    # //a[contains(text(),'Appointment')]
    # //a[contains(text(),'Make')]
    # //a[contains(text(),'Ma')]
    # //a[contains(text(),'App')] - This may fail if there 1 or more a tag with App.
    # <a rel="https:/google.com"/>
    
    # //a[starts-with(text(),'Make')]
    
    # # -> id
    make_btn_css = driver.find_element(By.CSS_SELECTOR,"#btn-make-appointment")
    make_btn_css_list = driver.find_elements(By.CSS_SELECTOR,".btn.btn-dark.btn-lg")
    
    # //header[@id='top']/div -> header#top > div
    
    #Xpath
    
    
    allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType.PNG)
    
   
    driver.quit()
