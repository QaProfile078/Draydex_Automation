import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RunAnalysis:
    def __init__(self,context):
        self.driver=context.driver
        self.market_input_field="(//input[@aria-activedescendant])[1]"
        self.origin_destination_input_filed= '//input[@name="origin_destination"]'
        self.address_list_locator='//ul[@class="city-listing-css"]'
        self.run_analysis_button_locator='//button[text()="Run Analysis"]'

        self.roundtrip_miles_filter_minRange_placeholder = '(//thead[@class="p-datatable-thead"]//th[13])[2]//input[@placeholder="Min Range"]'
        self.roundtrip_miles_filter_maxRange_placeholder = '(//thead[@class="p-datatable-thead"]//th[13])[2]//input[@placeholder="Max Range"]'
        self.Avg_Spot_Carrier_Rate_Fuel_locator='(//p[@class="box-head"])[1]'

    def fill_market_field(self):
        WebDriverWait (self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.market_input_field)))
        input_element = self.driver.find_element(By.XPATH, self.market_input_field )
        input_element.send_keys("AB-CALGARY")
        input_element.send_keys(Keys.RETURN)
        return "AB-CALGARY"

    def fill_address_field(self):
        zip = "60139"
        for digit in zip:
            self.driver.find_element(By.XPATH, self.origin_destination_input_filed).send_keys(digit)
            time.sleep(0.5)
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.address_list_locator)))
        address = self.driver.find_element(By.XPATH, f'{self.address_list_locator}/li')
        assert zip in address.text
        address.click()
        return zip

    def click_on_runAnalysis_button(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, self.run_analysis_button_locator)))
        run_analysis_button= self.driver.find_element(By.XPATH, self.run_analysis_button_locator)
        return run_analysis_button.click()

    def get_value_in_min_roundtrip(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.roundtrip_miles_filter_minRange_placeholder)))
        minimum_roundtrip= self.driver.find_element(By.XPATH, self.roundtrip_miles_filter_minRange_placeholder).get_attribute("value")
        return float(minimum_roundtrip)

    def get_value_in_max_roundtrip(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.roundtrip_miles_filter_maxRange_placeholder)))
        maximum_roundtrip = self.driver.find_element(By.XPATH,self.roundtrip_miles_filter_maxRange_placeholder).get_attribute("value")
        return float(maximum_roundtrip)

    def get_Avg_Spot_Carrier_Rate_Fuel(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.Avg_Spot_Carrier_Rate_Fuel_locator)))
        avg_rate= self.driver.find_element(By.XPATH, self.Avg_Spot_Carrier_Rate_Fuel_locator)
        print("Avg Spot Carrier Rate Fuel showing on Rate Quote Page: ",round(float(avg_rate.text.replace("$","")),2))
        return round(float(avg_rate.text.replace("$","")),2)



