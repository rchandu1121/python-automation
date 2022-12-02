from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('https://demo.automationtesting.in/')
driver.maximize_window()
search_text = driver.find_element(By.ID, 'btn2')
search_text.click()
widgets = driver.find_element(By.LINK_TEXT, 'Widgets')
widgets.click()
sliders = driver.find_element(By.LINK_TEXT, 'Slider')
sliders.click()
slider = driver.find_element(By.ID, 'slider')
slider.click()
slider.click()
slider.click()




