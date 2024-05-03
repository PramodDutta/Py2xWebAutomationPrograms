import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_01_actions():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.maximize_window()
    # Windows
    parent_window = driver.current_window_handle
    
    print(parent_window)
    
    link = driver.find_element(By.LINK_TEXT, "Click Here")
    link.click()
    
    window_handles = driver.window_handles # 2
    print(window_handles)
    
    
    for handle in window_handles:
        driver.switch_to.window(handle) # child
        if "New Window" in driver.page_source:
            print("Testcase Passed, Switched to Child Window")
            break
            
    time.sleep(3)
    driver.switch_to.window(parent_window)
    
    
    
    
    
    
    

    
    time.sleep(10)
    driver.quit()