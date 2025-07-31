from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_ERROR_LABEL = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_HELLO_TEXT = (By.XPATH, """/html/body/div[1]/main/nav/ul/li[3]/a""")
    LOCATOR_TITLE_FIELD = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_DESCRIPTION_FIELD = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_CONTENT_FIELD = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_TITLE_POST = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_IN_BTN = (By.CSS_SELECTOR, """button""")
    LOCATOR_CREATE_BTN = (By.ID, """create-btn""")
    LOCATOR_SAVE_BTN = (By.XPATH, """//button[.//span[text()='Save']]""")
    LOCATOR_CONTACT_BTN = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_YOUR_NAME_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_YOUR_EMAIL_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_YOUR_CONTENT_FIELD = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")


class OperationHelper(BasePage):
    def enter_login(self, word):
        """Ищет поле для ввода логина, очищает его, вводит логин"""
        locator_login = TestSearchLocators.LOCATOR_LOGIN_FIELD
        logging.info(f"Send {word} to element {locator_login[1]}")
        login_field = self.find_element(locator_login, clear=True)
        login_field.send_keys(word)

    def enter_pass(self, word):
        """Ищет поле для ввода пароля, очищает его, вводит пароль"""
        locator_passwd = TestSearchLocators.LOCATOR_PASS_FIELD
        logging.info(f"Send {word} to element {locator_passwd[1]}")
        login_field = self.find_element(locator_passwd, clear=True)
        login_field.send_keys(word)

    def click_login_button(self):
        """Ищет кнопку LOGIN, нажимает на неё"""
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_IN_BTN).click()

    def get_error_text(self):
        """
        Ищет текст сообщения об ошибке, время ожидание загрузки элемента до 3сек.
        Возвращает текст элемента.
        """
        locator = TestSearchLocators.LOCATOR_ERROR_LABEL
        error_field = self.find_element(locator)
        text_err = error_field.text
        logging.info(f"We find text {text_err} in error field {locator[1]}")
        return text_err

    def get_label_text(self):
        """
        Ищет текст сообщения Hello, <name>, время ожидание загрузки элемента до 3сек.
        Возвращает текст элемента."""
        locator = TestSearchLocators.LOCATOR_HELLO_TEXT
        text_hello = self.find_element(locator)
        text_h = text_hello.text
        logging.info(f"We find text {text_h} in text hello label {locator[1]}")
        return text_h

    def click_create_new_post_btn(self):
        """Ищет кнопку create new post, нажимает на неё"""
        logging.info("Click create new post button")
        self.find_element(TestSearchLocators.LOCATOR_CREATE_BTN).click()

    def enter_title(self, word):
        """Ищет поле для ввода "Заголовок/Title", очищает его, вводит текст"""
        locator_in_t = TestSearchLocators.LOCATOR_TITLE_FIELD
        logging.info(f"Send {word} to element {locator_in_t[1]}")
        login_field = self.find_element(locator_in_t)
        login_field.send_keys(word)

    def enter_description(self, word):
        """Ищет поле для ввода "Описание/Description", очищает его, вводит текст"""
        locator_in_d = TestSearchLocators.LOCATOR_DESCRIPTION_FIELD
        logging.info(f"Send {word} to element {locator_in_d[1]}")
        login_field = self.find_element(locator_in_d)
        login_field.send_keys(word)

    def enter_content(self, word):
        """Ищет поле для ввода "Контент/Content", очищает его, вводит текст"""
        locator_in_c = TestSearchLocators.LOCATOR_CONTENT_FIELD
        logging.info(f"Send {word} to element {locator_in_c[1]}")
        login_field = self.find_element(locator_in_c)
        login_field.send_keys(word)

    def click_save_post_btn(self):
        """
        Ищет кнопку SAVE, сохраняет url в переменную, ожидает изменения url, записывает url после перехода.
        """
        self.find_element(TestSearchLocators.LOCATOR_SAVE_BTN).click()
        current_url = self.driver.current_url
        self.wait_for_url(current_url)
        new_url = self.driver.current_url
        logging.info(f"Routing {current_url} -> {new_url}")

    def get_title_post(self):
        """
        Ищет название добавленного поста title, время ожидание загрузки элемента до 3сек.
        Возвращает текст элемента.
        """
        locator_title_text = TestSearchLocators.LOCATOR_TITLE_POST
        text_title_post = self.find_element(locator_title_text)
        text_t = text_title_post.text
        logging.info(f"We find text {text_t} in title post field {locator_title_text[1]}")
        return text_t

    def click_contact_btn(self):
        """Ищет ссылку contact, нажимает на неё"""
        logging.info("Click contact button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()

    def enter_your_name(self, word):
        """Ищет поле для ввода "enter_your_name", очищает его, вводит текст"""
        locator_in_t = TestSearchLocators.LOCATOR_YOUR_NAME_FIELD
        logging.info(f"Send {word} to element {locator_in_t[1]}")
        login_field = self.find_element(locator_in_t)
        login_field.send_keys(word)

    def enter_your_email(self, word):
        """Ищет поле для ввода "enter_your_email", очищает его, вводит текст"""
        locator_in_t = TestSearchLocators.LOCATOR_YOUR_EMAIL_FIELD
        logging.info(f"Send {word} to element {locator_in_t[1]}")
        login_field = self.find_element(locator_in_t)
        login_field.send_keys(word)

    def enter_your_content(self, word):
        """Ищет поле для ввода "enter_your_content", очищает его, вводит текст"""
        locator_in_t = TestSearchLocators.LOCATOR_YOUR_CONTENT_FIELD
        logging.info(f"Send {word} to element {locator_in_t[1]}")
        login_field = self.find_element(locator_in_t)
        login_field.send_keys(word)

    def click_contact_us_btn(self):
        """Ищет ссылку contact_us, нажимает на неё"""
        logging.info("Click contact us button")
        self.find_element(TestSearchLocators.LOCATOR_IN_BTN).click()

    def get_alert(self):
        alert = self.find_element(None, alert=True)
        return alert

