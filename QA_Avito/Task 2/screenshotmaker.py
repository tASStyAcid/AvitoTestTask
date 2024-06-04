from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация драйвера (например, Chrome)
driver = webdriver.Chrome()

# Загрузка веб-страницы
driver.get("https://www.avito.ru/avito-care/eco-impact")

# Найдите элемент (например, по ID)
element = driver.find_element(By.ID, "block-id")

# Сделайте скриншот элемента
element.screenshot("block_screenshot.png")

# Закрыть драйвер
driver.quit()