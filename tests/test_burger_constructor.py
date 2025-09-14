from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_burger_construction_and_order():
    """Тест проверяет полный цикл: сборка бургера через перетаскивание и оформление заказа.
    
    Шаги:
    1. Авторизоваться в системе
    2. Перетащить ингредиент в конструктор
    3. Нажать кнопку 'Оформить заказ'
    4. Проверить появление модального окна с подтверждением заказа
    
    Ожидаемый результат:
    - Появление модального окна с текстом о начале приготовления заказа
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
        
        # Переходим в конструктор
        driver.get("https://stellarburgers.nomoreparties.site")
        time.sleep(2)
        
        # Перетаскиваем ингредиент
        ingredient = driver.find_element(By.XPATH, "//div[contains(@class, 'BurgerIngredient_ingredient__')]")
        constructor_area = driver.find_element(By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket__')]")
        
        actions = ActionChains(driver)
        actions.drag_and_drop(ingredient, constructor_area).perform()
        time.sleep(2)
        
        # Нажимаем "Оформить заказ"
        order_button = driver.find_element(By.XPATH, "//button[text()='Оформить заказ']")
        order_button.click()
        time.sleep(5)
        
        # Проверяем успешное оформление заказа
        modals = driver.find_elements(By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
        orbit_text = driver.find_elements(By.XPATH, "//*[contains(text(), 'орбитальной станции')]")
        
        assert len(modals) > 0 or len(orbit_text) > 0, "Признаки успешного заказа не найдены"
        
        print("Тест пройден: бургер собран и заказ оформлен!")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_burger_construction_and_order()