import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# Selenium 4


# @pytest.mark.smoke
def test_vwologin_negative_tc():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    
    # id -> name -> className -> tagName -> LinkText, PartialText -> css Selector -> Xpath
    
    # <input
    # type="email"
    # class="text-input W(100%)"
    # name="username"
    # data-qa="hocewoqisi"
    # >
    
    email_element = driver.find_element(By.NAME,"username")
    email_element.send_keys("admin")
    
    
    # <input
    # type="password"
    # class="text-input W(100%)"
    # name="password"
    # id="login-password"
    # data-qa="jobodapuxe">
    
    password_element = driver.find_element(By.ID, "login-password")
    password_element.send_keys("admin")
    
    button_submit_element = driver.find_element(By.ID,"js-login-btn")
    button_submit_element.click()
    
    time.sleep(5)
    
    error_msg_element = driver.find_element(By.ID,"js-notification-box-msg")
    print(error_msg_element.text)
    assert error_msg_element.text == "Your email, password, IP address or location did not match"
    
    driver.quit()
