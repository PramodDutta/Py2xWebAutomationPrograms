import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# Selenium 4


# @pytest.mark.smoke
def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    
    # <a
    # id="btn-make-appointment"
    # href="./profile.php#login"
    # class="btn btn-dark btn-lg"
    # >
    # Make Appointment
    # </a>
    
    # Find the element the anchor tag - button
    # Click on it
    
    # #1 - id, className, name, tagName, linkText and PartialLinkText.
    # #2 - css Selector, xpath(sure shot way to find the elements in the HTML)
    
    element = driver.find_element(By.ID, "btn-make-appointment")
    element.click()
    
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    
    driver.quit()
