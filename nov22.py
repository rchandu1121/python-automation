from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

# import Alert
from selenium.webdriver.common.alert import Alert



driver = webdriver.Chrome()
driver.get('https://demo.automationtesting.in/')
driver.maximize_window()
search_text = driver.find_element(By.ID, 'btn2')
search_text.click()
search_text = driver.find_element(By.CLASS_NAME, 'dropdown-toggle')
search_text.click()
alert_box = driver.find_element(By.LINK_TEXT, 'Alerts')
alert_box.click()
button = driver.find_element(By.XPATH, '//*[@id="OKTab"]/button')
button.click()
al = Alert(driver).accept()
#hover.perform()


