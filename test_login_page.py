from pages.locators import ProfilePageLocators
from .pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_enter_login(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.enter_login()
    page.enter_pass()
    page.press_btn()
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located(ProfilePageLocators.PROFILE_PET_IMG))
    browser.save_screenshot(r'C:\Users\Userman\Documents\Олеся\PycharmProjects\Selenium_UI_Pet\result7.png')
