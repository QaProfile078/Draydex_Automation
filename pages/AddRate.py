import random
from operator import truediv

from parse_type import build_type_dict
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddRate:
    def __init__(self,context):
        self.driver= context.driver
        self.Add_Rate_button='//button[text()="ADD RATE"]'
        self.modal_popup= '//div[@class="modal-content"]'
        self.submit_button='//button[text()="Submit"]'
        self.submit_button_span= '//span[text()=" Submit"]'
        self.required_messages_locator='//div[@class="text-danger"]'

        self.carrier_name_field_locator='//input[contains(@placeholder, "Carrier Name")]'
        self.company_name_list='//ul[@class="searchable-list-options"]/li[contains(text(),"Test")]'

        self.LineHaul_value_locator='//input[contains(@placeholder, "Linehaul")]'
        self.FSC_percent_locator='//input[contains(@placeholder, "FSC")]'
        self.Chassis_per_day_locator='//input[contains(@placeholder, "Chassis")]'
        self.accesorials_list='//table[contains(@class,"table-sm")]//td[1]'
        self.accesorial_value_list = '//table[contains(@class,"table-sm")]//td[2]/input'

        self.min_chasis_day_locator='//input[@name="options-chassis-day"]/following-sibling::label'
        self.carrier_has_no_capacity= '//input[@name="options-carrier"]/following-sibling::label[contains(text(),"No")]'

        self.add_rate_submission_popup_message= '//div[contains(text(),"spot rate added")]'

        self.rates_table_locator='//div[@class="rateQuotestablelist"]'

        self.Rate_table_carrier_list='//div[@class="rateQuotestablelist"]//a'

        self.linehaul_list='//span[contains(text(),"Linehaul")]/span/span'
        self.FSC_list='//span[contains(text(),"Fuel")]/span'
        self.Chassis_list='//span[contains(text(),"Chassis")]/span'

        self.first_row_entries_locator='(//tr[contains(@id,"tbl_rate_id")])[1]/td'
        self.table_header_column_locator='//thead//th'
        self.table_button_column_locator='//div[@class="gap-select"]/button'

        self.delete_button_locator= '//button[@type="submit" and text()="Delete"]'
        self.modal_header_message_locator= '//div[@class="modal-title h4"]'

        self.popup_message_locator='//div[@role="alert"]/div[2]'

    def click_on_Add_Rate(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.Add_Rate_button)))
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(By.XPATH, self.Add_Rate_button)).click().perform()

    def Is_Manually_Add_Carrier_Spot_Rate_visible(self):
        AddRate_popup=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.modal_popup)))
        return AddRate_popup.is_displayed()

    def list_of_fields_present_on_popup(self):
        fields_present_on_popup=[]
        labels_present_on_popup= WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,f'{self.modal_popup}//label')))
        for entry in labels_present_on_popup:
            fields_present_on_popup.append(entry.text)
        buttons_present_on_popup=WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,f'{self.modal_popup}//button')))
        for entry in buttons_present_on_popup:
            fields_present_on_popup.append(entry.text)
        print(fields_present_on_popup)
        return fields_present_on_popup


    def click_on_submit_button(self):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.submit_button)))
            submit_button= self.driver.find_element(By.XPATH, self.submit_button)
        except:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.submit_button_span)))
            submit_button = self.driver.find_element(By.XPATH, self.submit_button_span)
        return submit_button.click()

    def is_required_field_visible(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,self.required_messages_locator)))
        required_fields_list=self.driver.find_elements(By.XPATH,self.required_messages_locator)
        for entry in required_fields_list:
            assert "required" in entry.text.lower()
        return True

    def fill_Carrier_Name_field(self):

        #filling carrier name field

        Carrier_Name= self.driver.find_element(By.XPATH, self.carrier_name_field_locator)
        Carrier_Name.send_keys("test")
        WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, self.company_name_list)))
        company_name_list =self.driver.find_elements(By.XPATH,self.company_name_list)
        selected_company_name= company_name_list[0].text
        company_name_list[0].click()
        print(selected_company_name)
        return selected_company_name

    def fill_linehauls_field(self):
        LineHaul_value= self.driver.find_element(By.XPATH, self.LineHaul_value_locator)
        if LineHaul_value.get_attribute("value") == "":
            random_value=random.randint(1, 100)
            LineHaul_value.send_keys(random_value)
        else:
            random_value= int(LineHaul_value.get_attribute("value"))
            LineHaul_value.send_keys(random_value)
        print(random_value)
        return random_value

    def fill_FSC_percent_field(self):
        FSC_percent= self.driver.find_element(By.XPATH, self.FSC_percent_locator)
        if FSC_percent.get_attribute("value") == "":
            random_value = random.randint(1, 100)
            FSC_percent.send_keys(random_value)
        else:
            random_value = float(FSC_percent.get_attribute("value"))
            FSC_percent.send_keys(random_value)
        print(random_value)
        return random_value

    def fill_Chassis_per_day_field(self):
        Chassis_per_day= self.driver.find_element(By.XPATH, self.Chassis_per_day_locator)
        if Chassis_per_day.get_attribute("value") == "":
            random_value = random.randint(1, 100)
            Chassis_per_day.send_keys(random_value)
        else:
            random_value = float(Chassis_per_day.get_attribute("value"))
            Chassis_per_day.send_keys(random_value)
        print(random_value)
        return random_value

    def select_min_chassis_day(self):
        min_chasis_day= self.driver.find_elements(By.XPATH, self.min_chasis_day_locator)
        random_value= random.randint(1,len(min_chasis_day)-1)
        selected_min_chasis_day= min_chasis_day[random_value-1]
        selected_min_chasis_day.click()
        print(random_value)
        return random_value

    def accessorials_are_present(self):
        accessorial_names_list=self.driver.find_elements(By.XPATH,self.accesorials_list)
        if len(accessorial_names_list)>0:
            return True
        else: return False

    def get_accessorial_names(self):
        accessorial_names_list = self.driver.find_elements(By.XPATH, self.accesorials_list)
        accessorial_names=[]
        for entry in accessorial_names_list:
            accessorial_names.append(entry.text)
        print(accessorial_names)
        return accessorial_names

    def get_accessorial_values(self):
        accessorial_values_list = self.driver.find_elements(By.XPATH, self.accesorial_value_list)
        accessorial_values = []
        for entry in accessorial_values_list:
            print(type(entry.get_attribute('value')), f"({(entry.get_attribute('value'))})")
            if (entry.get_attribute("value") == None) or (entry.get_attribute("value") == ""):
                value= random.randint(1,100)
                entry.send_keys(value)
                accessorial_values.append(value)
            else:
                accessorial_values.append(float(entry.get_attribute("value")))
        print(accessorial_values)
        return accessorial_values

    def select_carrier_has_capacity(self):
        no_carrier_capacity= self.driver.find_element(By.XPATH,self.carrier_has_no_capacity)
        return no_carrier_capacity.click()

    def verify_successful_rate_added_message(self):
        popup_message= WebDriverWait(self.driver,10,poll_frequency=2, ignored_exceptions=[Exception]).until(EC.visibility_of_element_located((By.XPATH,self.add_rate_submission_popup_message))).text
        print(popup_message)
        try:
            WebDriverWait(self.driver,10).until(EC.invisibility_of_element_located((By.XPATH,self.add_rate_submission_popup_message)))
        except: pass
        return popup_message

    def is_rates_table_present(self):
        rates_table=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.rates_table_locator)))
        return rates_table.is_displayed()

    def get_carrier_names_from_rates_table(self):
        Carrier_names=self.driver.find_elements(By.XPATH,self.Rate_table_carrier_list)
        carrier_list=[]
        for entry in Carrier_names:
            carrier_list.append(entry.text)
        print(carrier_list)
        return carrier_list

    def get_linehauls_from_rates_table(self):
        Linehaul_list = self.driver.find_elements(By.XPATH,self.linehaul_list )
        Linehauls=[]
        for entry in Linehaul_list:
            Linehauls.append(float(entry.text.replace("$", "")))
        print(Linehauls)
        return Linehauls

    def get_FSC_from_rates_table(self):
        FSC_list = self.driver.find_elements(By.XPATH,self.FSC_list )
        FSCs=[]
        for entry in FSC_list:
            FSCs.append(float(entry.text.replace("$", "")))
        print(FSCs)
        return FSCs

    def get_Chassis_from_rates_table(self):
        Chassis_list = self.driver.find_elements(By.XPATH,self.Chassis_list )
        Chassis=[]
        for entry in Chassis_list:
            Chassis.append(float(entry.text.replace("$", "")))
        print(Chassis)
        return Chassis

    def get_populated_columns_and_buttons(self):
        populated_columns_and_buttons =[]
        populated_columns_in_rates_table= WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,self.table_header_column_locator)))
        for entry in populated_columns_in_rates_table:
            populated_columns_and_buttons.append(entry.text)

        buttons_populated_in_rates_table= WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,self.table_button_column_locator)))
        for entry in buttons_populated_in_rates_table:
            assert entry.text == "SELECT" or entry.text == "DELETE"
            if entry.text not in populated_columns_and_buttons:
                populated_columns_and_buttons.append(entry.text)
        print(populated_columns_and_buttons)
        return populated_columns_and_buttons

    def is_first_row_a_success_class(self):
        first_row_entries= WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, self.first_row_entries_locator)))
        for entry in first_row_entries:
            print(entry.get_attribute("class"))
            assert "success-class" in entry.get_attribute("class")
        return True

    def store_added_rates_data(self,added_rate_data):
        global Added_rate_data
        Added_rate_data= added_rate_data

    def get_stored_added_rates_data(self):
        print("Added Rates across different fields: ",Added_rate_data)
        return Added_rate_data

    def store_row_number_of_rate_added(self,row):
        global row_number
        row_number = row

    def get_stored_row_number_of_rate_added(self):
        print("Added Rates is at row number : ",row_number+1,"in table")
        return row_number

    def delete_added_rate_from_row(self,row):
        delete_button_of_rate_to_deleted= WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,f'({self.delete_button_locator})[{row + 1}]')))
        action= ActionChains(self.driver)
        action.move_to_element(delete_button_of_rate_to_deleted).perform()
        return delete_button_of_rate_to_deleted.click()

    def delete_rate_confirmation_popup_message(self):
        popup_header_locator= WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.modal_header_message_locator)))
        return popup_header_locator.text

    def buttons_present_in_popup(self):
        modal_buttons_locator = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, f'{self.modal_popup}//button')))
        buttons=[]
        for entry in modal_buttons_locator:
            buttons.append(entry.text)
        return buttons

    def click_on_yes_to_delete_rate(self):
        yes_button =WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f'{self.modal_popup}//button[1]')))
        return yes_button.click()

    def popup_message_after_rate_deletion(self):
        popup_message = WebDriverWait(self.driver,10, poll_frequency=1, ignored_exceptions= [Exception]).until(EC.visibility_of_element_located((By.XPATH, self.popup_message_locator)))
        deletion_message = popup_message.text
        WebDriverWait(self.driver,10).until(EC.invisibility_of_element_located((By.XPATH, self.popup_message_locator)))
        print(deletion_message)
        return deletion_message