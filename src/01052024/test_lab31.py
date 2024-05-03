import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton


def test_01_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    
    # Click - Normal Driver will find the element and click on it, release it
    # Click and Hold -> Click -> and Hold, we will not release it.
    atag = driver.find_element(By.ID,"click")
    atag.click()
    
    
    
    # Actions Builders  = mouse go back
    
    actions_builder= ActionBuilder(driver)
    actions_builder.pointer_action.pointer_up(MouseButton.BACK)
    actions_builder.perform()
    
    
    
    
    time.sleep(10)
    driver.quit()