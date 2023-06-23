import pytest
from settings import valid_email, valid_password, user_name
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_show_pet_friends(browser, go_to_my_pets):
   '''Проверка карточек питомцев'''

   # Устанавливаем неявное ожидание
   pytest.driver.implicitly_wait(10)

   # Нажимаем на кнопку Мои питомцы
   submit_button = WebDriverWait(browser, 10).until(
      EC.element_to_be_clickable((By.CLASS_NAME, 'nav-link')))
   submit_button.click()

   # Проверяем, что мы оказались на главной странице пользователя
   assert browser.find_element(By.TAG_NAME, 'h2').text == user_name

   images = browser.find_elements(By.CSS_SELECTOR, 'tr th[scope=row] img')
   names = browser.find_elements(By.CSS_SELECTOR, 'td:nth-child(2)')
   descriptions = browser.find_elements(By.CSS_SELECTOR, 'td:nth-child(3)')
   age = browser.find_elements(By.CSS_SELECTOR, 'td:nth-child(4)')
   print(names)

   num_photos_pets = 0
   count_names = len(names)
   name_list = []
   age_list = []
   descriptions_list = []

   for i in range(count_names):
      assert names[i].text != ''
      name_list.append(names[i].text)
      if images[i].get_attribute('src'):
         num_photos_pets += 1
      assert descriptions[i].text != ''
      descriptions_list.append(descriptions[i].text)
      assert age[i].text != ''
      age_list.append(age[i].text)
      assert 0 <= int(age[i].text) < 100
      assert 0 < len(names[i].text) < 255
      assert 0 < len(descriptions[i].text) < 255