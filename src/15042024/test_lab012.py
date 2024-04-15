from selenium import webdriver
import time
import pytest
# Selenium 4
import logging


# @pytest.mark.smoke
def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://bing.com/chat")
    time.sleep(25) # Python Int.- wait for the 25 seconds, not the webdriver.
    driver.get("https://google.com")
    print(driver.title)
    
    