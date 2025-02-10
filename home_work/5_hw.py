#задание 1
from selenium import webdriver
from selenium.webdriver.common.by import  By

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

#поиск элемента
uname = driver.find_element(By.CSS_SELECTOR, 'form > div > input')
pass_w = driver.find_element(By.CSS_SELECTOR, '#password')
button = driver.find_element(By.CSS_SELECTOR, '#login-button')

if uname and pass_w and button is None:
    print('Элементы не найдены')
else:
    print('Элементы найдены')