import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from settings import valid_email, valid_password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


@pytest.fixture(autouse=True)
def browser():
    driver = Service("pythonProject7-master/chromedriver/")
    pytest.driver = webdriver.Chrome(service=driver)

    # Переходим на страницу авторизации
    pytest.driver.get('https://petfriends.skillfactory.ru/login')
    pytest.driver.maximize_window()
    pytest.driver.implicitly_wait(10)
    yield pytest.driver
    pytest.driver.quit()


@pytest.fixture()
def go_to_my_pets():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)

    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)

    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()