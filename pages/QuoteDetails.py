import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.Dashboard_page import DashboardPage


class CreatedQuoteDetails:
    def __init__(self,context):
        self.driver= context.driver
        self.selected_market='//select[@name="port_name"]'
        self.selected_terminal='//select[@name="terminal"]'
        self.selected_origin_destination='(//div[@class="mb-3 position-relative"]/input)[1]'
        self.selected_equipment='//select[@name="carrier_equipment_code"]'
        self.selected_special_services ='//div[@class="rbt-token-label"]'
        self.filled_quantity='//input[@name="quantity"]'
        self.filled_weight='//input[@name="weight"]'
        self.selections_in_yellow='input[type="radio"]:checked'
        self.quotes_details = {'Market': '','Type': '', 'Terminal': '', 'origin_destination': '','Length': '', 'Equipment': '','special_services': '', 'Quantity': '', 'Weight': '','option-lbs': '' }
        self.view_log_button_locator='//button[contains(text(),"View Log")]'
        self.close_button_locator='//button[contains(text(),"Close")]'
        self.Send_To_Carrier_button ='//button[contains(text(),"SEND TO CARRIERS")]'
        self.update_changes_button_locator='//button[contains(text(),"UPDATE CHANGES")]'


        self.Modal_locator='//div[@class="modal-content"]'
        self.send_to_carrier_popup_columns_locator='//thead//th'
        self.carrier_name_input_field_locator='//input[contains(@placeholder,"Carrier Name")]'
        self.phone_number_input_field_locator='//input[contains(@placeholder,"phone")]'
        self.email_input_filed_locator='//span[@class="p-multiselect-token-label"]'
        self.other_email_input_field_locator='//input[contains(@placeholder,"Enter Email")]'
        self.carrier_name_suggestions_locator='//ul[@class="city-listing-css"]/li'
        self.add_more_button_locator='//label[text()="Add More"]'

        self.close_button_on_modal_locator='//div[@class="modal-body"]//button[contains(text(),"Close")]'
        self.column_entries_locator='//tbody/tr/td'
        self.close_view_log_button_locator= '//button[@class="btn close-btn"]'


    def fetch_selected_market(self):
        selected_element = self.driver.find_element(By.XPATH, self.selected_market)
        select = Select(selected_element)
        self.quotes_details['Market'] = select.first_selected_option.text
        return self.quotes_details['Market']

    def fetch_selected_terminal(self):
        selected_element = self.driver.find_element(By.XPATH, self.selected_terminal)
        select = Select(selected_element)
        self.quotes_details['Terminal'] = select.first_selected_option.text
        return self.quotes_details['Terminal']

    def fetch_selected_origin_destination(self):
        self.quotes_details['origin_destination'] = self.driver.find_element(By.XPATH,self.selected_origin_destination).get_attribute('value')
        return self.quotes_details['origin_destination']

    def fetch_selected_equipment(self):
        selected_element = self.driver.find_element(By.XPATH, self.selected_equipment)
        select = Select(selected_element)
        self.quotes_details['Equipment'] = select.first_selected_option.text
        return self.quotes_details['Equipment']

    def fetch_selected_special_services(self):
        self.quotes_details['special_services'] = self.driver.find_element(By.XPATH, '//div[@class="rbt-token-label"]').text
        return self.quotes_details['special_services']

    def fetch_filled_quantity(self):
        self.quotes_details['Quantity'] = self.driver.find_element(By.XPATH, self.filled_quantity).get_attribute('value')
        #print(self.quotes_details['Quantity'])
        return self.quotes_details['Quantity']

    def fetch_filled_weight(self):
        self.quotes_details['Weight']=self.driver.find_element(By.XPATH,self.filled_weight).get_attribute('value')
        #print(self.quotes_details['Weight'])
        return self.quotes_details['Weight']

    def fetch_selected_type(self):
        checked_radio = self.driver.find_elements(By.CSS_SELECTOR, self.selections_in_yellow)

        for labels in checked_radio:
            label_for = labels.get_attribute("id")
            for data in self.quotes_details:
                if data.lower() in label_for.lower():
                    self.quotes_details[data] = self.driver.find_element(By.CSS_SELECTOR, f'label[for="{label_for}"]').text
        #print(self.quotes_details['Type'])
        return self.quotes_details['Type']

    def fetch_selected_size(self):
        checked_radio = self.driver.find_elements(By.CSS_SELECTOR, self.selections_in_yellow)

        for labels in checked_radio:
            label_for = labels.get_attribute("id")
            for data in self.quotes_details:
                if data.lower() in label_for.lower():
                    self.quotes_details[data] = self.driver.find_element(By.CSS_SELECTOR, f'label[for="{label_for}"]').text
        #print(self.quotes_details['Length'])
        if 'Length' in self.quotes_details:
            self.quotes_details['Size'] = self.quotes_details.pop('Length')

        return self.quotes_details['Size']

    def fetch_selected_weight_unit(self):
        checked_radio = self.driver.find_elements(By.CSS_SELECTOR, self.selections_in_yellow)

        for labels in checked_radio:
            label_for = labels.get_attribute("id")
            for data in self.quotes_details:
                if data.lower() in label_for.lower():
                    self.quotes_details[data] = self.driver.find_element(By.CSS_SELECTOR, f'label[for="{label_for}"]').text
        #print(self.quotes_details['option-lbs'])
        if 'option-lbs' in self.quotes_details:
            self.quotes_details['Weight_unit'] = self.quotes_details.pop('option-lbs')

        return self.quotes_details['Weight_unit']

    def click_on_view_log_button(self):
        view_log_button = WebDriverWait(self.driver,10,poll_frequency=1,ignored_exceptions=[Exception]).until(EC.visibility_of_element_located((By.XPATH,self.view_log_button_locator)))
        return view_log_button.click()

    def click_on_close_button(self):
        close_button = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.close_button_locator)))
        return close_button.click()

    def click_on_Send_To_Carrier_button(self):
        Send_To_Carrier_button = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.Send_To_Carrier_button)))
        return Send_To_Carrier_button.click()


    def data_in_quote_details_page(self):
        self.fetch_selected_market()
        self.fetch_selected_terminal()
        self.fetch_selected_origin_destination()
        self.fetch_selected_equipment()
        self.fetch_selected_special_services()
        self.fetch_filled_quantity()
        self.fetch_filled_weight()
        self.fetch_selected_type()
        self.fetch_selected_size()
        self.fetch_selected_weight_unit()

        print("Details present on Quote Details page ", self.quotes_details)
        return self.quotes_details

    def store_quote_details(self, quote_data):
        global Quote_details
        Quote_details = quote_data
        return Quote_details

    def get_stored_Quote_details(self):
        print("\nData of Quote stored: \n", Quote_details)
        return Quote_details

