import time
import random

from behave.textutil import select_best_encoding
from cffi.model import voidp_type
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:
    def __init__(self, context):
        self.driver = context.driver
        self.market_dropdown_locator='//select[@name="port_id"]'
        self.type_dropdown_locator = '//select[@name="type"]'
        self.terminal_dropdown_locator = '//select[@name="terminal"]'
        self.size_dropdown_locator = '//select[@name="size"]'
        self.equipment_dropdown_locator = '//select[contains(@name,"equipment")]'
        self.special_services_wrapper_locator = '//div[@class="rbt-input-wrapper"]'
        self.special_services_dropdown_locator ='//div[contains(@class,"dropdown-menu")]/a'
        self.quantity_field_locator = '//form//input[@name="quantity"]'
        self.weight_field_locator = '//form//input[@name="weight"]'
        self.weight_unit_dropdown_locator = '//select[@name="weight_type"]'
        self.create_quote_button_locator='//button[text()="Create Quote"]'
        self.origin_destination_field_locator='//input[@name="origin_destination"]'
        self.origin_destination_list_locator='//ul[@class="city-listing-css"]'
        self.origin_destination ='//ul[@class="city-listing-css"]/li'
        self.new_quote_created_message ='//div[@class="new_quote text-center"]//h2'
        self.quote_id_locator='//div[@class="new_quote text-center"]//h3/span'
        self.close_and_send_button_locator='//button[text()="Close & Send"]'
        self.view_quote_button_locator='//div[@class="quote_btn_block modal-footer"]/a'
        self.missing_required_field_message='//div[@class="invalid-feedback"]'

    def is_dashboard_displayed_in_title(self):
        WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=[Exception]).until(
            EC.title_contains("Dashboard"))
        return "Dashboard" in self.driver.title

    def select_market_from_dropdown(self):
        Market_dropdown=WebDriverWait(self.driver,5).until(
            EC.visibility_of_element_located((By.XPATH, self.market_dropdown_locator)))

        select = Select(Market_dropdown)
        if len(select.options) > 1:
            select.select_by_index(random.randint(1, len(select.options) - 1))
        else:
            select.select_by_index(0)

        selected_market = select.first_selected_option
        return selected_market.text

    def select_specific_market_from_dropdown(self,market):
        Market_dropdown = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.market_dropdown_locator)))

        select = Select(Market_dropdown)
        select.select_by_visible_text(market)

        return



    def select_type_from_dropdown(self):
        Type_dropdown = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.type_dropdown_locator)))

        # select = Select(self.driver.find_element(By.XPATH, self.type_dropdown_locator))
        select = Select(Type_dropdown)
        if len(select.options) > 1:
            select.select_by_index(random.randint(1, len(select.options) - 1))
        else:
            select.select_by_index(0)

        selected_type = select.first_selected_option
        return selected_type.text

    def select_terminal_from_dropdown(self):
        Terminals_dropdown = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.terminal_dropdown_locator))
        )

        # select = Select(self.driver.find_element(By.XPATH, self.terminal_dropdown_locator))
        select= Select(Terminals_dropdown)
        if len(select.options) > 1:
            select.select_by_index(random.randint(1, len(select.options) - 1))
        else:
            select.select_by_index(0)

        selected_terminal = select.first_selected_option
        return selected_terminal.text

    def select_size_from_dropdown(self):
        Size_dropdown = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.size_dropdown_locator))
        )

        # select = Select(self.driver.find_element(By.XPATH, self.size_dropdown_locator))
        select=Select(Size_dropdown)
        if len(select.options) > 1:
            select.select_by_index(random.randint(1, len(select.options) - 1))
        else:
            select.select_by_index(0)

        selected_size = select.first_selected_option
        return selected_size.text

    def select_equipment_from_dropdown(self):
        Equipment_dropdown = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.equipment_dropdown_locator))
        )

        # select = Select(self.driver.find_element(By.XPATH, self.equipment_dropdown_locator))
        select = Select(Equipment_dropdown)
        if len(select.options) > 1:
            select.select_by_index(random.randint(1, len(select.options) - 1))
        else:
            select.select_by_index(0)

        selected_equipment = select.first_selected_option
        return selected_equipment.text

    def select_weight_unit_from_dropdown(self):
        Weight_unit_dropdown = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.weight_unit_dropdown_locator))
        )

        # select = Select(self.driver.find_element(By.XPATH, self.weight_unit_dropdown_locator))
        select = Select(Weight_unit_dropdown)
        if len(select.options) > 1:
            select.select_by_index(random.randint(1, len(select.options) - 1))
        else:
            select.select_by_index(0)

        selected_weight_unit = select.first_selected_option
        return selected_weight_unit.text

    def fill_origin_destination_field(self):
        pincode = "60139"
        input_field = self.driver.find_element(By.XPATH, self.origin_destination_field_locator)

        for digit in pincode:
            input_field.send_keys(digit)
            time.sleep(0.5)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.origin_destination_list_locator)))

        suggestions_in_origin_destination_dropdown= WebDriverWait(self.driver, 5).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.origin_destination )))
        for address in suggestions_in_origin_destination_dropdown:
            if pincode in address.text:
              address.click()

        WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located((By.XPATH, self.origin_destination_list_locator)))

        return pincode

    def fill_special_services_field(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.special_services_wrapper_locator)))
        self.driver.find_element(By.XPATH, self.special_services_wrapper_locator).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH,self.special_services_dropdown_locator )))
        dropdown_menu = self.driver.find_elements(By.XPATH, self.special_services_dropdown_locator)
        if len(dropdown_menu) > 1:
            random_element = random.randint(1, len(dropdown_menu) - 1)
            special_service=self.driver.find_element(By.XPATH, f'{self.special_services_dropdown_locator}{[random_element]}')
            action=ActionChains(self.driver)
            selected_special_service=special_service.text
            action.move_to_element(special_service).click().perform()
            return selected_special_service

        else:
            special_service=self.driver.find_element(By.XPATH, self.special_services_dropdown_locator)
            selected_special_service = special_service.text
            action=ActionChains(self.driver)
            action.move_to_element(special_service).click().perform()
            return selected_special_service


    def fill_quantity_field(self):
        quantity = random.randint(1, 1000)
        self.driver.find_element(By.XPATH, self.quantity_field_locator).send_keys(quantity)
        return quantity

    def fill_weight_field(self):
        weight = random.randint(1, 100)
        self.driver.find_element(By.XPATH,self.weight_field_locator).send_keys(weight)
        return weight

    def click_on_create_quote(self):
        create_quote_button = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.XPATH, self.create_quote_button_locator)))
        return create_quote_button.click()

    def check_quote_created_message(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.new_quote_created_message )))

        return self.driver.find_element(By.XPATH, self.new_quote_created_message).text == "New Quote Created!"

    def check_view_quote_present_in_pop_up(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.new_quote_created_message)))

        View_Quote_button= self.driver.find_element(By.XPATH,self.view_quote_button_locator)
        return "View Quote" in View_Quote_button.text

    def check_Close_and_Send_present_in_pop_up(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.new_quote_created_message)))

        close_and_send_button= self.driver.find_element(By.XPATH,self.close_and_send_button_locator)
        return "Close & Send" in close_and_send_button.text

    def fetch_quote_id_created(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.new_quote_created_message)))
        Quote_ID = self.driver.find_element(By.XPATH, self.quote_id_locator).text
        return Quote_ID


    def click_on_view_quote(self):
        void_quote_button= WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.view_quote_button_locator)))
        return void_quote_button.click()

    def click_on_close_and_send(self):
        close_and_send_button= WebDriverWait(self.driver,10,poll_frequency=1, ignored_exceptions=[Exception]).until(EC.visibility_of_element_located((By.XPATH, self.close_and_send_button_locator)))
        action=ActionChains(self.driver)
        return action.move_to_element(close_and_send_button).click().perform()

    def check_invalid_feedback_message(self):
        invalid_feedback_message= self.driver.find_element(By.XPATH, self.missing_required_field_message).text
        return "value is required" in invalid_feedback_message

    def verify_market_in_market_dropdown_list(self,market_data):
        Market_dropdown = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.market_dropdown_locator)))
        select= Select(Market_dropdown)
        options = select.options
        option_texts = [option.text for option in options]
        # print(option_texts)

        for entry in option_texts:
            if market_data["Name"].lower() not in entry.lower():
                continue
            else:
                print(f'Market {entry} is present in Markets dropdown')
                return True
        print(f'Market {market_data["Name"]} is not present in Market dropdown')
        return False



