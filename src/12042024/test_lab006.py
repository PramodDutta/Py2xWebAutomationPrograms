from selenium import webdriver
import time
import pytest
# Selenium 4
import logging


# @pytest.mark.smoke
def test_open_vwologin():
    driver = webdriver.Chrome() # POST request | Create the Session
    driver.get("https://app.vwo.com") # GET Request to URL param
    print(driver.title)
    driver.maximize_window()
    assert driver.title == "Login - VWO"
    
    
    