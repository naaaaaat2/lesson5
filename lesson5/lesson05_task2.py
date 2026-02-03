from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/dynamicid")
    # Находим кнопку по CSS-селектору
    button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
    # Кликаем
    button.click()
    time.sleep(1)
finally:
    driver.quit()
