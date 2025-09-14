from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_via_forgot_password():
    """Тест проверяет переход на страницу логина со страницы восстановления пароля.
    
    Шаги:
    1. Открыть страницу восстановления пароля
    2. Нажать ссылку 'Войти' под формой
    3. Проверить переход на страницу логина
    
    Ожидаемый результат:
    - URL содержит '/login'
    """
    driver = webdriver.Chrome()
    
    try:
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        time.sleep(2)
        
        # Нажимаем ссылку "Войти"
        login_link = driver.find_element(By.XPATH, "//a[text()='Войти']")
        login_link.click()
        time.sleep(2)
        
        # Проверяем переход на страницу логина
        assert "/login" in driver.current_url
        
        print("Тест пройден: переход на логин со страницы восстановления пароля работает")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login_via_forgot_password()