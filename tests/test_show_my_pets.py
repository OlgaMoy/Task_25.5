import pytest
from settings import valid_email, valid_password, user_name
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_show_my_pets(browser, go_to_my_pets):
   '''Проверяем что мы оказались на странице "Мои питомцы"'''

   # Нажимаем на кнопку Мои питомцы
   submit_button = WebDriverWait(pytest.driver, 10).until(
      EC.element_to_be_clickable((By.CLASS_NAME, 'nav-link')))
   submit_button.click()

   assert browser.find_element(By.TAG_NAME, 'h2').text == user_name