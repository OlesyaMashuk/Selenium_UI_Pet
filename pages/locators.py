from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')

class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASS = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")

class ProfilePageLocators:
     PROFILE_PET_IMG = (By.CSS_SELECTOR, '#app > main > div > div > div.p-dataview-content > div > div:nth-child(1)' \
                                       ' > div > img')
