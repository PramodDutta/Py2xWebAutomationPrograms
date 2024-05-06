import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.common.exceptions import *


def test_expcetion():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    try:
        textarea = driver.find_element(By.NAME,"q")
        # textarea
        driver.refresh()
        # DOM elements - refreshed
        # // Refresh, Navigate other Page, change in DOM elements (Ajax Calls) - VueJS, AngularJS
        # webdriver -> stale element exception
        
        
         # driver.switch_to.alert
        
        textarea = driver.find_element(By.NAME, "q")
        textarea.send_keys("the testing academy")
        # NoAlertPresentException
    except StaleElementReferenceException as see:
        print(see)
        
        
    
    
    
    time.sleep(10)
    driver.quit()
