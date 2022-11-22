from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('https://naukri.com/')
driver.maximize_window()
search_text = driver.find_element(By.CLASS_NAME, 'suggestor-input ')
search_text.send_keys('automation testing/cognizant')
#a1.click()
#a2 = driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div[2]/div[1]/div/div/div[3]/div/div/span')
#a2.click()
b1 = driver.find_element(By.ID, 'expereinceDD')
b1.send_keys('3 years')
b1.click()
c1 = driver.find_element(By.XPATH, '//*[@id="root"]/div[6]/div/div/div[5]/div/div/div/input')
c1.send_keys('hyderabad')
#c1.click()
d1 = driver.find_element(By.CLASS_NAME, 'qsbSubmit')
d1.click()
abc= Select(driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[7]/div/multi-select/div[2]/ul/li[7]/a'))
abc.select_by_visible_text('Oracle')
abc.select_by_index(0)