import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, WebDriverException
from framework.pages.support_page import SupportPage
from framework.pages.industrial_cybersecurity_page import IndustrialCybersecurityPage

def find_stale_element(driver, by, value):
    attempts = 0
    while attempts < 3:
        try:
            return driver.find_element(by, value)
        except StaleElementReferenceException:
            attempts += 1
    raise StaleElementReferenceException("Element could not be located, too many attempts.")

def find_version_element(driver, card_url, version_text):
    version_locator = (By.XPATH, f'//div[@data-url="{card_url}"]//a[contains(@class, "dropdown__link") and contains(@class, "js_version_item") and contains(text(), "{version_text}")]')
    return WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(version_locator)
    )

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_check_sensor_ram_v30(browser):
    support_page = SupportPage(browser)
    industrial_cybersecurity_page = IndustrialCybersecurityPage(browser)

    # Открываем https://support.kaspersky.com/help/
    support_page.open_url("https://support.kaspersky.com/help/")

    # Находим карточку с data-url="/KICSforNetworks/4.0/en-US"
    card_locator = (By.CSS_SELECTOR, '[data-url="/KICSforNetworks/4.0/en-US"]')
    card_element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(card_locator)
    )
    card_url = card_element.get_attribute("data-url")

    # Открываем стрелочку для выбора версии внутри карточки
    arrow_icon = find_stale_element(card_element, By.CLASS_NAME, "product__version")
    arrow_icon.click()

    # Находим и кликаем на версию 3.0 в меню выбора
    version_3_0_locator = (By.XPATH, f'//div[@data-url="{card_url}"]//a[contains(@class, "dropdown__link") and contains(@class, "js_version_item") and contains(text(), "3.0")]')

    try:
        version_3_0_element = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(version_3_0_locator)
        )
    except WebDriverException as e:
        if "no such execution context" in str(e):
            # Если возникает ошибка, перейдем на страницу версии 3.0 заново
            support_page.open_url(f"https://support.kaspersky.com/{card_url}")
            # Повторим поиск элемента
            version_3_0_element = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable(version_3_0_locator)
            )
        else:
            raise  # Если это не ошибка "no such execution context", пробросим исключение дальше

    version_3_0_element.click()

    # Открываем "About Kaspersky Industrial CyberSecurity for Networks" с использованием JavaScript
    element_about = industrial_cybersecurity_page.find_element_by_text("About Kaspersky Industrial CyberSecurity for Networks")
    browser.execute_script("arguments[0].click();", element_about)

    # Открываем "Hardware and software requirements"
    element_hardware_requirements = industrial_cybersecurity_page.find_element_by_text("Hardware and software requirements")
    element_hardware_requirements.click()

    # Находим текст "RAM: 4 GB, and an additional 2 GB for each monitoring point on this computer"
    expected_text = "RAM: 4 GB, and an additional 2 GB for each monitoring point on this computer"
    actual_text = industrial_cybersecurity_page.find_element_by_text(expected_text).text

    # Assert текст соответствует ожидаемому тексту
    assert expected_text in actual_text
