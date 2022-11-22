from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.get('https://demo.automationtesting.in/')
driver.maximize_window()
search_text = driver.find_element(By.ID, 'btn2')
search_text.click()
search_text = driver.find_element(By.CSS_SELECTOR, '#basicBootstrapForm > div:nth-child(1) > div:nth-child(2) > input')
search_text.send_keys('chandu')
search_text = driver.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[1]/div[2]/input')
search_text.send_keys('rankireddy')
search_text = driver.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[2]/div/textarea')
search_text.send_keys('palakol near maruthi theatre andhra pradesh ')
search_text = driver.find_element(By.CSS_SELECTOR, '#eid > input')
search_text.send_keys('chandu.rankireddy1121@gmail.com')
search_text = driver.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[4]/div/input')
search_text.send_keys(7995952133)
search_text =driver.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[5]/div/label[1]/input')
search_text.click()
search_text = driver.find_element(By.ID, 'checkbox1')
search_text.click()
search_text = driver.find_element(By.ID, 'checkbox2')
search_text.click()
search_text = driver.find_element(By.XPATH, '//*[@id="msdd"]')
search_text.click()
search_text = driver.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[7]/div/multi-select/div[2]/ul/li[8]/a')
search_text.click()

skills = Select(driver.find_element(By.XPATH, '//*[@id="Skills"]'))
skills.select_by_visible_text('iPhone')

time.sleep(60)
driver.close()











