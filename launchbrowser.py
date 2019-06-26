from selenium import webdriver
import time

driver = webdriver.Chrome('/Users/neelamtawar/PycharmProjects/sample-repo-1/drivers/chromedriver')
driver.get('https://www.google.com')
driver.maximize_window()
time.sleep(5)
driver.quit()


