from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

def test_successful_registration():
    driver = webdriver.Chrome()
    
    try:
        driver.get("https://stellarburgers.nomoreparties.site/register")
        time.sleep(2)
        
        # Генерируем УНИКАЛЬНЫЙ email каждый раз
        random_num = random.randint(1000, 9999)  # Увеличиваем диапазон
        email = f"ilya_kartashev_{random_num}@yandex.ru"  # Меняем шаблон
        
        # Заполняем форму корректными данными
        all_inputs = driver.find_elements(By.TAG_NAME, "input")
        all_inputs[0].send_keys("Илья Карташев")
        all_inputs[1].send_keys(email)  # Используем уникальный email!
        all_inputs[2].send_keys("qwerty123")
        
        # Нажимаем кнопку регистрации
        driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
        time.sleep(3)
        
        # ПРОВЕРЯЕМ переход на логин
        current_url = driver.current_url
        assert "/login" in current_url, f"Ожидался переход на логин, но URL: {current_url}"
        
        print("Тест пройден: регистрация успешна")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_successful_registration()