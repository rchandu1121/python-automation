from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard

driver = webdriver.Chrome()
driver.maximize_window()

class Google:
    def url(self):
        driver.get('https://www.google.com/')

    def search_text(self):
        s = driver.find_element(By.CLASS_NAME, 'gLFyf')
        s.send_keys('twitter')

    def search_button(self):
        driver.find_element(By.CLASS_NAME, 'pcTkSc')
        keyboard.press_and_release('enter')