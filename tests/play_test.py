from selenium import webdriver

from pages.after_login_main_page import AfterLoginMainPage
from pages.main_page import MainPage, driver


def login_test():
    driver = webdriver.Chrome()

    print('начинаем тест по запуску игры')

main_page = MainPage(driver)
main_page.landing_page()
main_page.click_login_button()
main_page.input_username("ValeriiTest")
main_page.input_password("TestPassword12345")
main_page.click_login_confirm_button()
after_login_page = AfterLoginMainPage(driver)
after_login_page.play()