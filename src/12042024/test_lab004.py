from selenium import webdriver
import time

# Selenium 4


def test_open_vwologin():
    driver = webdriver.Chrome() # POST request | Create the Session
    driver.get("https://app.vwo.com") # GET Request to URL param
    time.sleep(5)
    
    