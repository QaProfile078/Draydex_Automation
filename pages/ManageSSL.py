import random
from email.charset import add_codec

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ManageSSL:
    def __init__(self,context):
        self.driver = context.driver
        self.setting_sidebar_locator = '//ul[@class="metismenu"]//a[@href="#"]'
        self.SSL_management_page_url= 'https://app.draydex.com/settings/ssl'

        self.manage_SSL_sidebar_locator='//span[text()="Manage SSL"]'

        self.active_ssl_button='//button[text()="Active SSL"]'
        self.InActive_SSL_button='//button[text()="InActive SSL"]'
        self.add_ssl_button= '//button[text()="Add SSL"]'
        self.remove_ssl_button= '//button[text()="Remove SSL"]'
        self.Clear_button= '//span[text()="Clear"]'

        self.create_ssl_popup_locator='//div[@class="modal-content"]'

        self.SSl_name_label_locator= '//label/b[text()="SSL Name"]'
        self.SCAC_Code_label_locator = '//label/b[text()="SCAC Code"]'
        self.Abbreviated_Name_label_locator= '//label/b[text()="Abbreviated Name"]'

        self.SSl_name_label_locator = '// label / b[text() = "SSL Name"]'
        self.SCAC_Code_label_locator = '//label/b[text()="SCAC Code"]'
        self.Abbreviated_Name_label_locator = '//label/b[text()="Abbreviated Name"]'

        self.SSl_name_input_field_locator = '//input[@name="sslName"]'
        self.SCAC_Code_input_field_locator = '//input[@name="ssacCode"]'
        self.Abbreviated_Name_input_field_locator = '//input[@name="abbreviatedName"]'

        self.cancel_button_field_locator='//button[text()="Cancel"]'
        self.save_button_field_locator='//button[text()="Save"]'

        self.error_message_locator='//div[@class="invalid-feedback" and contains(text(),"is required")]'

        self.ssl_name_list='//tr[contains(@class,"p-selectable-row")]//a'
        self.scac_code_and_abbreviated_list='//tr[contains(@class,"p-selectable-row")]//p'

        self.SSL_table_locator= '//table[@class="p-datatable-table"]'
        self.ssl_created_popup_message= '//div[@role="alert"]/div[2]'

        self.button_block_locator='//div[@class="seprator_div"]//button'
        self.checkbox_locator='(//div[@data-pc-section="checkboxwrapper"])'
        self.remove_ssl_cofirmation_popup='//div[@class="modal-content"]'

        self.ssl_moved_to_inactive_message_locator='//div[@role="alert"]/div[2]'

        self.close_button_in_popup='//button[text()="Close"]'
        self.confirm_button_in_popup='//button[text()="Confirm"]'


    def check_and_move_to_manage_settings(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.setting_sidebar_locator)))
        setting_sidebar= self.driver.find_element(By.XPATH,self.setting_sidebar_locator)
        action= ActionChains(self.driver)
        return action.move_to_element(setting_sidebar).click().perform()

    def click_on_manage_ssl(self):
        manage_ssl_button= self.driver.find_element(By.XPATH, self.manage_SSL_sidebar_locator)
        return manage_ssl_button.click()

    def is_user_on_ssl_management_page(self):
        print("ssl" in self.driver.current_url and "Manage" in self.driver.title)
        return "ssl" in self.driver.current_url and "Manage" in self.driver.title

    def open_SSL_management_page(self):
        self.driver.get(self.SSL_management_page_url)

