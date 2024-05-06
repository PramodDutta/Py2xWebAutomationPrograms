import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.common.exceptions import *


def test_expcetion():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    try:
        driver.find_element(By.NAME,"pramod").send_keys("the testing academy")
    except NoSuchElementException as nse:
        print(f"No Such a element found, check locator:  {nse}")
    
    time.sleep(10)
    driver.quit()
