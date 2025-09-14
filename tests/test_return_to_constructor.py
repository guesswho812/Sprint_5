from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_return_to_constructor_from_profile():
    """Тест проверяет переход из личного кабинета в конструктор через кнопку 'Конструктор'.
    
    Шаги:
    1. Авторизоваться и перейти в личный кабинет
    2. Нажать кнопку 'Конструктор' в шапке сайта
    3. Проверить возврат на главную страницу
    
    Ожидаемый результат:
    - URL главной страницы ('https://stellarburgers.nomoreparties.site/')
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
        
        # Возвращаемся в конструктор
        constructor_button = driver.find_element(By.XPATH, "//p[text()='Конструктор']")
        constructor_button.click()
        time.sleep(2)
        
        # Проверяем возврат на главную
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        
        print("Тест пройден: переход из ЛК в конструктор через кнопку работает")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_return_to_constructor_from_profile()