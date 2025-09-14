from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_via_personal_account():
    """Тест проверяет вход через кнопку 'Личный кабинет' без авторизации.
    
    Шаги:
    1. Открыть главную страницу
    2. Нажать кнопку 'Личный кабинет'
    3. Проверить переход на страницу логина
    4. Выполнить вход с валидными данными
    5. Проверить переход на главную страницу
    
    Ожидаемый результат:
    - Успешный вход и переход на главную страницу
    """
    driver = webdriver.Chrome()
    
    try:
        driver.get("https://stellarburgers.nomoreparties.site")
        time.sleep(2)
        
        # Нажимаем кнопку "Личный кабинет"
        personal_account_button = driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']")
        personal_account_button.click()
        time.sleep(2)
        
        # Проверяем переход на страницу логина
        assert "/login" in driver.current_url
        
        # Выполняем вход
        all_inputs = driver.find_elements(By.TAG_NAME, "input")
        all_inputs[0].send_keys("test_killa@mail.ru")
        all_inputs[1].send_keys("qwerty123")
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        time.sleep(3)
        
        # Проверяем успешный вход
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        
        print("Тест пройден: вход через личный кабинет работает")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login_via_personal_account()