##--------------------------------------------------------------------------------------------------------------------------------------------------------##
##------------------------------------------------------- Send To Carrier Section ------------------------------------------------------------------------##
##--------------------------------------------------------------------------------------------------------------------------------------------------------##

    def has_send_to_carrier_popup_appeared(self):
        try:
            WebDriverWait(self.driver,10).until(EC.invisibility_of_element_located((By.XPATH,self.Modal_locator)))
            send_to_carrier_popup_header=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, f'{self.Modal_locator}//h2')))
            print(send_to_carrier_popup_header.text)
            return "E-mail Spot Quote Request to Your Carriers" in send_to_carrier_popup_header.text
        except:
            return True

    def get_send_to_carrier_popup_columns(self):
        List_of_columns = []
        include_column = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, f'{self.send_to_carrier_popup_columns_locator}//label')))
        List_of_columns.append(include_column.text)

        columns_list= WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, f'{self.send_to_carrier_popup_columns_locator}[text()]')))
        for entry in columns_list:
            List_of_columns.append(entry.text)

        print(List_of_columns)
        return List_of_columns

    def enter_carrier_name(self, carrier_name):
        # Wait for and enter the carrier name into the input field
        carrier_name_input_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.carrier_name_input_field_locator))
        )
        carrier_name_input_field.send_keys(carrier_name)

        # Wait until the matching suggestion is visible and click it
        def click_matching_suggestion(driver):
            suggestions = WebDriverWait(self.driver,20,poll_frequency=2,ignored_exceptions=[Exception]).until(EC.visibility_of_all_elements_located((By.XPATH, self.carrier_name_suggestions_locator)))
            for entry in suggestions:
                if entry.text.strip().lower() == carrier_name.strip().lower():
                    entry.click()
                    return True
            return False

        try:
            WebDriverWait(self.driver, 15,poll_frequency=1,ignored_exceptions=[Exception]).until(click_matching_suggestion)
        except :
            raise Exception(f"No matching suggestion found for '{carrier_name}'")

        # Assertion to ensure correct value is selected
        final_value = carrier_name_input_field.get_attribute("value").strip().lower()
        assert final_value == carrier_name.strip().lower(), f"Expected '{carrier_name}', but got '{final_value}'"

        return final_value






    def get_filled_phone_number(self):
        phone_number_input_field=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.phone_number_input_field_locator)))
        return phone_number_input_field.get_attribute("value")

    def get_filled_email(self):
        email_input_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.email_input_filed_locator)))
        return email_input_field.text

    def fill_other_email_field(self,email):
        other_email_input_field= WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.other_email_input_field_locator)))
        other_email_input_field.send_keys(email)

        return other_email_input_field.get_attribute("value")

    def click_on_add_more_button(self):
        add_more_button = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.add_more_button_locator)))
        return add_more_button.click()

