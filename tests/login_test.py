from selenium import webdriver

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