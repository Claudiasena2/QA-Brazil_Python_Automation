from selenium.webdriver.common import driver_finder
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from helpers import retrieve_phone_code



class UrbanRoutesPage:

    # Localizadores
    from_field = (By.ID,"from")
    to_field = (By.ID,"to")
    order_button = (By.XPATH, "//button[contains(text(), 'Digitar o número e o pedido')]")

    # Selecionar tarifa e chamar taxi
    taxi_option_locator = (By.XPATH, '//button[contains(text(),"Chamar")]')
    comfort_icon_locator = (By.XPATH, '//img[@src="/static/media/kids.075fd8d4.svg"]')
    comfort_active = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')
    # Numero de Telefone
    number_text_locator = (By.CSS_SELECTOR, '.np-button')
    number_enter = (By.ID, 'phone')
    number_confirm = (By.CSS_SELECTOR, '.button.full')
    number_code = (By.ID, 'code')
    code_confirm = (By.XPATH, '//button[contains(text(),"Confirmar")]')
    number_finish = (By.CSS_SELECTOR, '.np-text')
    # Metodo de Pagamento
    add_metodo_pagamento = (By.CSS_SELECTOR, '.pp-button.filled')
    add_card = (By.CSS_SELECTOR, '.pp-plus')
    number_card = (By.ID, 'number')
    code_card = (By.CSS_SELECTOR, 'input.card-input#code')
    add_finish_card = (By.XPATH, '//button[contains(text(),"Adicionar")]')
    close_button_card = (By.CSS_SELECTOR, '.payment-picker.open .close-button')
    confirm_card = (By.CSS_SELECTOR, '.pp-value-text')
    # Comentário para o motorista
    comment_field = (By.ID, "comment")
    message_for_driver_field = (By.ID, "comment")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Metodo COR POM

    def select_comfort_tariff(self):
        comfort_icon = self.driver.find_element(*self.comfort_icon_locator)
        comfort_icon.click()
        
    def get_message_field_value(self):
        return self.driver.find_element(*self.message_for_driver_field).get_attribute("value")

    def set_message_for_driver(self, message):
        comment_field = self.wait.until(EC.element_to_be_clickable(self.comment_field))
        comment_field.clear()
        comment_field.send_keys(message)

    def _find(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )
    def _click(self,locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()


   # Endereço

    def _type(self, locator, text):
        element = self._find(locator)
        element.clear()
        element.send_keys(text)

    def _get_text(self, locator):
        return self._find(locator).text

    def _get_value(self,locator):
        return self._find(locator).get_attribute("value")

    def enter_location(self, from_text, to_text):
        self._type(self.from_field, from_text)
        self._type(self.to_field, to_text)

    def get_from_location(self):
        return self._get_value(self.from_field)

    def get_to_location(self):
        return self._get_value(self.to_field)

    def click_taxi(self):
        self.driver.find_element(*self.taxi_option_locator).click()

    def click_comfort(self):
        self.driver.find_element(*self.comfort_icon_locator).click()

    def click_comfort_active(self):
        try:
            active_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.comfort_active))
            return "active" in active_button.get_attribute("class")
        except:
            return False

    def click_number(self, phone):
        self.driver.find_element(*self.number_text_locator).click()
        self.driver.find_element(*self.number_enter).send_keys(phone)
        self.driver.find_element(*self.number_confirm).click()

        code = retrieve_phone_code(self.driver)
        code_impult = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.number_code)
        )
        code_impult.clear()
        code_impult.send_keys(code)
        self.driver.find_element(*self.code_confirm).click()

    def click_number_confirm(self):
        number_confirm = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.number_finish)
        )
        return number_confirm.text

    def click_add_card(self, card,code):
        self.driver.find_element(*self.add_metodo_pagamento).click()
        self.driver.find_element(*self.add_card).click()
        time.sleep(1)
        self.driver.find_element(*self.number_card).send_keys(card)
        time.sleep(1)
        self.driver.find_element(*self.code_card).send_keys(code)
        time.sleep(1)
        self.driver.find_element(*self.add_finish_card).click()
        self.driver.find_element(*self.close_button_card).click()

    def card_confirm(self):
       return self.driver.find_element(*self.confirm_card).text



