from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://demo.automationtesting.in/')
driver.maximize_window()
search_text = driver.find_element(By.ID, 'btn2')
search_text.click()
frames = driver.find_element(By.CLASS_NAME, 'dropdown-toggle')
frames.click()
frames1 = driver.find_element(By.LINK_TEXT, 'Frames')
frames1.click()
add = driver.find_element(By.ID, 'dismiss-button')
add.click()

#iframes = driver.find_element(By.XPATH, '/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[1]/a')
iframes1 = driver.find_element(By.XPATH, '/html/body/section/div/div/div/input')
iframes1.send_keys('123c')
#iframes1.click()












