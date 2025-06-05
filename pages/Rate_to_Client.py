import random
import re

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RateToClient:
    def __init__(self,context):
        self.driver= context.driver
        self.rate_to_quote_button='//button[@type="submit" and text()="select"]'
        self.estimated_total_label_locator='(//td[@class="lable-info etotal"])[1]'
        self.gross_margin_label_locator='(//td[@class="lable-info etotal"])[2]'
        self.email_input_field_locator='//input[@name="email"]'
        self.submit_button_locator='//button[text()="Submit"]'
        self.quote_rated_successful_message_locator='//div[@role="alert"]/div[2]'

        self.charge_type_list='//td[@class="lable-info"]'
        self.carrier_charge_list=f'{self.charge_type_list}/following-sibling::td[1]//input'
        self.your_charge_list = f'{self.charge_type_list}/following-sibling::td[3]//input'
        self.mim_chasis_day_locator='(//span[contains(text(),"Chassis")])[2]'

        self.estimated_total_value='//input[@placeholder="ESTIMATED TOTAL"]'
        self.Gross_Margin_value= '//input[@placeholder="GROSS MARGIN"]'

    def extract_days(self,inputstring):
        match = re.search(r'(\d+)\s*day', inputstring, re.IGNORECASE)
        if match:
            return int(match.group(1))
        else:
            return None


    def open_rate_to_quote(self):
        select_spot=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.rate_to_quote_button)))
        action= ActionChains(self.driver)
        return action.move_to_element(select_spot).click().perform()


    def is_estimated_total_label_present(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.estimated_total_label_locator)))
        estimated_total_label= self.driver.find_element(By.XPATH, self.estimated_total_label_locator)
        action=ActionChains(self.driver)
        action.move_to_element(estimated_total_label).perform()
        print(estimated_total_label.text)
        return "Estimated Total" in estimated_total_label.text

    def is_gross_margin_label_present(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.gross_margin_label_locator)))
        gross_margin_label= self.driver.find_element(By.XPATH, self.gross_margin_label_locator)
        action = ActionChains(self.driver)
        action.move_to_element(gross_margin_label).perform()
        print(gross_margin_label.text)
        return "Gross Margin" in gross_margin_label.text

    def Is_email_field_present(self):
        email_input_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.email_input_field_locator)))
        placeholder_text = email_input_field.get_attribute("placeholder")
        return "emails are separated by a comma" in placeholder_text

    def enter_email_in_email_field(self):
        email_input_field = self.driver.find_element(By.XPATH, self.email_input_field_locator)
        email_input_field.send_keys("draydextesting@yopmail.com")
        return email_input_field.get_attribute("value")

    def click_on_submit_button(self):
        submit_button= WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.submit_button_locator)))
        return submit_button.click()

    def get_your_charges_for_charge_types(self):
        charge_type_list= self.driver.find_elements(By.XPATH,self.charge_type_list)
        your_charges_list= self.driver.find_elements(By.XPATH,self.your_charge_list)

        your_charges_list_against_charge_type= {}

        for i in range (len(charge_type_list)):
            key = charge_type_list[i].text
            value = your_charges_list[i].get_attribute("value")
            if value == "":
                your_charges_list[i].send_keys(random.randint(1,50))
                value= your_charges_list[i].get_attribute("value")

            your_charges_list_against_charge_type[key] = value

        min_chassis_days= self.driver.find_element(By.XPATH,self.mim_chasis_day_locator).text
        days = self.extract_days(min_chassis_days)
        your_charges_list_against_charge_type["min_chassis_days"] = days

        print("Your Charges: ",your_charges_list_against_charge_type)
        return your_charges_list_against_charge_type

    def get_updated_your_charges_for_charge_types(self):
        charge_type_list= self.driver.find_elements(By.XPATH,self.charge_type_list)
        old_your_charges_list= self.driver.find_elements(By.XPATH,self.your_charge_list)

        updated_your_charges_list_against_charge_type= {}

        for i in range (len(charge_type_list)):
            key = charge_type_list[i].text
            old_your_charges_list[i].clear()
            old_your_charges_list[i].send_keys(random.randint(1,500))
            updated_value= old_your_charges_list[i].get_attribute("value")

            updated_your_charges_list_against_charge_type[key] = updated_value

        min_chassis_days = self.driver.find_element(By.XPATH, self.mim_chasis_day_locator).text
        days = self.extract_days(min_chassis_days)
        updated_your_charges_list_against_charge_type["min_chassis_days"] = days

        print("updated values in Your Charges: ",updated_your_charges_list_against_charge_type)
        return updated_your_charges_list_against_charge_type


    def get_carrier_charges_for_charge_types(self):
        charge_type_list= self.driver.find_elements(By.XPATH,self.charge_type_list)
        carrier_charges_list= self.driver.find_elements(By.XPATH, self.carrier_charge_list)

        carrier_charges_list_against_charge_type= {}

        for i in range (len(charge_type_list)):
            key = charge_type_list[i].text
            value = carrier_charges_list[i].get_attribute("value")
            if "$" in value:
                value= value.replace("$","")
            elif "%" in value:
                value = value.replace("%", "")
            carrier_charges_list_against_charge_type[key] = value

        min_chassis_days = self.driver.find_element(By.XPATH, self.mim_chasis_day_locator).text
        days = self.extract_days(min_chassis_days)
        carrier_charges_list_against_charge_type["min_chassis_days"] = days

        print ("Carrier Charges: ",carrier_charges_list_against_charge_type)
        return carrier_charges_list_against_charge_type

    def estimated_total_calculation(self,Your_Charges):

        total = sum(round(float(value),2) for key, value in Your_Charges.items() if key != 'FSC (%)' and key != 'Chassis ($/day)' and key != 'min_chassis_days')
        total += float(Your_Charges['Linehaul($)'])* (float(Your_Charges['FSC (%)']) / 100)
        total += float(Your_Charges["min_chassis_days"])*float(Your_Charges["Chassis ($/day)"])
        print ("calculated estimated total: ",round(total,2))
        return round(total,2)

    def value_present_in_esimated_total(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.estimated_total_value)))
        estimated_total=self.driver.find_element(By.XPATH,self.estimated_total_value).get_attribute("value")
        print(float(estimated_total.replace("$","")))
        return float(estimated_total.replace("$",""))

    def Gross_margin_calculation(self,Carrier_Charges, value_in_estimated_total):

        total = sum(round(float(value),2) for key, value in Carrier_Charges.items() if key != 'FSC (%)' and key != 'Chassis ($/day)' and key != 'min_chassis_days')
        total += float(Carrier_Charges['Linehaul($)'])* (float(Carrier_Charges['FSC (%)']) / 100)
        total += float(Carrier_Charges["min_chassis_days"])*float(Carrier_Charges["Chassis ($/day)"])

        Gross_margin= round((value_in_estimated_total - total),2)

        print("calculated gross margin",Gross_margin)
        return Gross_margin

    def value_present_in_Gross_Margin(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.Gross_Margin_value)))
        gross_margin=self.driver.find_element(By.XPATH,self.Gross_Margin_value).get_attribute("value")
        print(float(gross_margin.replace("$","")))
        return float(gross_margin.replace("$",""))

    def is_estimated_total_field_disabled(self):
        estimated_total= self.driver.find_element(By.XPATH,self.estimated_total_value)
        estimated_total_is_disabled = estimated_total.get_attribute("disabled") is not None
        print(estimated_total_is_disabled)
        return estimated_total_is_disabled

    def is_gross_margin_field_disabled(self):
        gross_margin= self.driver.find_element(By.XPATH,self.Gross_Margin_value)
        gross_margin_is_disabled = gross_margin.get_attribute("disabled") is not None
        print(gross_margin_is_disabled)
        return gross_margin_is_disabled

    def Quote_rated_popup_message(self):
        quote_rated_message = WebDriverWait(self.driver,10, poll_frequency=1, ignored_exceptions=[Exception]).until(EC.visibility_of_element_located((By.XPATH, self.quote_rated_successful_message_locator))).text
        print(quote_rated_message)
        try:
            WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=[Exception]).until(
            EC.invisibility_of_element_located((By.XPATH, self.quote_rated_successful_message_locator)))
        except:pass
        return quote_rated_message