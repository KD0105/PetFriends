from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация WebDriver
driver = webdriver.Chrome()

# Открытие страницы
driver.get("https://petfriends.skillfactory.ru/all_pets")

# Установка явных ожиданий
wait = WebDriverWait(driver, 10)

# Ожидание, пока таблица с питомцами станет доступной
table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover')))

# Ожидание, пока все строки таблицы станут видимыми
rows = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))

# Убедитесь, что таблица и строки таблицы были найдены
assert table is not None, "Таблица питомцев не найдена"
assert len(rows) > 0, "Строки таблицы питомцев не найдены"

# Закрытие WebDriver
driver.quit()
