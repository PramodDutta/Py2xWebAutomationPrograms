from selenium import webdriver
import time
import pytest
# Selenium 4
import logging


# @pytest.mark.smoke
def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://bing.com/chat")
    driver.back()
    driver.get("https://www.bing.com")
    print(driver.title)
    
    driver.forward()
    print(driver.title)
    
    driver.back()
    print(driver.title)
    driver.refresh()
    
    time.sleep(5)
    driver.quit()
    
    