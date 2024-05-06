import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


def test_practice():
    driver = webdriver.Chrome()
    driver.get("https://www.aqi.in/real-time-most-polluted-city-ranking")
    driver.maximize_window()
    time.sleep(10)
    
    search_city = driver.find_element(By.ID, "search_city")
    search_city.send_keys("India")
    time.sleep(5)
    
    list_of_states = driver.find_elements(By.XPATH, "//table[@id='example']/tbody/tr/td[2]")
    print("Name" + " | " + "ACQ" + " | " + "Rank")
    for state in list_of_states:
        if "India" in state.text:
            s1 = driver.find_element(locate_with(By.TAG_NAME, "p").to_right_of(state)).text
            s2 = driver.find_element(locate_with(By.TAG_NAME, "p").to_left_of(state)).text
            s3 = driver.find_element(locate_with(By.TAG_NAME, "p").below(state)).text
            s4 = driver.find_element(locate_with(By.TAG_NAME, "p").above(state)).text
            print(state.text + " | " + s1 + " | " + s2)
            print(state.text + " | " + s3 + " | " + s4)
    

    driver.quit()
