import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def test_photo_availability(browser, go_to_my_pets):
   '''Поверяем что на странице со списком моих питомцев хотя бы у половины питомцев есть фото'''

   # Нажимаем на кнопку Мои питомцы
   submit_button = WebDriverWait(browser, 10).until(
      EC.element_to_be_clickable((By.CLASS_NAME, 'nav-link')))
   submit_button.click()

   # Сохраняем в переменную images элементы с атрибутом img
   images = browser.find_elements(By.CSS_SELECTOR, 'tr th[scope=row] img')

   # Сохраняем в переменную names количество питомцев
   names = browser.find_elements(By.CSS_SELECTOR, 'td:nth-child(2)')
   count_names = len(names)

   name_list = []
   num_photos_pets = 0

   # Находим количество питомцев с фотографией
   for i in range(count_names):
      assert names[i].text != ''
      name_list.append(names[i].text)
      if images[i].get_attribute('src'):
         num_photos_pets += 1

   assert count_names / 2 <= float(num_photos_pets)