from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, "input.first[required]")
    last_name = browser.find_element(By.CSS_SELECTOR, "input.second[required]")
    email = browser.find_element(By.CSS_SELECTOR, "input.third[required]")
    phone = browser.find_element(By.CSS_SELECTOR, "input.first[placeholder='Input your phone:']")
    address = browser.find_element(By.CSS_SELECTOR, "input.second[placeholder='Input your address:']")

    # Fill the required fields
    first_name.send_keys("Мой ответ")
    last_name.send_keys("Мой ответ")
    email.send_keys("Мой ответ")

    # Fill the optional fields
    phone.send_keys("Мой ответ")
    address.send_keys("Мой ответ")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()