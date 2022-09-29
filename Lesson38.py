import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os


driver = webdriver.Chrome()
driver.get('https://myshows.me/')
driver.maximize_window()
xpath_button_enter = '//div[@class="Login"]/div[@class="Login-container"]/div[@class="Login-user"]/div[contains(@class,"Login-login")]'

WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_button_enter)))
button_enter = driver.find_element('xpath', xpath_button_enter)
button_enter.click()

xpath_button_registration = '//div[@class="Login-alter"]/a[@href="/registration/"]'

WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_button_registration)))
button_registration = driver.find_element('xpath', xpath_button_registration)
button_registration.click()

nickname = 'qwerkvfvds'
xpath_nickname = '//form/div[@class="FormField"]/div/input[@class="FormField-input"]'
#//form/div[@class="FormField"]/label[contains(text(),"Имя пользователя")]/following::div/input[@class="FormField-input"]
WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_nickname)))
field_nickname = driver.find_element('xpath', xpath_nickname)
field_nickname.send_keys(nickname)

email = 'TestTestgrgregergergergeeerg@gmail.com'
xpath_email = '//form/div[@class="FormField"]/div/input[@class="FormField-input"][@type="email"]'
#//form/div[@class="FormField"]/label[contains(text(),"Имя пользователя")]/following::div/input[@class="FormField-input"]
WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_email)))
field_email = driver.find_element('xpath', xpath_email)
field_email.send_keys(email)

password = 'TestTestgrgregergergergeeerg1'
xpath_password = '//form/div[@class="FormField"]/div/input[@class="FormField-input"][@type="password"]'
#//form/div[@class="FormField"]/label[contains(text(),"Имя пользователя")]/following::div/input[@class="FormField-input"]
WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_password)))
field_password = driver.find_element('xpath', xpath_password)
field_password.send_keys(password)

password1 = 'TestTestgrgregergergergeeerg1'
xpath_password1 = '//form/div[@class="FormField"]/div/input[@class="FormField-input"][@type="password"]/following::input[@class="FormField-input"][@type="password"]'
#//form/div[@class="FormField"]/label[contains(text(),"Имя пользователя")]/following::div/input[@class="FormField-input"]
WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_password1)))
field_password1 = driver.find_element('xpath', xpath_password1)
field_password1.send_keys(password1)



xpath_button_enter = '//button[contains(@class,"RoundedButton")]'

WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_button_enter)))
button_enter = driver.find_element('xpath', xpath_button_enter)
button_enter.click()