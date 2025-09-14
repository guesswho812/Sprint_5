from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_logout_from_profile():
    """Тест проверяет выход из аккаунта через кнопку 'Выйти' в личном кабинете.
    
    Шаги:
    1. Авторизоваться и перейти в личный кабинет
    2. Нажать кнопку 'Выйти'
    3. Проверить переход на страницу логина
    
    Ожидаемый результат:
    - URL содержит '/login'
    """
    driver = webdriver.Chrome()
    
    try:
        # Логинимся и переходим в ЛК
        driver.get("https://stellarburgers.nomoreparties.site/login")
        time.sleep(2)
        
        all_inputs = driver.find_elements(By.TAG_NAME, "input")
        all_inputs[0].send_keys("test_killa@mail.ru")
        all_inputs[1].send_keys("qwerty123")
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        time.sleep(3)
        
        # Переходим в личный кабинет
        driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
        time.sleep(2)
        
        # Нажимаем кнопку "Выйти"
        logout_button = driver.find_element(By.XPATH, "//button[text()='Выход']")
        logout_button.click()
        time.sleep(2)
        
        # Проверяем выход (переход на логин)
        assert "/login" in driver.current_url
        
        print("Тест пройден: выход из аккаунта работает корректно")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_logout_from_profile()