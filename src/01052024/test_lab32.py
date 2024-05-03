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
    driver.get("https://www.makemytrip.com/")
    # Find the element -> move to the element -> send keys
    driver.maximize_window()
    
    time.sleep(10)
    
    # WebDriverWait(driver=driver, timeout=5).until(
    #     EC.visibility_of_element_located((By.XPATH, "//i[@class='wewidgeticon we_close']"))
    # )
    
    #driver.find_element(By.XPATH,"//i[@class='wewidgeticon we_close']").click()
    
    # Javascript executor
    # Keys. Escape
    
    
    # Wait Web driver, present click on it
    fromCity = driver.find_element(By.ID, "fromCity")
    actions = ActionChains(driver)
    actions.move_to_element(fromCity).send_keys("New Delhi").perform()
    actions.drag_and_drop_by_offset()
    
    
    
    
    
    time.sleep(10)
    driver.quit()