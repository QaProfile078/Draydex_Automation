
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RateQuotePage:
    def __init__(self, context):
        self.driver = context.driver
        self.RateQuotesTab='//a[@aria-expanded="false" and @href="/rate-quotes"]'
        self.Carrier_Rate_locator='//h2[@class="box-heading" and contains(text(),"Carrier Rate")]'
        self.Carrier_Chassis_locator='//h2[@class="box-heading" and contains(text(),"Carrier Chassis")]'
        self.Accessorial_Fee_locator='//h2[@class="box-heading" and contains(text(),"Accessorial Fee")]'
        self.data_table_locator='//table[@class="p-datatable-table"]'
        self.data_table_loader_locator='//span[@class="table_loader"]'
        self.quote_list_locator='//*[@class="title_heading"]'
        self.market_list_locator='//tbody[@class="p-datatable-tbody"]/tr/td[10]'
        self.origin_destination_list_locator='//tbody[@class="p-datatable-tbody"]/tr/td[11]'
        self.roundtrip_list_locator= '//tbody[@class="p-datatable-tbody"]/tr/td[13]'
        self.estimated_total_list_locator='//tbody[@class="p-datatable-tbody"]/tr/td[14]'

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------- Locators for different sorting ---------------------------------------------------------------------------------#
        self.quote_sorting_locator ='//*[contains(@class, "p-sortable-column")]//span[contains(text(),"Quote")]'
        self.customer_lead_sorting_locator = '//*[contains(@class, "p-sortable-column")]//span[contains(text(),"Customer Lead")]'
        self.status_sorting_locator = '//*[contains(@class, "p-sortable-column")]//span[contains(text(),"Status")]'
        self.request_date_sorting_locator = '//*[contains(@class, "p-sortable-column")]//span[contains(text(),"Request Date")]'
        self.requested_by_sorting_locator = '//*[contains(@class, "p-sortable-column")]//span[contains(text(),"Requested By")]'
        self.engagement_sorting_locator = '//*[contains(@class, "p-sortable-column")]//span[contains(text(),"Engagement")]'
        self.type_sorting_locator = '//*[contains(@class, "p-sortable-column")]//span[contains(text(),"Type")]'
        self.size_sorting_locator = '//*[contains(@class, "p-sortable-column")]//span[contains(text(),"Size")]'
        self.equipment_sorting_locator = '//*[contains(@class, "p-sortable-column")]//span[contains(text(),"Equipment")]'
        self.market_sorting_locator = '//*[contains(@class, "p-sortable-column")]//span[contains(text(),"Market")]'
        self.origin_destination_sorting_locator = '//*[contains(@class, "p-sortable-column")]//span[contains(text(),"Origin/Destination")]'
        self.provided_by_sorting_locator = '//*[contains(@class, "p-sortable-column")]//span[contains(text(),"Provided By")]'
        self.roundtrip_sorting_locator = '//*[contains(@class, "p-sortable-column")]//span[contains(text(),"Roundtrip Miles")]'
        self.estimated_total_sorting_locator = '//*[contains(@class, "p-sortable-column")]//span[contains(text(),"Estimated Total")]'

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        self.void_quote_button_locator = '//button[text()="VOID QUOTE"]'
        self.confirm_delete_quote_locator='//button[text()="Confirm"]'
        self.reject_delete_quote_locator='//button[text()="Close"]'
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    def move_to_rate_quotes_page(self):
        rate_Quotes_page =WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.RateQuotesTab)))
        action = ActionChains(self.driver)
        action.move_to_element(rate_Quotes_page).click().perform()


    def is_rateQuotes_displayed_in_title(self):
        WebDriverWait(self.driver, 10).until(
            EC.title_contains("Rate-Quotes")
        )
        return "Rate-Quotes" in self.driver.title

    def is_carrier_rate_on_rateQuotes_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.Carrier_Rate_locator))
        )
        carrier_rate_text= self.driver.find_element(By.XPATH, self.Carrier_Rate_locator).text
        print(carrier_rate_text)
        return carrier_rate_text.lower() == "AVG. SPOT CARRIER RATE W/FUEL".lower()

    def is_carrier_chasis_on_rateQuotes_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.Carrier_Chassis_locator))
        )
        carrier_chasis_text=self.driver.find_element(By.XPATH, self.Carrier_Chassis_locator).text
        print(carrier_chasis_text)
        return carrier_chasis_text.lower() == ("Avg. Spot Carrier Chassis $/day").lower()

    def is_accessorial_fee_on_rateQuotes_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.Accessorial_Fee_locator))
        )
        accessorial_fee_text=self.driver.find_element(By.XPATH, self.Accessorial_Fee_locator).text
        print(accessorial_fee_text)
        return accessorial_fee_text.lower()== ("Common Accessorial Fee Averages").lower()


    def is_differnt_sorts_present_on_rateQuotes_page(self):
        try:
            self.driver.find_element(By.XPATH, self.quote_sorting_locator)
            self.driver.find_element(By.XPATH, self.customer_lead_sorting_locator)
            self.driver.find_element(By.XPATH, self.status_sorting_locator)
            self.driver.find_element(By.XPATH, self.request_date_sorting_locator)
            self.driver.find_element(By.XPATH, self.requested_by_sorting_locator)
            self.driver.find_element(By.XPATH, self.engagement_sorting_locator)
            self.driver.find_element(By.XPATH, self.type_sorting_locator)
            self.driver.find_element(By.XPATH, self.size_sorting_locator)
            self.driver.find_element(By.XPATH, self.equipment_sorting_locator)
            self.driver.find_element(By.XPATH, self.market_sorting_locator)
            self.driver.find_element(By.XPATH, self.origin_destination_sorting_locator)
            self.driver.find_element(By.XPATH, self.provided_by_sorting_locator)
            self.driver.find_element(By.XPATH, self.roundtrip_sorting_locator)
            self.driver.find_element(By.XPATH, self.estimated_total_sorting_locator)

            return True
        except:
            return False

    def click_on_Quote_to_sort(self):
        WebDriverWait(self.driver,10).until(
            EC.invisibility_of_element_located((By.XPATH, self.data_table_loader_locator)))

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.quote_sorting_locator)))

        quote_sorting_button = self.driver.find_element(By.XPATH, self.quote_sorting_locator)
        action = ActionChains(self.driver)
        action.move_to_element(quote_sorting_button).perform()

        return quote_sorting_button.click()


    def is_quotes_in_ascending(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.quote_list_locator)))
        Quotes_list_elements = self.driver.find_elements(By.XPATH, self.quote_list_locator)
        Quotes_list = []
        for element in Quotes_list_elements:
            Quotes_list.append(int(element.text))
        return Quotes_list == sorted(Quotes_list)


    def is_quotes_in_descending(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.quote_list_locator)))
        Quotes_list_elements = self.driver.find_elements(By.XPATH, self.quote_list_locator)
        Quotes_list = []
        for element in Quotes_list_elements:
            Quotes_list.append(int(element.text))
        return Quotes_list == sorted(Quotes_list, reverse=True)

    def click_on_market_to_sort(self):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, self.data_table_loader_locator)))

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.market_sorting_locator)))

        market_sorting_button = self.driver.find_element(By.XPATH, self.market_sorting_locator)
        action = ActionChains(self.driver)
        action.move_to_element(market_sorting_button).perform()

        return market_sorting_button.click()

    def is_market_in_ascending(self):
        Market_list_elements = self.driver.find_elements(By.XPATH, self.market_list_locator)
        Market_list = []
        for element in Market_list_elements:
            Market_list.append(element.text)

        return Market_list == sorted(Market_list)

    def is_market_in_descending(self):
        Market_list_elements = self.driver.find_elements(By.XPATH, self.market_list_locator)
        Market_list = []
        for element in Market_list_elements:
            Market_list.append(element.text)

        return Market_list == sorted(Market_list, reverse=True)
    
    def click_on_origin_destination_to_sort(self):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, self.data_table_loader_locator)))

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.origin_destination_sorting_locator)))

        origin_destination_sorting_button = self.driver.find_element(By.XPATH, self.origin_destination_sorting_locator)
        action = ActionChains(self.driver)
        action.move_to_element(origin_destination_sorting_button).perform()

        return origin_destination_sorting_button.click()

    def is_origin_destination_in_ascending(self):
        Origin_destination_list_elements = self.driver.find_elements(By.XPATH, self.origin_destination_list_locator)
        Origin_destination_list = []
        for element in Origin_destination_list_elements:
            Origin_destination_list.append(element.text)

        return Origin_destination_list == sorted(Origin_destination_list)

    def is_origin_destination_in_descending(self):
        Origin_destination_list_elements = self.driver.find_elements(By.XPATH, self.origin_destination_list_locator)
        Origin_destination_list = []
        for element in Origin_destination_list_elements:
            Origin_destination_list.append(element.text)

        return Origin_destination_list == sorted(Origin_destination_list, reverse=True)
    
    def click_on_roundtrip_to_sort(self):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, self.data_table_loader_locator)))

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.roundtrip_sorting_locator)))

        roundtrip_sorting_button=self.driver.find_element(By.XPATH, self.roundtrip_sorting_locator)
        action = ActionChains(self.driver)
        action.move_to_element(roundtrip_sorting_button).perform()

        return roundtrip_sorting_button.click()

    def is_roundtrip_in_ascending(self):
        Roundtrip_list_elements = self.driver.find_elements(By.XPATH, self.roundtrip_list_locator)
        Roundtrip_list = []
        for element in Roundtrip_list_elements:
            Roundtrip_list.append(float(element.text))

        return Roundtrip_list == sorted(Roundtrip_list)

    def is_roundtrip_in_descending(self):
        Roundtrip_list_elements = self.driver.find_elements(By.XPATH, self.roundtrip_list_locator)
        Roundtrip_list = []
        for element in Roundtrip_list_elements:
            Roundtrip_list.append(float(element.text))

        return Roundtrip_list == sorted(Roundtrip_list, reverse=True)

    def click_on_estimated_total_to_sort(self):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, self.data_table_loader_locator)))

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.roundtrip_sorting_locator)))

        estimated_total_sorting_button=self.driver.find_element(By.XPATH, self.estimated_total_sorting_locator)
        action = ActionChains(self.driver)
        action.move_to_element(estimated_total_sorting_button).perform()

        return estimated_total_sorting_button.click()

    def is_estimated_total_in_ascending(self):
        Estimated_total_list_elements = self.driver.find_elements(By.XPATH, self.estimated_total_list_locator)
        Estimated_total_list = []
        for element in Estimated_total_list_elements:
            if element.text == 'N/A':
                Estimated_total_list.append(0)
            else:
                Estimated_total_list.append(float(element.text.replace('$', '')))

        return Estimated_total_list == sorted(Estimated_total_list)

    def is_estimated_total_in_descending(self):
        Estimated_total_list_elements = self.driver.find_elements(By.XPATH, self.estimated_total_list_locator)
        Estimated_total_list = []
        for element in Estimated_total_list_elements:
            if element.text == 'N/A':
                Estimated_total_list.append(0)
            else:
                Estimated_total_list.append(float(element.text.replace('$', '')))

        return Estimated_total_list == sorted(Estimated_total_list, reverse=True)

#---------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------
    def click_on_void_quote_button(self):
        void_quote_button= self.driver.find_element(By.XPATH, self.void_quote_button_locator)
        return void_quote_button.click()

    def click_on_confirm_button_to_proceed_deletion(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.confirm_delete_quote_locator)))
        confirm_button=self.driver.find_element(By.XPATH, self.confirm_delete_quote_locator)
        return confirm_button.click()

    def click_on_close_button_to_cancel_deletion(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.reject_delete_quote_locator)))
        close_button=self.driver.find_element(By.XPATH, self.confirm_delete_quote_locator)
        return close_button.click()

#---------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------

