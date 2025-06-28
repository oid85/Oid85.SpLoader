from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    # Инициализация драйвера (например, Chrome)
    driver = webdriver.Chrome()

    driver.get("https://spvtomske.ru/site/loginAjax")
    login = driver.find_element(By.XPATH, "//input[@placeholder='Имя пользователя']")
    login.send_keys("olga-m")
    password = driver.find_element(By.XPATH, "//input[@placeholder='Пароль']")
    password.send_keys("2wSxDr5t")
    autorize = driver.find_element(By.XPATH, "//input[@value='Авторизоваться']")
    autorize.click()

    # Переход на страницу с формой загрузки файла
    driver.get("https://spvtomske.ru/org/catalog/ChangeImageModal/id/328069193/active/CatalogActive/")

    # Находим элемент <input type="file">
    file_input = driver.find_element(By.XPATH, "//input[@type='file']")

    # Указываем путь к файлу
    file_path = "d:\\temp\\img123.png"  # Замените на реальный путь
    file_input.send_keys(file_path)

    # (Опционально) Находим и кликаем по кнопке отправки формы
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    submit_button.click()
