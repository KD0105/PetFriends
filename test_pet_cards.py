from selenium import webdriver

# Инициализация WebDriver
driver = webdriver.Chrome()

# Установка неявных ожиданий
driver.implicitly_wait(10)  # Ждать до 10 секунд для всех элементов

# Открытие страницы
driver.get("https://petfriends.skillfactory.ru/all_pets")

# Проверка наличия карточек питомцев
photos = driver.find_elements_by_css_selector('.pet-card-photo')
names = driver.find_elements_by_css_selector('.pet-card-name')
ages = driver.find_elements_by_css_selector('.pet-card-age')

# Убедитесь, что все элементы были найдены
assert len(photos) > 0, "Фото питомцев не найдены"
assert len(names) > 0, "Имена питомцев не найдены"
assert len(ages) > 0, "Возраст питомцев не найден"

# Закрытие WebDriver
driver.quit()
