import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_01_JS1():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    # Javascript executor
    button = driver.find_element(By.XPATH, "//button[@onclick='addElement()']")
    # button.click()
    
    # Use the Javascript code to click on this button also
    js_ex = driver.execute_script
    js_ex("arguments[0].click()",button)
    js_ex("arguments[0].click()",button)
    
    time.sleep(10)
    driver.quit()



