from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
a1 = driver.find_element(By.NAME, 'q')
a1.send_keys('youtube')
b1 = driver.find_element(By.NAME, 'btnK')
b1.click()
c1 = driver.find_element(By.CLASS_NAME, 'LC20lb MBeuO DKV0Md')
c1.click()





