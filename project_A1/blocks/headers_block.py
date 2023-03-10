import time
from selenium import webdriver
import allure
from selenium.webdriver import ActionChains

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base import Base
from utilities.logger import Logger


class Headers_blocks(Base):

    url = 'https://www.a1.by/ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    logo_image = '/html/body/header/nav[2]/div/div[1]/a/span/img'
    private_customers_button = "//span[contains (text(), 'Частным клиентам')]"

    business_button = "//span[contains (text(), 'Бизнесу')]"
    assert_business_button = "//h2[contains (text(), ' Бизнес решения')]"

    company_button = "//span[contains (text(), 'О компании')]"
    assert_company_button = "//h1[contains (text(), 'О компании')]"

    shopA1_button = "//span[contains (text(), 'Магазины А1')]"
    assert_shopA1_button = "//h1[contains (text(), 'Магазины А1')]"

    help_and_support_button = "//span[contains (text(), 'Помощь и поддержка')]"
    assert_help_and_support_button = "//h2[contains (text(), 'Частным клиентам')]"

    i_onlain_button = "//span[contains (text(), '#яонлайн')]"
    assert_onlain_button = "//a[contains (text(), 'Волонтерский проект #яонлайн.')]"


    # Language

    en_button = "//a[contains (text(), 'EN')]"
    be_button = "//a[contains (text(), 'BE')]"
    ru_button = "//a[contains (text(), 'RU')]"

    def get_EN(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.en_button)))

    def get_BE(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.be_button)))

    def get_RU(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.ru_button)))

    def click_language_EN(self):
        self.get_EN().click()
        print('Language EN check')

    def click_language_BE(self):
        self.get_BE().click()
        print('Language BE check')

    def click_language_RU(self):
        self.get_RU().click()
        print('Language RU check')


    # Getters

    def get_logo_image(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.logo_image)))

    def get_private_customers_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.private_customers_button)))

    def get_business_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.business_button)))

    def get_company_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.company_button)))

    def get_shopA1_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.shopA1_button)))

    def get_help_and_support_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.help_and_support_button)))

    def get_i_onlain_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.i_onlain_button)))


    # Actions

    def click_logo_image(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.logo_image)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Move to element success")

        self.get_logo_image().click()
        print('Click logo image')

    def click_private_customers_button(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.private_customers_button)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Move to element success")

        self.get_private_customers_button().click()
        print('Click private_customers_button')

    def click_business_button(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.business_button)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Move to element success")

        self.get_business_button().click()
        print('Click business_button')

    def click_company_button(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.company_button)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Move to element success")

        self.get_company_button().click()
        print('Click company_button')

    def click_shopA1_button(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.shopA1_button)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Move to element success")

        self.get_shopA1_button().click()
        print('Click shopA1_button')

    def click_help_and_support_button(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.help_and_support_button)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Move to element success")

        self.get_help_and_support_button().click()
        print('Click help_and_support_button')

    def click_i_onlain_button(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.i_onlain_button)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Move to element success")

        self.get_i_onlain_button().click()
        print('Click i_onlain_button')

    # Methods

    def headers_menu_elements(self):

        with allure.step('headers_menu_elements'):
            Logger.add_start_step(method='headers_menu_elements')

            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.get_screenshot()
            print('-'*100)

            self.click_logo_image()
            self.assert_url(self.url)
            self.click_language_EN()
            self.assert_url('https://www.a1.by/en/')
            self.get_screenshot()
            self.click_language_BE()
            self.assert_url('https://www.a1.by/be/')
            self.get_screenshot()
            self.click_language_RU()
            self.assert_url('https://www.a1.by/ru/')
            self.get_screenshot()
            print('-'*100)

            self.click_private_customers_button()
            self.assert_url(self.url)
            print('-'*100)

            self.click_business_button()
            self.assert_url('https://www.a1.by/ru/corporate/')
            self.assert_word(self.assert_business_button, 'Бизнес решения')
            self.get_screenshot()
            self.back_and_refresh()
            print('-'*100)

            self.click_company_button()
            self.assert_url('https://www.a1.by/ru/company/')
            self.assert_word(self.assert_company_button, 'О компании')
            self.get_screenshot()
            self.back_and_refresh()
            print('-' * 100)

            self.click_shopA1_button()
            print(f"List tabs: {str(self.driver.window_handles)}")
            self.driver.switch_to.window(self.driver.window_handles[1])
            print('Switch to window success')
            self.assert_url('https://www.a1.by/ru/company/company-centers')
            self.assert_word(self.assert_shopA1_button, 'Магазины А1')
            self.get_screenshot()
            self.driver.close()
            time.sleep(1)
            self.driver.switch_to.window(self.driver.window_handles[0])
            # self.back_and_refresh()
            print('-' * 100)

            self.click_help_and_support_button()
            self.assert_url('https://support.a1.by/chastnym-klientam/')
            self.assert_word(self.assert_help_and_support_button, 'Частным клиентам')
            self.get_screenshot()
            self.back_and_refresh()
            print('-' * 100)

            self.click_i_onlain_button()
            self.assert_url('https://ionline.a1.by/?utm_source=a1&utm_medium=link&utm_campaign=ionline')
            self.assert_word(self.assert_onlain_button, 'Волонтерский проект #яонлайн.')
            self.get_screenshot()
            self.back_and_refresh()
            print('-' * 100)


            Logger.add_end_step(url=self.driver.current_url, method='headers_menu_elements')
