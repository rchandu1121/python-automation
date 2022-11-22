from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://practicetestautomation.com/')
driver.maximize_window()
a1 = driver.find_element(By.ID, 'menu-item-20')
a1.click()
b1 = driver.find_element(By.LINK_TEXT, 'Test Login Page')
b1.click()
c1 = driver.find_element(By.NAME, 'username')
c1.send_keys("student")
d1 = driver.find_element(By.ID, "password")
d1.send_keys("Password123")
e1 = driver.find_element(By.ID, 'submit')
e1.click()

if ('Logged In Successfully' in (driver.page_source)):
    print('yes')
else:
    print('no')

f1 = driver.find_element(By.LINK_TEXT, 'Log out')

f1.click()

