import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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

    # Открываем "About Kaspersky Industrial CyberSecurity for Networks" с использованием JavaScript
    element_about = industrial_cybersecurity_page.find_element_by_text("About Kaspersky Industrial CyberSecurity for Networks")
    browser.execute_script("arguments[0].click();", element_about)

    # Открываем "Hardware and software requirements"
    element_hardware_requirements = industrial_cybersecurity_page.find_element_by_text("Hardware and software requirements")
    element_hardware_requirements.click()

    # Находим текст "RAM: 8 GB, and an additional 2 GB for each monitoring point on this computer"
    expected_text = "RAM: 8 GB, and an additional 2 GB for each monitoring point on this computer"
    actual_text = industrial_cybersecurity_page.find_element_by_text(expected_text).text

    # Assert текст соответствует ожидаемому тексту
    assert actual_text == expected_text