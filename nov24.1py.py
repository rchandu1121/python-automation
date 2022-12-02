from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://demo.automationtesting.in/')
driver.maximize_window()
search_text = driver.find_element(By.ID, 'btn2')
search_text.click()
window = driver.find_element(By.CLASS_NAME, 'dropdown-toggle')
window.click()
window1 = driver.find_element(By.LINK_TEXT, 'Windows')
window1.click()
new = driver.find_element(By.LINK_TEXT, 'true')
new.click()
button = driver.find_element(By.CLASS_NAME, 'btn btn-info')
button.click()
















