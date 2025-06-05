import random

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ManageMarketTerminal:
    def __init__(self,context):
        self.driver= context.driver
        self.manage_market_sidebar_locator='//span[text()="Manage Market"]'
        self.manage_terminal_sidebar_locator='//span[text()="Manage Terminal"]'

        self.column_names_locator= '//span[@class="p-column-title"]'
        self.top_buttons_locator ='//div[@class="seprator_div"]//button'
        self.labels_list_locator='//label/b'

        self.active_Market_button = '//button[text()="Active Market"]'
        self.InActive_Market_button = '//button[text()="InActive Markets"]'
        self.add_Market_button = '//button[text()="Add Market"]'
        self.remove_Market_button = '//button[text()="Remove Market"]'
        self.Clear_button = '//span[text()="Clear"]'

        self.countries_dropdown_locator='//select[@name="countryId"]'
        self.states_dropdown_locator='//select[@name="stateId"]'
        self.market_name_input_field_locator='//input[@name="city"]'
        self.zip_code_input_field_locator='//input[@name="zip"]'
        self.market_created_popup_message='//div[@role="alert"]/div[2]'

        self.market_name_list = '//tr[contains(@class,"p-selectable-row")]//a'
        self.market_related_data = '//tr[contains(@class,"p-selectable-row")]//p'

        self.Market_table_locator = '//table[@class="p-datatable-table"]'
        self.checkboxes_list_locator='//div[@class="p-checkbox-box p-component"]'

        self.country_searchbox_locator='//input[@type="text" and @placeholder="Country"]'
        self.state_searchbox_locator='//input[@type="text" and @placeholder="State"]'
        self.name_searchbox_locator='//input[@type="text" and @placeholder="Name"]'
        self.zip_code_searchbox_locator='//input[@type="text" and @placeholder="Zip Code"]'

        self.button_block_locator='//div[@class="seprator_div"]//button'
        self.remove_market_cofirmation_popup = '//div[@class="modal-content"]'

        self.close_button_in_popup = '//button[text()="Close"]'
        self.confirm_button_in_popup = '//button[text()="Confirm"]'

        self.market_moved_to_inactive_message_locator='//div[@role="alert"]/div[2]'
        self.no_record_message_locator='//td[text()="No record found."]'

    def click_on_manage_terminal(self):
        Manage_Market_Terminal =WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.manage_terminal_sidebar_locator)))
        return Manage_Market_Terminal.click()

    def click_on_manage_market(self):
        Manage_Market_Terminal =WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.manage_market_sidebar_locator)))
        return Manage_Market_Terminal.click()

    def is_user_on_market_terminal_management_page(self):
        print("Market" in self.driver.current_url and "Manage" in self.driver.title)
        return "Market" in self.driver.current_url and "Manage" in self.driver.title

    def get_list_of_column_names(self):
        column_name_list= WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located((By.XPATH,self.column_names_locator)))
        column_names=[]
        for entry in column_name_list:
            column_names.append(entry.text)
        print(column_names)
        return column_names

    def get_list_of_button_names(self):
        button_name_list= WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located((By.XPATH,self.top_buttons_locator)))
        button_names=[]
        for entry in button_name_list:
            aria_label = entry.get_attribute('aria-label')
            if aria_label:
                button_names.append(aria_label)
            else:
                button_names.append(entry.text)
        print(button_names)
        return button_names

    def get_list_of_labels_on_add_market_popup(self):
        labels_list=WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, self.labels_list_locator)))
        labels = []
        for entry in labels_list:
            labels.append(entry.text)
        print(labels)
        return labels

    
#-----------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------#

    def click_on_InActive_Market(self):
        InActive_Market_button=self.driver.find_element(By.XPATH,self.InActive_Market_button)
        return InActive_Market_button.click()

    def click_add_Market(self):
        add_Market_button=self.driver.find_element(By.XPATH, self.add_Market_button)
        return add_Market_button.click()

    def click_on_Remove_Market(self):
        Remove_Market_button=self.driver.find_element(By.XPATH, self.remove_Market_button)
        return Remove_Market_button.click()

    def click_on_clear_button(self):
        Clear_button = self.driver.find_element(By.XPATH, self.Clear_button)
        return Clear_button.click()

