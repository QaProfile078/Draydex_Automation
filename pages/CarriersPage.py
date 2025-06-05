import random

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CarriersPage:
    def __init__(self,context):
        self.driver = context.driver
        self.CarriersTab= '//a[@aria-expanded="false" and @href="/carriers"]'
        self.carriers_page_table_locator= '//div[@class="row"]'
        self.carrier_names_list='//div[@class="pro_list"]/a'
        self.Switch_box_locator='//div[@class="switch_box"]'
        self.carrier_list_column_headers_locator='//span[@data-pc-section="headertitle"]'
        self.carrier_details_label_locator='//label[contains(@class,"carrier-details")]'
        self.different_section_header_locator='//div[contains(@class,"mb-3")]//b'
        self.add_to_carrier_button_locator='//button[contains(@class,"add_carriers")]'
        self.block_or_ban_carrier_button_locator='//button[contains(@class,"block_btn")]'

        self.modal_popup= '//div[@class="modal-content"]'
        self.popup_message_locator='//div[@role="alert"]/div[2]'
        self.back_button_locator='//button[contains(@class,"Back")]'
        self.my_carrier_locator='//button[text()="My Carrier"]'
        self.blue_background_carrier_list='td[class="title_heading"] a'

        self.favourite_carrier_data= '//tr[@role="row"]/td'

    def move_to_carriers_page(self):
        carrier_Quotes_page =WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.CarriersTab)))
        action = ActionChains(self.driver)
        action.move_to_element(carrier_Quotes_page).click().perform()

    def is_carriers_displayed_in_title(self):
        WebDriverWait(self.driver, 10, poll_frequency=2, ignored_exceptions=[Exception]).until(EC.title_contains("Carriers"))
        return "Carriers" in self.driver.title

    def is_carrier_table_present(self):
        Carriers_table= WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.carriers_page_table_locator)))
        return Carriers_table.is_displayed()

    def carrier_table_header(self):
        CarriersPage_table_header= WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, f'{self.carriers_page_table_locator}//h3')))
        return CarriersPage_table_header.text

    def list_of_carriers_present(self):
        List_of_carriers= WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, self.carrier_names_list)))
        List_of_carrier_names=[]
        for entry in List_of_carriers:
            List_of_carrier_names.append(entry.text)
        print(List_of_carrier_names)
        return List_of_carrier_names

    def list_of_radio_buttons(self):
        Radio_button_names_list= WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, f'{self.Switch_box_locator}/p')))
        Radio_buttons=[]
        for entry in Radio_button_names_list:
            Radio_buttons.append(entry.text)
        print(Radio_buttons)
        return Radio_buttons

    def list_of_column_headers(self):
        carrier_list_column_headers= WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located((By.XPATH, self.carrier_list_column_headers_locator)))
        column_headers=[]
        for entry in carrier_list_column_headers:
            column_headers.append(entry.text)
        print(column_headers)
        return column_headers

    def open_and_get_random_carrier_profile(self):
        List_of_carriers= WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, self.carrier_names_list)))
        random_carrier_number= random.randint(0,(len(List_of_carriers)-1))
        action= ActionChains(self.driver)
        action.move_to_element(List_of_carriers[random_carrier_number]).perform()

        selected_carrier_name = List_of_carriers[random_carrier_number].text
        print("Selected carrier: ",selected_carrier_name )
        List_of_carriers[random_carrier_number].click()

        return  selected_carrier_name


    def list_of_different_sections_on_carrier_details_page(self):
        sections=[]
        carrier_details_label=WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, self.carrier_details_label_locator)))
        for entry in carrier_details_label:
            label= entry.text
            if ":" in entry.text:
                label= label.replace(":","")
            sections.append(label)

        section_header= WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, self.different_section_header_locator)))
        for entry in section_header:
            sections.append(entry.text)

        print(sections)
        return sections

    def is_add_to_carrier_button_present(self):
        Add_to_Carrier_button= WebDriverWait(self.driver,10,poll_frequency=1, ignored_exceptions=[Exception]).until(EC.visibility_of_element_located((By.XPATH,self.add_to_carrier_button_locator)))
        print(Add_to_Carrier_button.text)
        assert "Add to My Carriers" in Add_to_Carrier_button.text
        return Add_to_Carrier_button.is_displayed()

    def is_block_ban_carrier_button_present(self):
        Block_or_Ban_Carrier_button = WebDriverWait(self.driver, 10,poll_frequency=1, ignored_exceptions=[Exception]).until(
            EC.visibility_of_element_located((By.XPATH, self.block_or_ban_carrier_button_locator)))
        print(Block_or_Ban_Carrier_button.text)
        assert "Block/Ban Carrier" in Block_or_Ban_Carrier_button.text
        return Block_or_Ban_Carrier_button.is_displayed()

    def click_on_add_to_carrier(self):
        Add_to_Carrier_button= WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.add_to_carrier_button_locator)))
        return Add_to_Carrier_button.click()

    def click_on_block_ban_carrier(self):
        Block_or_Ban_Carrier_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.block_or_ban_carrier_button_locator)))
        return Block_or_Ban_Carrier_button.click()

    def buttons_present_in_modal_popup(self):
        modal_buttons_locator = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, f'{self.modal_popup}//button')))
        buttons = []
        for entry in modal_buttons_locator:
            buttons.append(entry.text)
        return buttons

    def click_on_confirm(self):
        confirm_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f'{self.modal_popup}//button[1]')))
        return confirm_button.click()

    def popup_message_after_adding_to_favourite(self):
        popup_message = WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=[Exception]).until(
            EC.visibility_of_element_located((By.XPATH, self.popup_message_locator)))
        print(popup_message.text)
        return popup_message.text

    def click_on_back_button(self):
        Back_button= WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.back_button_locator)))
        return Back_button.click()

    def click_on_my_carrier(self):
        My_carrier_button= WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.my_carrier_locator)))
        return My_carrier_button.click()

    def check_carrier_in_blue_background(self):
        Blue_background_row_list= WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, self.blue_background_carrier_list)))
        carrier_name_list=[]
        for entry in Blue_background_row_list:
            carrier_name_list.append(entry.text)

        if Carrier_name in carrier_name_list:
            print(f'{Carrier_name} is present in My Carriers list with Blue Background')

        return Carrier_name in carrier_name_list

    def store_selected_carrier_name(self,carrier_name):
        global Carrier_name
        Carrier_name =carrier_name

    def get_stored_selected_carrier_name(self):
        return Carrier_name

    def fetch_carriers_data(self):
        favourite_carriers_data = []
        list_of_data = WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, self.favourite_carrier_data)))
        data = [entry.text for entry in list_of_data]
        if len(data) % 8 != 0:
            print("Warning: Data length not divisible by 8. Some rows may be incomplete.")

        for i in range(len(data) // 8):
            row_data = data[i * 8: (i + 1) * 8]
            favourite_carriers_data.append(row_data)

        print(favourite_carriers_data)
        return favourite_carriers_data

    def is_favourite_carrier_present(self):
        list_of_data = self.driver.find_elements(By.XPATH, self.favourite_carrier_data)
        data = [entry.text for entry in list_of_data]

        return len(data)//8 >0