##--------------------------------------------------------------------------------------------------------------------------------------------------------##
##--------------------------------------------------------------------------------------------------------------------------------------------------------##
##--------------------------------------------------------------------------------------------------------------------------------------------------------##

    def is_update_changes_button_enabled(self):
        update_changes_button= WebDriverWait(self.driver,20,poll_frequency=1,ignored_exceptions=[Exception]).until(EC.visibility_of_element_located((By.XPATH, self.update_changes_button_locator)))
        return update_changes_button.is_enabled()

    def click_on_update_changes(self):
        update_changes_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.update_changes_button_locator)))
        return update_changes_button.click()

    def has_changes_updated_popup_appeared(self):
            send_to_carrier_popup_header = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, f'{self.Modal_locator}//h4')))
            print(send_to_carrier_popup_header.text)
            return "You Have Updated the Details of This Quote!" in send_to_carrier_popup_header.text

    def click_on_close_changes_updated_popup(self):
        try:
            close_button_on_modal= WebDriverWait(self.driver,5).until(
                EC.element_to_be_clickable((By.XPATH, self.close_button_on_modal_locator)))
        except:
            close_button_on_modal = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,  '//div[@class="modal-body"]//span[contains(text(),"Close")]')))

        action = ActionChains(self.driver)
        return action.move_to_element(close_button_on_modal).click().perform()


    def fetch_updated_data_from_log_history(self):
        # Column_entries = WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, self.column_entries_locator)))
        Label_column_entries =  WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, f'{self.column_entries_locator}[1]')))
        Old_Values_column_entries =  WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, f'{self.column_entries_locator}[2]')))
        New_Values_column_entries =  WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, f'{self.column_entries_locator}[3]')))

        Labels = []
        Old_Values = []
        New_Values = []

        for entry in Label_column_entries:
            if entry.text not in Labels:
                Labels.append(entry.text)
            else:
                break
        for i in range (len(Labels)):
            Old_Values.append(Old_Values_column_entries[i].text)
        for i in range (len(Labels)):
            New_Values.append(New_Values_column_entries[i].text)

        Logs = []
        for i in range(len(Labels)):
            Logs.append({"Label": Labels[i],"Old Value": Old_Values[i],"New Value": New_Values[i]})
        print(Logs)
        return Logs

    def check_log_has_entry_of_updated_data(self):
        Logs = self.fetch_updated_data_from_log_history()
        for entry in Logs:
            if "Origin/Destination" in entry["Label"]:
                continue
            else:
                print(entry["Old Value"] != entry["New Value"])
                assert entry["Old Value"] != entry["New Value"]

        return True

    def close_view_log_popup(self):
        close_view_log_button= WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.close_view_log_button_locator)))
        return close_view_log_button.click()










