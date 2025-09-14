from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_from_main_page():
    """Тест проверяет вход через кнопку 'Войти в аккаунт' на главной странице.
    
    Шаги:
    1. Открыть главную страницу
    2. Нажать кнопку 'Войти в аккаунт'
    3. Проверить переход на страницу логина
    
    Ожидаемый результат: 
    - URL содержит '/login'
    """
    driver = webdriver.Chrome()
    
    try:
        driver.get("https://stellarburgers.nomoreparties.site")
        time.sleep(2)
        
        # Находим кнопку "Войти в аккаунт" и кликаем
        login_button = driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']")
        login_button.click()
        time.sleep(2)
        
        # Проверяем что перешли на страницу логина
        current_url = driver.current_url
        assert "/login" in current_url
        
        print("Тест пройден: переход на страницу логина работает")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login_from_main_page()