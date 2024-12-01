from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def enter_login(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys('fox-cherry@yandex.ru')

    def enter_pass(self):
        login_pass = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        login_pass.send_keys('password2023')

    def press_btn(self):
        login_btn = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_btn.submit()
