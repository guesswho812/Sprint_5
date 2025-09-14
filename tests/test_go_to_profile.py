from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_go_to_profile():
    """Тест проверяет переход в личный кабинет после авторизации.
    
    Шаги:
    1. Выполнить вход в систему
    2. Нажать кнопку 'Личный кабинет'
    3. Проверить переход в личный кабинет
    
    Ожидаемый результат:
    - URL содержит '/account/profile'
    """
    driver = webdriver.Chrome()
    
    try:
        # Логинимся
        driver.get("https://stellarburgers.nomoreparties.site/login")
        time.sleep(2)
        
        all_inputs = driver.find_elements(By.TAG_NAME, "input")
        all_inputs[0].send_keys("test_killa@mail.ru")
        all_inputs[1].send_keys("qwerty123")
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        time.sleep(3)
        
        # Переходим в личный кабинет
        profile_button = driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']")
        profile_button.click()
        time.sleep(2)
        
        # Проверяем переход в личный кабинет
        assert "/account/profile" in driver.current_url
        
        print("Тест пройден: переход в личный кабинет работает")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_go_to_profile()