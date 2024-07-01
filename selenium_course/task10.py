from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    fist_name_input = browser.find_element(By.CSS_SELECTOR, "[name = firstname]")
    fist_name_input.send_keys("Ivan")

    last_name_input = browser.find_element(By.CSS_SELECTOR, "[name = lastname]")
    last_name_input.send_keys("Ivanov")

    email_input = browser.find_element(By.CSS_SELECTOR, "[name = email]")
    email_input.send_keys("ivan@ivanov.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_example.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()