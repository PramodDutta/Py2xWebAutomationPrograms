import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_01_dragdrop():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")
    
    
    actions = ActionChains(driver)
    from_element = driver.find_element(By.ID,"column-a")
    to_element = driver.find_element(By.ID,"column-b")
    
    (actions
     .click_and_hold(from_element)
     .move_to_element(to_element)
     .release(to_element)
     .perform()) # firefox, edge, chrome , opera, IE
    
    
    
    #actions.drag_and_drop(from_element,to_element)
    
    
    
    time.sleep(10)
    driver.quit()
    
    
    