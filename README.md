Чеклист для самопроверки

Неявные ожидания:
Убедитесь, что в тесте проверки карточек питомцев установлены неявные ожидания:
driver.implicitly_wait(10)

Явные ожидания:
Убедитесь, что в тесте проверки таблицы питомцев используются явные ожидания с помощью WebDriverWait:
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.some-selector')))
