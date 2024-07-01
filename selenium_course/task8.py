from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x ,y):
    return convertToInt(x) + convertToInt(y)

def convertToInt(parameter):
    return int(parameter)

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "[id = num1]")
    x = x_element.text

    print("x => ", x)

    y_element = browser.find_element(By.CSS_SELECTOR, "[id = num2]")
    y = y_element.text

    print("y => ", y)
    result = calc(x, y)

    print("result => ", result)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(result))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()





finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()