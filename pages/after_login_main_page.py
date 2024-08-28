
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base import Base


class AfterLoginMainPage(Base):

    rapid = "//div[text()='Rapid']"

    first_random_table = "//*[@class='panel button SimpleButton SimpleButton_v_flat SimpleButton_c_gradient_primary SimpleButton_use_text action buy_in SimpleButton_interactive']"

    login_name = "//*[@class='panel MiniUserInfo__nickname_text']/span"

    def get_rapid_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.rapid)))

    def get_first_random_table(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_random_table)))

    def get_login_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_name)))

    def click_rapid(self):
        self.get_rapid_button().click()
        print('click rapid')

    def click_first_random_table(self):
        self.get_first_random_table().click()
        print('click first_random_table')

    def take_login_name(self):
        login_name_element = self.get_login_name()
        login_name = login_name_element.text
        print(login_name)
        return login_name

    def play(self):
        self.get_current_url()
        self.click_rapid()
        self.click_first_random_table()
