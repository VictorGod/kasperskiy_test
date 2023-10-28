from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SupportPage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_by_class_name(self, class_name, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.CLASS_NAME, class_name))
        )
    
    def open_version_dropdown(self):
        version_dropdown = self.find_element_by_class_name("js_dropdown_btn")
        version_dropdown.click()

    def open_url(self, url):
        self.driver.get(url)

    def find_element_by_text(self, text):
        locator = (By.XPATH, f"//*[contains(text(), '{text}')]")
        return self.wait_for_element(locator)

    def click_element(self, element):
        if element:
            element.click()
            self.driver.implicitly_wait(5)

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
