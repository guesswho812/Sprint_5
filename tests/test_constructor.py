from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_constructor_sections():
    """Тест проверяет переключение между разделами конструктора: 'Булки', 'Соусы', 'Начинки'.
    
    Шаги:
    1. Открыть главную страницу
    2. Найти вкладки разделов
    3. Последовательно кликнуть на каждую вкладку
    4. Проверить активацию соответствующей вкладки
    
    Ожидаемый результат:
    - При клике на вкладку она становится активной
    - Отображается соответствующий раздел с ингредиентами
    """
    driver = webdriver.Chrome()
    
    try:
        driver.get("https://stellarburgers.nomoreparties.site")
        time.sleep(2)
        
        # Находим все вкладки
        buns_tab = driver.find_element(By.XPATH, "//span[text()='Булки']/..")
        sauces_tab = driver.find_element(By.XPATH, "//span[text()='Соусы']/..")
        fillings_tab = driver.find_element(By.XPATH, "//span[text()='Начинки']/..")
        
        # Кликаем на "Соусы"
        sauces_tab.click()
        time.sleep(1)
        
        # Проверяем активную вкладку
        active_tab = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
        assert "Соусы" in active_tab.text
        
        # Кликаем на "Начинки"
        fillings_tab.click()
        time.sleep(1)
        
        # Проверяем активную вкладку
        active_tab = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
        assert "Начинки" in active_tab.text
        
        # Кликаем на "Булки"
        buns_tab.click()
        time.sleep(1)
        
        # Проверяем активную вкладку
        active_tab = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
        assert "Булки" in active_tab.text
        
        print("Тест пройден: переключение между разделами конструктора работает")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_constructor_sections()