from selenium import webdriver
import time

driver = webdriver.Chrome('https://github.com/sugandhgithub/sample-repo-1/tree/master/drivers/chromedriver')
driver.get('https://www.google.com')
driver.maximize_window()
time.sleep(5)
driver.quit()


