from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

def test_successful_registration():
    """Тест проверяет успешную регистрацию с валидными данными.
    
    Для регистрации используется уникальный email по формату: 
    имя_фамилия_номеркогорты_3цифры@домен (требование задания)
    Это гарантирует, что каждый запуск теста создает нового пользователя.
    """
    driver = webdriver.Chrome()
    
    try:
        driver.get("https://stellarburgers.nomoreparties.site/register")
        time.sleep(2)
        
        # Генерируем уникальный email по формату из задания
        random_num = random.randint(1000, 9999)
        email = f"ilya_kartashev_99_{random_num}@yandex.ru"
        
        # Заполняем форму корректными данными
        all_inputs = driver.find_elements(By.TAG_NAME, "input")
        all_inputs[0].send_keys("Илья Карташев")
        all_inputs[1].send_keys(email)  # Уникальный email
        all_inputs[2].send_keys("qwerty123")  # Пароль >6 символов
        
        # Нажимаем кнопку регистрации
        driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
        time.sleep(3)
        
        # Проверяем переход на страницу логина после успешной регистрации
        current_url = driver.current_url
        assert "/login" in current_url, f"Ожидался переход на логин, но URL: {current_url}"
        
        print(f"Тест пройден: регистрация {email} успешна")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_successful_registration()