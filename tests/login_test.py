import time

from selenium import webdriver

from pages.after_login_main_page import AfterLoginMainPage
from pages.main_page import MainPage, driver


def login_test():
    driver = webdriver.Chrome()

    print('начинаем тест по входу в аккаунт')

landing_page = MainPage(driver)
landing_page.landing_page()
landing_page.click_login_button()
landing_page.input_username("ValeriiTest")
landing_page.input_password("TestPassword12345")
landing_page.click_login_confirm_button()
time.sleep(5)
after_login_page = AfterLoginMainPage(driver)
loggin_name = after_login_page.take_login_name()
print(loggin_name)
assert loggin_name == "ValeriiTest"
print('логин совпадает')
