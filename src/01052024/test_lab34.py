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
    # Windows,  # Web Tables - Self PACED. - Done
    
    # Problem statement of app.vo.com - iframe, windows, actions
    # Alerts, JS Executor, Shadow Dom, Relative Locators( Selenium 4)

    # --headless - EdgeOptions or ChromeOptions -
    # Pom, PF
    
    # Framework  -> BDD(behave) - Exception
    
    
    
    
    
    
    

    
    time.sleep(10)
    driver.quit()