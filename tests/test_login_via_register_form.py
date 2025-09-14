from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_via_register_form():
    """Тест проверяет переход на страницу логина со страницы регистрации.
    
    Шаги:
    1. Открыть страницу регистрации
    2. Нажать ссылку 'Войти' под формой
    3. Проверить переход на страницу логина
    
    Ожидаемый результат:
    - URL содержит '/login'
    """
    driver = webdriver.Chrome()
    
    try:
        driver.get("https://stellarburgers.nomoreparties.site/register")
        time.sleep(2)
        
        # Нажимаем ссылку "Войти"
        login_link = driver.find_element(By.XPATH, "//a[text()='Войти']")
        login_link.click()
        time.sleep(2)
        
        # Проверяем переход на страницу логина
        assert "/login" in driver.current_url
        
        print("Тест пройден: переход на логин со страницы регистрации работает")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login_via_register_form()