from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
website = driver.get("https://www.youtube.com/")
driver.maximize_window()
a1 = website.find_element(By.ID, 'search')
a1.send_keys('123456789')

#print(dir(webdriver))
#print(help(webdriver


