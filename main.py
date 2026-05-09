import data
import helpers
import time

from pages import UrbanRoutesPage
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = Chrome()
        cls.driver.implicitly_wait (5)
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

    def setup_method(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.page = UrbanRoutesPage(self.driver)
        self.page.enter_location(data.ADDRESS_FROM,data.ADDRESS_TO)

    def test_set_route(self):
        self.page.enter_location(data.ADDRESS_FROM,data.ADDRESS_TO)
        assert self.page.get_from_location() == data.ADDRESS_FROM
        assert self.page.get_to_location() == data.ADDRESS_TO
        time.sleep(10)

    def test_select_plan(self):
        self.page.click_taxi()
        self.page.click_comfort()
        assert self.page.click_comfort_active()
        time.sleep(10)

    def test_fill_phone_number(self):
        self.page.click_taxi()
        self.page.click_comfort()
        self.page.click_number(data.PHONE_NUMBER)
        assert data.PHONE_NUMBER in self.page.click_number_confirm()
        time.sleep(10)

    def test_fill_card(self):
        self.page.click_taxi()
        self.page.click_comfort()
        self.page.click_add_card(data.CARD_NUMBER, data.CARD_CODE)
        assert "Cartão" in self.page.card_confirm()
        time.sleep(10)

    def test_comment_for_driver(self):
        self.page.click_taxi()
        self.page.click_comfort()
        self.page.set_message_for_driver("Mensagem para o motorista")
        message_value = self.page.get_message_field_value()
        assert message_value == "Mensagem para o motorista"

    def test_order_blanket_and_handkerchiefs(self):
        self.page.click_taxi()
        self.page.click_comfort()
        self.page.click_blanket_and_handkerchiefs()
        assert self.page.is_blanket_and_handkerchiefs_selected()

    def test_order_2_ice_creams(self):
        number_of_ice_creams = 2
        for count in range(number_of_ice_creams):
            # Adicionar em S8
            print("função criada para adicionar a quantidade de sorvetes")
        pass

    def test_car_search_model_appears(self):
        # Adicionar em S8
        print("função criada para busca ou modelo de carro ")
        pass

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()