from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/classattr")
    # Находим кнопку по CSS-классу
    button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    # Кликаем по кнопке
    button.click()
    # Немного задержки для наблюдения
    time.sleep(1)
finally:
    driver.quit()
    
