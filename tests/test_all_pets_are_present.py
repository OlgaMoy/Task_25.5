import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from settings import user_name


def test_all_pets_are_present(browser, go_to_my_pets):
    """Проверяем что на странице со списком моих питомцев присутствуют все питомцы"""
    assert browser.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    submit_button = WebDriverWait(pytest.driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'nav-link')))
    submit_button.click()

    assert browser.find_element(By.TAG_NAME, 'h2').text == user_name

    pet_info = browser.find_element(By.CSS_SELECTOR, 'div.left:nth-child(1)').text.split('\n')[1]
    number_of_pets = int("".join(filter(str.isdigit, pet_info)))
    print(number_of_pets)

    assert len(browser.find_elements(By.CSS_SELECTOR, 'tbody tr')) == number_of_pets