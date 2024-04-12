from selenium import webdriver
import time
import pytest
# Selenium 4
import logging


# @pytest.mark.smoke
def test_open_vwologin():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome() # POST request | Create the Session
    driver.get("https://app.vwo.com") # GET Request to URL param
    print(driver.title)
    LOGGER.info(driver.title)
    assert driver.title == "Login - VWO"
    
    
    