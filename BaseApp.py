from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://test-stand.gb.ru"

    def find_element(self, element, time=10, clear=False, alert=False):
        """
        Поиск элемента, если clear=True то после того как
        элемент будет найден - это поле очистится.
        """
        if alert:
            alert = WebDriverWait(self.driver, time).until(EC.alert_is_present(),
                                                           message=f"Can't find alert within {time} seconds")
            return alert

        res_element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(element),
                                                             message=f"Cant's find element by locator {element}")
        if clear:
            res_element.clear()
        return res_element

    def get_element_property(self, locator, property):
        """Поиск свойств элемента"""
        element = self.find_element(locator)
        return element.value_of_css_property(property)

    def go_to_site(self):
        """Открытие страницы"""
        return self.driver.get(self.base_url)

    def wait_for_url(self, old_url, time=5):
        return WebDriverWait(self.driver, time).until(EC.url_changes(old_url))
