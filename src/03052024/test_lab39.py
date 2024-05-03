import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_practice():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/analyze/osa/13/heatmaps/1?token=eyJhY2NvdW50X2lkIjo2NjY0MDAsImV4cGVyaW1lbnRfaWQiOjEzLCJjcmVhdGVkX29uIjoxNjcxMjA1MDUwLCJ0eXBlIjoiY2FtcGFpZ24iLCJ2ZXJzaW9uIjoxLCJoYXNoIjoiY2IwNzBiYTc5MDM1MDI2N2QxNTM5MTBhZDE1MGU1YTUiLCJzY29wZSI6IiIsImZybiI6ZmFsc2V9&isHttpsOnly=1")
    main_window_handle = driver.current_window_handle
    print("Before Click " + main_window_handle)
    
    actions = ActionChains(driver)
    list = driver.find_elements(By.CSS_SELECTOR,"[data-qa='yedexafobi']")
    #control = list[0]
    variation = list[1]
    
    actions.click(variation).perform()
    
    time.sleep(15)
    
    
    # Switch to the Chid window
    all_handles = driver.window_handles #2
    for handle in all_handles:
        if handle!=main_window_handle:
            driver.switch_to.window(handle)
            print(driver.title) #switch to child window
            driver.switch_to.frame("heatmap-iframe")
            clickmap = driver.find_element(By.CSS_SELECTOR,"[data-qa='liqokuxuba']")
            clickmap.click()
            time.sleep(20)
            
            
    
    
    
    
    
    time.sleep(10)
    driver.quit()