#-----------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------#

    def select_country_from_dropdown(self):
        country_dropdown=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.countries_dropdown_locator)))
        select = Select(country_dropdown)
        if len(select.options) > 1:
            select.select_by_index(random.randint(1, len(select.options) - 1))
        else:
            select.select_by_index(0)

        selected_country = select.first_selected_option
        return selected_country.text

    def select_state_from_dropdown(self):
        state_dropdown = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.states_dropdown_locator)))
        select = Select(state_dropdown)
        if len(select.options) > 1:
            select.select_by_index(random.randint(1, len(select.options) - 1))
        else:
            select.select_by_index(0)

        selected_state = select.first_selected_option
        return selected_state.text

    def fill_market_name_field(self):
        market_name_input_field= WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.market_name_input_field_locator)))
        input= f'TestMarket{random.randint(11,99)}'
        market_name_input_field.send_keys(input)
        return input

    def fill_zip_code_field(self,country):
        zip_code_input_field_locator=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.zip_code_input_field_locator)))

        if country == "USA":
            zip_code= f"{random.randint(10000, 99999)}"
            zip_code_input_field_locator.send_keys(zip_code)
            return zip_code
        elif country == "CANADA":
            letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            zip_code=f"{random.choice(letters)}{random.randint(0, 9)}{random.choice(letters)} {random.randint(0, 9)}{random.choice(letters)}{random.randint(0, 9)}"
            zip_code_input_field_locator.send_keys(zip_code)
            return zip_code
        else:
            zip_code = f"{random.randint(10000, 99999)}"
            zip_code_input_field_locator.send_keys(zip_code)
            return zip_code

    def verify_Market_created_message(self):
        market_created_message=WebDriverWait(self.driver,10, poll_frequency=1, ignored_exceptions=[Exception] ).until(EC.visibility_of_element_located((By.XPATH,self.market_created_popup_message)))
        print(market_created_message.text)
        return "Market created" in market_created_message.text
    
    def fill_market_details_in_search_box(self,market_data):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.Market_table_locator)))

        country_searchbox= WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.country_searchbox_locator)))
        state_searchbox= WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.state_searchbox_locator)))
        name_searchbox= WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.name_searchbox_locator)))
        zip_code_searchbox= WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.zip_code_searchbox_locator)))

        country_searchbox.send_keys(market_data["Country"])
        state_searchbox.send_keys(market_data["State"])
        name_searchbox.send_keys(market_data["Name"])
        zip_code_searchbox.send_keys(market_data["Zip Code"])

    def verify_market_in_market_list(self, market_data):
        try:
            List_of_Market_names_in_table = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located((By.XPATH, self.market_name_list)))
            List_of_market_related_data_in_table = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located((By.XPATH, self.market_related_data)))

            Market_table_data = []

            for i in range(len(List_of_Market_names_in_table)):
                market_name = List_of_Market_names_in_table[i].text

                Country = List_of_market_related_data_in_table[i * 4].text
                State = List_of_market_related_data_in_table[i * 4 + 1].text
                Market_name = List_of_market_related_data_in_table[i * 4 + 2].text
                Zip_code = List_of_market_related_data_in_table[i * 4 + 3].text

                Market_table_data.append(
                    {"Country": Country, "State": State, "Name": Market_name, "Zip Code": Zip_code})
            print(Market_table_data)

            return market_data in Market_table_data

        except:
            no_record_message=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.no_record_message_locator)))
            return no_record_message.text


    def select_market_to_remove(self,market_data):
        List_of_Market_names_in_table = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.market_name_list)))
        List_of_market_related_data_in_table = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.market_related_data)))

        Market_table_data = []

        for i in range(len(List_of_Market_names_in_table)):
            market_name = List_of_Market_names_in_table[i].text

            Country = List_of_market_related_data_in_table[i * 4].text
            State = List_of_market_related_data_in_table[i * 4 + 1].text
            Market_name = List_of_market_related_data_in_table[i * 4 + 2].text
            Zip_code = List_of_market_related_data_in_table[i * 4 + 3].text

            Market_table_data.append({"Country": Country, "State": State, "Name": Market_name, "Zip Code": Zip_code})
        print(Market_table_data)

        if market_data in Market_table_data:
            index = Market_table_data.index(market_data)
            select_market_checkbox= WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, self.checkboxes_list_locator)))
            select_market_checkbox[index + 1].click()
            return select_market_checkbox[index+1]
        else:
            assert market_data in Market_table_data , "The Market you searched for is not in the list"

    def Is_RemoveMarket_button_disabled(self):
        try:
            button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, f'{self.button_block_locator}[text()="Remove Market"]')))
            WebDriverWait(self.driver, 5).until(lambda driver: button.get_attribute('disabled') is None)
            print("Remove Market button is enabled.")
            return False

        except TimeoutException:
            print("Remove Market button is disabled.")
            return True

    def has_confirm_Market_Removal_popup_aapeared(self):
        confirm_market_removal_popup = (WebDriverWait(self.driver,10, poll_frequency=1, ignored_exceptions=[Exception]).until
                                     (EC.visibility_of_element_located((By.XPATH,self.remove_market_cofirmation_popup))))
        return confirm_market_removal_popup.is_displayed()

    def Is_close_and_confirm_button_present(self):
        try:
            close_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.close_button_in_popup))
            )
            confirm_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.confirm_button_in_popup))
            )

            return close_button.is_displayed() and confirm_button.is_displayed()

        except TimeoutException:
            print("Close or confirm button did not appear within the timeout period.")
            return False
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            return False

    def click_on_confirm_confirmation(self):
        confirm_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.confirm_button_in_popup)))
        return confirm_button.click()

    def click_on_cancel_confirmation(self):
        close_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.close_button_in_popup)))
        return close_button.click()

    def verify_market_moved_to_inactive_popup(self):
        market_moved_to_inactive_popup = WebDriverWait(self.driver, 10, poll_frequency=1,
                                                    ignored_exceptions=[Exception]).until(
            EC.visibility_of_element_located((By.XPATH, self.market_moved_to_inactive_message_locator)))
        WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=[Exception]).until(
            EC.invisibility_of_element_located((By.XPATH, self.market_moved_to_inactive_message_locator)))
        print(market_moved_to_inactive_popup.text)

        return "Moved to Inactive" in market_moved_to_inactive_popup.text

    def created_market_data(self,market_data):
        self.market_data = market_data
        global stored_market_data
        stored_market_data = self.market_data
        print(stored_market_data)
        return stored_market_data

    def get_created_market_data(self):
        print("Created Market data: ", stored_market_data)
        return stored_market_data



    