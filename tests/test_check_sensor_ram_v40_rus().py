import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.pages.support_page import SupportPage
from framework.pages.industrial_cybersecurity_page import IndustrialCybersecurityPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_check_sensor_ram_v40(browser):
    support_page = SupportPage(browser)
    industrial_cybersecurity_page = IndustrialCybersecurityPage(browser)

    # Открываем https://support.kaspersky.com/help/
    support_page.open_url("https://support.kaspersky.com/help/")

    # Находим на странице Industrial CyberSecurity for Networks
    element_industrial = support_page.find_element_by_text("Industrial CyberSecurity for Networks")
    element_industrial.click()

    # Открываем версию 4.0
    element_version_4_0 = support_page.find_element_by_text("4.0")
    element_version_4_0.click()

    # Находим селектор языка и выбираем русский
    language_selector_locator = (By.CLASS_NAME, 'js_header_lang_list')  # Измененный класс селектора
    language_selector = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(language_selector_locator)
    )
    language_selector.click()

    # Выбираем русский язык
    russian_language_locator = (By.CLASS_NAME, 'dropdown__link.js_lang_item')
    russian_language_option = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(russian_language_locator)
    )
    russian_language_option.click()

    # Открываем "Аппаратные и программные требования"
    element_hardware_requirements = industrial_cybersecurity_page.find_element_by_text("Аппаратные и программные требования")
    element_hardware_requirements.click()

    # Находим текст "объем оперативной памяти: 8 ГБ и по 2 ГБ для каждой точки мониторинга на этом компьютере;"
    expected_text = "объем оперативной памяти: 8 ГБ и по 2 ГБ для каждой точки мониторинга на этом компьютере;"
    actual_text = industrial_cybersecurity_page.find_element_by_text(expected_text).text

    # Assert текст соответствует ожидаемому тексту
    assert actual_text == expected_text
