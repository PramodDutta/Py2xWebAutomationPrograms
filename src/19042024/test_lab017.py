import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# Selenium 4


# @pytest.mark.smoke
def test_vwologin_negative_tc():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    
    # driver.find_element(By.ID,"btn-make-appointment").click()
    
    # By. Link Text - Full Match or Exact match with the Text
    # rule 1 - first one, if there is not link text it will not able to find the element
    # a tag -> anchor tag
    #
    # <a
    # id="btn-make-appointment"
    # href="./profile.php#login"
    # class="btn btn-dark btn-lg">
    # Make Appointment
    # </a>
    
    # <a
    # id="btn-make-appointment"
    # href="./profile.php#login"
    # class="btn btn-dark btn-lg">
    # Make Appointment
    # </a>
    #
    # make_appoitnment_btn = driver.find_element(By.LINK_TEXT,"Make Appointment")
    # make_appoitnment_btn.click()
    
    
    
    # Partial Text
    # a anchor
    # partial match
    # PARTIAL_LINK_TEXT
    # Make Appointment
    # Appointment
    # Make
    # App
    # ment
    # Contains - keyword
    # Find the first unique element
    
    
    # make_appoitnment_btn = driver.find_element(By.PARTIAL_LINK_TEXT, "Appointment")
    # make_appoitnment_btn.click()
    
    
    
    # By TagName
    list_of_a_tags = driver.find_elements(By.TAG_NAME, "a")
    make_appoitnment_btn = list_of_a_tags[5]
    make_appoitnment_btn.click()
    
    # ID - Unique ID
    # name, Unique ClassName,
    # TagName - get 1, list of elements via findElements
    # Link/ partial - a anchor tags
    # Css Selector - 20%
    # XPath - 60%
    
    time.sleep(20)
    
    
    
    
    

    #assert error_msg_element.text == "Your email, password, IP address or location did not match"
    
    driver.quit()
