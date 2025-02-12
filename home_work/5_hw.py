#задание 1
from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.common.exceptions import NoSuchElementException

def search_elements():
    driver = webdriver.Chrome()
    try:
        driver.get('https://www.saucedemo.com/')

        # поиск элемента
        uname = driver.find_element(By.CSS_SELECTOR, 'form > div > input')
        pass_w = driver.find_element(By.CSS_SELECTOR, '#password')
        button = driver.find_element(By.CSS_SELECTOR, '#login-button')
        print('Элементы найдены')
    except NoSuchElementException:
        print('Элементы найдены')

search_elements()