from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/inputs")
    # Находим поле ввода
    input_field = driver.find_element(By.TAG_NAME, "input")
    # Вводим "Sky"
    input_field.send_keys("Sky")
    time.sleep(0.5)
    # Очищаем поле
    input_field.clear()
    time.sleep(0.5)
    # Вводим "Pro"
    input_field.send_keys("Pro")
    time.sleep(1)
finally:
    driver.quit()
