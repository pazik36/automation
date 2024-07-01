from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.execute_script("window.scrollTo(0, 100)")
    button1 = browser.find_element(By.ID, "book")

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element ((By.ID, "price"), "$100")
    )

    button1.click()

    x_element = browser.find_element(By.CSS_SELECTOR, "[id = input_value]")
    x = x_element.text

    result = calc(x)

    answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_input.send_keys(result)

    button2 = browser.find_element(By.ID, "solve")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()