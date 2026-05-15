from selenium.webdriver.common import driver_finder
from selenium.webdriver.common.keys import Keys
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
    # Para clicar no seletor de cobertor e lenços
    def click_blanket_and_handkerchiefs(self):
        self.driver.find_element(By.XPATH, "//div[@class='r-sw-container']//div[@class='switch']").click()
    # Comentário para o motorista
    comment_field = (By.ID, "comment")
    message_for_driver_field = (By.ID, "comment")
    # Para clicar no seletor de cobertor e lenços
    def click_blanket_and_handkerchiefs(self):
        self.driver.find_element(By.XPATH, "//div[@class='r-sw-container']//div[@class='switch']").click()
    # Localizadores para sorvetes
    ice_cream_plus_button = (By.CSS_SELECTOR, '.counter-plus')
    ice_cream_counter = (By.CLASS_NAME, "counter-value")
    #Criada para busca ou modelo de carro
    from_field = (By.ID, "from")
    to_field = (By.ID, "to")
    comfort_fare_button = (By.XPATH, "//div[@class='tcard'][.//div[text()='Comfort']]")
    car_model_locator = (By.XPATH, "//div[@class='tcard-title']")
    request_taxi_button = (By.CLASS_NAME, "smart-button-main")
    order_header_title = (By.CLASS_NAME, "order-header-title")
    phone_number_field = (By.ID, "phone")  # Localizador do campo de telefone

    def click_request_taxi(self):
        # Usar JavaScript para clicar no botão, evitando problemas de interceptação
        taxi_button = self.driver.find_element(*self.request_taxi_button)
        self.driver.execute_script("arguments[0].click();", taxi_button)

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

    def is_blanket_and_handkerchiefs_selected(self):
        checkbox = self.driver.find_element(By.XPATH, "//div[@class='r-sw-container']//input[@class='switch-input']")
        return checkbox.is_selected()

    def _find(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )
    def _click(self,locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def add_ice_cream(self, quantity=1):
        for i in range(quantity):
            self.driver.find_element(*self.ice_cream_plus_button).click()

    def get_ice_cream_counter(self):
        counter_text = self.driver.find_element(*self.ice_cream_counter).text
        return int(counter_text)

    def select_car_comfort(self):
        print("=== DEBUG: Procurando botão de conforto ===")
        cars = self.driver.find_elements(By.XPATH, "//div[@class='tcard']")
        print(f"Cartões de carro encontrados: {len(cars)}")
        if len(cars) == 0:
            print("Nenhum cartão encontrado. Vamos ver o que tem na página...")
            all_divs = self.driver.find_elements(By.TAG_NAME, "div")
            print(f"Total de divs na página: {len(all_divs)}")

    def get_visible_car_model_text(self):
        element = self.wait.until(EC.visibility_of_element_located(self.car_model_locator))
        return element.text

    def set_from(self, from_text):
        element = self.wait.until(EC.element_to_be_clickable(self.from_field))
        element.click()
        element.send_keys(Keys.CONTROL + "a")  # Seleciona tudo
        element.send_keys(Keys.DELETE)  # Deleta
        time.sleep(0.5)  # Pausa importante
        element.send_keys(from_text)

    def set_to(self, to_text):
        element = self.wait.until(EC.element_to_be_clickable(self.to_field))
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        time.sleep(0.5)
        element.send_keys(to_text)

    def click_request_taxi(self):
        time.sleep(2)
        print("=== DEBUG: Investigando botões na página ===")
    try:
        all_buttons = self.driver.find_elements(By.TAG_NAME, "button")
        print(f"Total de botões encontrados: {len(all_buttons)}")

        for i, button in enumerate(all_buttons):
            try:
                text = button.text.strip()
                classes = button.get_attribute("class")
                is_displayed = button.is_displayed()
                is_enabled = button.is_enabled()
                print(
                    f"Botão {i}: texto='{text}', classes='{classes}', visível={is_displayed}, habilitado={is_enabled}")
            except Exception as e:
                print(f"Botão {i}: erro ao obter informações - {e}")
        clickable_elements = self.driver.find_elements(By.XPATH,
                                                       "//*[contains(@class, 'button') or contains(@class, 'btn')]")
        print(f"\nElementos com 'button' ou 'btn' na classe: {len(clickable_elements)}")

        for i, element in enumerate(clickable_elements):
            try:
                text = element.text.strip()
                classes = element.get_attribute("class")
                tag = element.tag_name
                print(f"Elemento {i}: tag='{tag}', texto='{text}', classes='{classes}'")
            except:
                print(f"Elemento {i}: erro ao obter informações")

    except Exception as e:
        print(f"Erro geral no debug: {e}")

    # Por enquanto, não vamos tentar clicar - só investigar
    print("=== FIM DO DEBUG ===")

    def is_car_search_modal_visible(self):
        modal_locator = (By.CSS_SELECTOR, ".order-body")
        try:
            self.wait.until(EC.visibility_of_element_located(modal_locator))
            return True
        except:
            return False

        # Endereço

    def _type(self, locator, text):
        element = self._find(locator)
        element.clear()
        element.send_keys(Keys.CONTROL + "a")  # Seleciona tudo
        element.send_keys(Keys.DELETE)
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
