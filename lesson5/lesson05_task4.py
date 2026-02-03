from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/login")
    # Ввод логина
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    # Ввод пароля
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    # Нажатие на кнопку входа
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    # Получение сообщения
    message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
    print(message.text)
    time.sleep(1)
finally:
    driver.quit()