#--------------------------------------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------------------------------#

    def get_list_of_button_blocks(self):
        Button_blocks=self.driver.find_elements(By.XPATH,self.button_block_locator)
        button_names=[]
        for entry in Button_blocks:
            button_names.append(entry.text)

        return button_names

    def Is_RemoveSSL_button_disabled(self):
        try:
            button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, f'{self.button_block_locator}[text()="Remove SSL"]')))
            WebDriverWait(self.driver, 5).until(lambda driver: button.get_attribute('disabled') is None)
            print("Remove SSL button is enabled.")
            return False

        except TimeoutException:
            print("Remove SSL button is disabled.")
            return True


    def select_first_ssl_to_remove(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_any_elements_located((By.XPATH, self.checkbox_locator)))
        first_checkbox=self.driver.find_element(By.XPATH, f'{self.checkbox_locator}[1]')
        action= ActionChains(self.driver)
        action.move_to_element(first_checkbox).click().perform()

        selected_SSL_name = self.driver.find_element(By.XPATH, f'{self.ssl_name_list}[1]').text
        selected_scac_code = self.driver.find_element(By.XPATH,f'({self.scac_code_and_abbreviated_list})[1]').text
        selected_abbreviated_name = self.driver.find_element(By.XPATH,f'({self.scac_code_and_abbreviated_list})[2]').text
        Selected_SSL_data= {"SSL name": selected_SSL_name, "SCAC Code": selected_scac_code, "Abbreviated Name": selected_abbreviated_name}

        return Selected_SSL_data

# --------------------------------------------------------------------------------------------------------------------------------------------------------#
# --------------------------------------------------------------------------------------------------------------------------------------------------------#
    def click_on_InActive_SSl(self):
        InActive_SSL_button=self.driver.find_element(By.XPATH,self.InActive_SSL_button)
        return InActive_SSL_button.click()

    def click_add_ssl(self):
        add_SSL_button=self.driver.find_element(By.XPATH, self.add_ssl_button)
        return add_SSL_button.click()

    def click_on_Remove_SSL(self):
        Remove_SSL_button=self.driver.find_element(By.XPATH, self.remove_ssl_button)
        return Remove_SSL_button.click()

    def click_on_clear_button(self):
        Clear_button = self.driver.find_element(By.XPATH, self.Clear_button)
        return Clear_button.click()
