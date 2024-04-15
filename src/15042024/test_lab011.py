from selenium import webdriver
import time
import pytest
# Selenium 4
import logging


# @pytest.mark.smoke
def test_open_vwologin():
    driver = webdriver.Chrome() # POST request | Create the Session
    # Session is created - Unique ID - 16 digit ID
    # 64avbdas6a6d89as9a7 - Session?
    # webdriver.Chomre() - fresh copy of browser is created
    # open new tabs, open url, those will be different from the
    # normal browser. - Automation.
    # everything is deleted.
    

    driver.get("https://app.vwo.com") # GET Request to URL param
    print(driver.title)
    # print(driver.page_source)
    print(driver.session_id)
    driver.maximize_window()
    assert driver.title == "Login - VWO"
    
    time.sleep(10)
    driver.quit() # 80%
    # Close all the windows or tabs
    # session id == null( Invalid)
    # It will all close the other tabs.
    time.sleep(10)
    
    
    