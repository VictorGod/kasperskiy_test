# tests/test_support_page.py
import pytest
from selenium import webdriver
from framework.pages.support_page import SupportPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_support_page(browser):
    support_page = SupportPage(browser)
    support_page.open_url("https://support.kaspersky.com/help/")
    # Добавьте тестирование элементов на странице SupportPage
