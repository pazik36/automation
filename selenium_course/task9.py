from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x ,y):
    return convertToInt(x) + convertToInt(y)

def convertToInt(parameter):
    return int(parameter)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "[id = input_value]")
    x = x_element.text

    print("x => ", x)

    y = calc(x)

    answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_input.send_keys(y)

    browser.execute_script("window.scrollTo(0, 100)")

    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robot_checkbox.click()

    robots_rule_radio_button = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    robots_rule_radio_button.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()