# --------------------------------------------------------------------------------------------------------------------------------------------------------#
# --------------------------------------------------------------------------------------------------------------------------------------------------------#

    def check_ssl_name_field(self):
        ssl_name_field = self.driver.find_element(By.XPATH, self.SSl_name_label_locator)
        return ssl_name_field.is_displayed()

    def check_scac_code_field(self):
        scac_code_field = self.driver.find_element(By.XPATH, self.SCAC_Code_label_locator)
        return scac_code_field.is_displayed()

    def check_abbreviated_name_field(self):
        abbreviated_name_field = self.driver.find_element(By.XPATH, self.Abbreviated_Name_label_locator)
        return abbreviated_name_field.is_displayed()

    def check_cancel_button_field(self):
        cancel_button_field = self.driver.find_element(By.XPATH, self.cancel_button_field_locator)
        return cancel_button_field.is_displayed()

    def check_save_button_field(self):
        save_button_field = self.driver.find_element(By.XPATH, self.save_button_field_locator)
        return save_button_field.is_displayed()

    def click_on_save_button(self):
        save_button_field = self.driver.find_element(By.XPATH, self.save_button_field_locator)
        return save_button_field.click()

    def click_on_cancel_button(self):
        cancel_button_field = self.driver.find_element(By.XPATH, self.cancel_button_field_locator)
        return cancel_button_field.click()

    def error_message_list_while_creating_ssl(self):
        error_messages_list=WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, self.error_message_locator)))
        error_messages=[]
        for error in error_messages_list:
            error_messages.append(error.text)
        return error_messages

    def fill_ssl_name_field(self):
        ssl_name_input = f'TestSSl{random.randint(1, 100)}'
        ssl_name_input_field = self.driver.find_element(By.XPATH, self.SSl_name_input_field_locator)
        ssl_name_input_field.send_keys(ssl_name_input)
        return ssl_name_input_field.get_attribute("value")

    def fill_scac_code_field(self):
        scac_code_input = f'Code{random.randint(1, 100)}'
        scac_code_input_field = self.driver.find_element(By.XPATH, self.SCAC_Code_input_field_locator)
        scac_code_input_field.send_keys(scac_code_input)
        return scac_code_input_field.get_attribute("value")

    def fill_abbreviated_name_field(self):
        abb_name_input = f'TstSsl{random.randint(1, 100)}'
        abbreviated_name_input_field = self.driver.find_element(By.XPATH, self.Abbreviated_Name_input_field_locator)
        abbreviated_name_input_field.send_keys(abb_name_input)
        return abbreviated_name_input_field.get_attribute("value")

    def is_create_SSL_popup_closed(self):
        try:
            WebDriverWait(self.driver,10).until(EC.invisibility_of_element_located((By.XPATH,self.create_ssl_popup_locator)))
            ssl_created_message=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.ssl_created_popup_message)))
            print(ssl_created_message.text)
            return "SSL Created" in ssl_created_message.text
        except:
            return True

    def verify_SSl_created_message(self):
        ssl_created_message = WebDriverWait(self.driver,10, poll_frequency=1, ignored_exceptions=[Exception] ).until(EC.visibility_of_element_located((By.XPATH,self.ssl_created_popup_message))).text
        print(ssl_created_message)
        WebDriverWait(self.driver,10, poll_frequency=1, ignored_exceptions=[Exception] ).until(EC.invisibility_of_element_located((By.XPATH,self.ssl_created_popup_message)))

        return "SSL Created" in ssl_created_message


    def SSL_data_in_active_SSl_table(self):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, self.SSL_table_locator)))
        List_of_SSL_names_in_table= self.driver.find_elements(By.XPATH, self.ssl_name_list)
        List_of_scac_code_and_abbreviated_names_in_table= self.driver.find_elements(By.XPATH, self.scac_code_and_abbreviated_list)
        SSL_table_data=[]

        for i in range(len(List_of_SSL_names_in_table)):
            ssl_name = List_of_SSL_names_in_table[i].text

            # For each SSL name, find the corresponding SCAC Code and Abbreviated Name
            scac_code = List_of_scac_code_and_abbreviated_names_in_table[i * 2].text  # SCAC Code is at even index
            abbreviated_name = List_of_scac_code_and_abbreviated_names_in_table[i*2 + 1].text  # Abbreviated Name is at odd index

            # Create a dictionary for each row and append to the list
            SSL_table_data.append({"SSL name": ssl_name,"SCAC Code": scac_code,"Abbreviated Name": abbreviated_name})

        return SSL_table_data

    def SSL_data_in_InActive_SSl_table(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.SSL_table_locator)))
        List_of_SSL_names_in_table = self.driver.find_elements(By.XPATH, self.ssl_name_list)
        List_of_scac_code_and_abbreviated_names_in_table = self.driver.find_elements(By.XPATH,
                                                                                     self.scac_code_and_abbreviated_list)
        SSL_table_data = []

        for i in range(len(List_of_SSL_names_in_table)):
            ssl_name = List_of_SSL_names_in_table[i].text

            # For each SSL name, find the corresponding SCAC Code and Abbreviated Name
            scac_code = List_of_scac_code_and_abbreviated_names_in_table[i * 2].text  # SCAC Code is at even index
            abbreviated_name = List_of_scac_code_and_abbreviated_names_in_table[
                i * 2 + 1].text  # Abbreviated Name is at odd index

            # Create a dictionary for each row and append to the list
            SSL_table_data.append({"SSL name": ssl_name, "SCAC Code": scac_code, "Abbreviated Name": abbreviated_name})

        return SSL_table_data

# --------------------------------------------------------------------------------------------------------------------------------------------------------#
# --------------------------------------------------------------------------------------------------------------------------------------------------------#
    def has_confirm_SSL_Removal_popup_aapeared(self):
        confirm_ssl_removal_popup = (WebDriverWait(self.driver,10, poll_frequency=1, ignored_exceptions=[Exception]).until
                                     (EC.visibility_of_element_located((By.XPATH,self.remove_ssl_cofirmation_popup))))
        return confirm_ssl_removal_popup.is_displayed()

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

    def verify_ssl_moved_to_inactive_popup(self):
        ssl_moved_to_inactive_popup = WebDriverWait(self.driver, 10, poll_frequency=1,ignored_exceptions=[Exception]).until(
                            EC.visibility_of_element_located((By.XPATH, self.ssl_moved_to_inactive_message_locator))).text
        WebDriverWait(self.driver, 10, poll_frequency=1,ignored_exceptions=[Exception]).until(
            EC.invisibility_of_element_located((By.XPATH, self.ssl_moved_to_inactive_message_locator)))
        print(ssl_moved_to_inactive_popup)

        return "Moved to Inactive" in ssl_moved_to_inactive_popup
