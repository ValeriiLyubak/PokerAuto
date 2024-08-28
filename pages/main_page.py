import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.geolocation": 2})
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=chrome_options)



from base.base import Base


class MainPage(Base):
    url = 'https://poker.evenbetpoker.com/html5'

    login_button = "//*[@class='panel button SimpleButton SimpleButton_v_flat SimpleButton_c_gradient_primary SimpleButton_use_text_use_icon MiniUserInfo__login_button SimpleButton_interactive']"

    username_field = "//*[@class='Input Input_v_rounded_outline Input_c_blue with_clear_button']"

    password_field = "//*[@class='Input Input_v_rounded_outline Input_c_blue']"

    login_confirm_button = "//*[@class='panel button SimpleButton SimpleButton_v_flat SimpleButton_c_gradient_primary SimpleButton_use_text Dialog__action LoginContainer__sign_in_action SimpleButton_interactive']"

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_username_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.username_field)))

    def get_password_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_field)))

    def get_login_confirm_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_confirm_button)))

    def landing_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        print('залендились на сайт')

    def click_login_button(self):
        self.get_login_button().click()
        print('click login_button')
        time.sleep(3)

    def input_username(self, username):
        self.get_username_field().send_keys(username)
        print('input username')
        time.sleep(3)


    def input_password(self, password):
        self.get_password_field().send_keys(password)
        print('input password')
        time.sleep(3)


    def click_login_confirm_button(self):
        self.get_login_confirm_button().click()
        print('click')


