from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IndustrialCybersecurityPage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_by_text(self, text):
        locator = (By.XPATH, f"//*[contains(text(), '{text}')]")
        return self.wait_for_element(locator)

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
