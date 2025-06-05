import random
import time

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class CommonActions:
    def __init__(self,context):
        self.driver= context.driver
        self.data_table_locator='//table[@class="p-datatable-table"]'
        self.data_table_loader_locator='//span[@class="table_loader"]'
        self.quote_ids_list_locator = '//td[@class="title_heading"]/a'
        self.Quote_status_list = '//tbody[@class="p-datatable-tbody"]//td[3]'
        self.requested_by_list_locator='//tbody[@class="p-datatable-tbody"]//td[5]'
        self.market_list_locator='//tbody[@class="p-datatable-tbody"]//td[10]'
        self.origin_destination_list_locator='//tbody[@class="p-datatable-tbody"]//td[11]'
        self.roundtrip_miles_list_locator='//tbody[@class="p-datatable-tbody"]//td[13]'
        self.estimated_total_list_locator='//tbody[@class="p-datatable-tbody"]//td[14]'
        self.No_record_found_message_locator = '//tr[@class ="p-datatable-emptymessage"]/td'
        self.move_to_last_page_button_locator='//button[@aria-label="Last Page"]'
        self.search_button_under_roundtrip='(//button//i[contains(@class,"pi-search")])[1]'
        self.search_button_under_estimatedtotal = '(//button//i[contains(@class,"pi-search")])[2]'

        self.quoteid_filter_placeholder = '//input[contains(@class,"p-inputtext")and @placeholder="Quote Id"]'
        self.requested_by_filter_placeholder = '//input[contains(@class,"p-inputtext")and @placeholder="Requested By"]'
        self.customer_lead_filter_placeholder = '//input[contains(@class,"p-inputtext")and @placeholder="Customer Lead"]'
        self.origin_destination_filter_placeholder = '//input[contains(@class,"p-inputtext")and @placeholder="Origin/Destination"]'
        self.roundtrip_miles_filter_minRange_placeholder='(//thead[@class="p-datatable-thead"]//th[13])[2]//input[@placeholder="Min Range"]'
        self.roundtrip_miles_filter_maxRange_placeholder='(//thead[@class="p-datatable-thead"]//th[13])[2]//input[@placeholder="Max Range"]'
        self.estimated_total_filter_minRange_placeholder = '(//thead[@class="p-datatable-thead"]//th[14])[2]//input[@placeholder="Min Range"]'
        self.estimated_total_filter_maxRange_placeholder = '(//thead[@class="p-datatable-thead"]//th[14])[2]//input[@placeholder="Max Range"]'

        self.select_status_filter_locator=''
        self.clear_button_locator='//span[contains(@class,"p-button-label p-c") and text()="Clear"]'

        self.manage_SSL_sidebar_locator = '//span[text()="Manage SSL"]'
        self.fallback_table_sidebar_locator='//span[text()="Fallback Table"]'
        self.manage_market_sidebar_locator='//span[text()="Manage Market"]'
        self.manage_terminal_sidebar_locator='//span[text()="Manage Terminal"]'


        self.DashboardTab='//a[@aria-expanded="false" and @href="/dashboard"]'
        self.button_on_Quote_details_page_locator = '//button[text()]'

    def move_to_dashboard_page(self):
        dashboard_page = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.DashboardTab)))
        action = ActionChains(self.driver)
        action.move_to_element(dashboard_page).click().perform()

    def has_loader_disappeared(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.data_table_loader_locator)))
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, self.data_table_loader_locator)))
        except:
            pass

    def is_data_table_present_on_page(self):
        try:
            data_table=WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=[Exception]).until(EC.visibility_of_element_located((By.XPATH, self.data_table_locator)))
            return data_table.is_displayed()
        except:
            return False

    def is_quote_present_in_table(self,Quote_ID):
        try:
            list_of_quotes = WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, self.quote_ids_list_locator)))
            assert len(list_of_quotes)==1
            first_quote = list_of_quotes[0].text
            print("Quote ID displaying in table: ",first_quote)
            return first_quote == Quote_ID

        except TimeoutException:
            No_record_found = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.No_record_found_message_locator)))
            return No_record_found.text



    def click_on_clear_button(self):
        clear_button= self.driver.find_element(By.XPATH, self.clear_button_locator)
        return clear_button.click()

# ------------------------------------------------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------------------------------------------------#
    def goto_quote_placeholder(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.quoteid_filter_placeholder)))
        return self.driver.find_element(By.XPATH, self.quoteid_filter_placeholder)

    def goto_customer_lead_placeholder(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.customer_lead_filter_placeholder)))
        return self.driver.find_element(By.XPATH, self.customer_lead_filter_placeholder)

    def goto_requested_by_placeholder(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.requested_by_filter_placeholder)))
        return self.driver.find_element(By.XPATH, self.requested_by_filter_placeholder)

    def goto_origin_destination_placeholder(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.origin_destination_filter_placeholder)))
        return self.driver.find_element(By.XPATH, self.origin_destination_filter_placeholder)

    def goto_min_roundtrip_miles_placeholder(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.roundtrip_miles_filter_minRange_placeholder)))
        return self.driver.find_element(By.XPATH, self.roundtrip_miles_filter_minRange_placeholder)

    def goto_max_roundtrip_miles_placeholder(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.roundtrip_miles_filter_maxRange_placeholder)))
        return self.driver.find_element(By.XPATH, self.roundtrip_miles_filter_maxRange_placeholder)

    def goto_min_estimated_total_placeholder(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.estimated_total_filter_minRange_placeholder)))
        return self.driver.find_element(By.XPATH, self.estimated_total_filter_minRange_placeholder)

    def goto_max_estimated_total_placeholder(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.estimated_total_filter_maxRange_placeholder)))
        return self.driver.find_element(By.XPATH, self.estimated_total_filter_maxRange_placeholder)

#------------------------------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------------------------#
    def are_all_requestor_selected_one(self,Requestor):
        WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,self.requested_by_list_locator)))
        Requestors_on_page_list= self.driver.find_elements(By.XPATH, self.requested_by_list_locator)
        for requestor in Requestors_on_page_list:
            print(requestor.text)
            assert requestor.text == Requestor
        return True

    def are_all_Origin_destination_selected_one(self,Origin_destination):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.origin_destination_list_locator)))
        origin_destination_on_page_list = self.driver.find_elements(By.XPATH, self.origin_destination_list_locator)

        for origin_destination in origin_destination_on_page_list:
            print(origin_destination.text)
            assert (origin_destination.text.replace(",", "").replace(" ", "") in Origin_destination.replace(",","").replace(" ", "")
                    or
                    Origin_destination.replace(",", "").replace(" ", "") in origin_destination.text.replace(",","").replace(" ", "")            )

        return True

    def are_all_markets_selected_one(self,Market):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, self.market_list_locator)))
        market_list = self.driver.find_elements(By.XPATH, self.market_list_locator)

        print("Row-wise Markets of different quotes showing in table: ")
        for entry in market_list:
            print(entry.text)
            assert (entry.text in Market) or (Market in entry.text)
        return True

    def are_all_roundtrips_between_min_and_max(self, minimumRoundtrip, maximumRoundtrip):
        WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,self.roundtrip_miles_list_locator)))
        roundtrip_miles_list= self.driver.find_elements(By.XPATH,self.roundtrip_miles_list_locator)

        print("Row-wise Roundtrip Miles of different quotes showing in table: ")
        for entry in roundtrip_miles_list:
            print (entry.text)
            assert minimumRoundtrip <= float(entry.text) <= maximumRoundtrip

        return True

    def are_all_estimatedTotal_between_min_and_max(self, minimumEstimatedTotal, maximumEstimatedTotal):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.estimated_total_list_locator)))
        estimated_total_list = self.driver.find_elements(By.XPATH, self.estimated_total_list_locator)
        for entry in estimated_total_list:
            print(entry.text.replace("$",""))
            assert minimumEstimatedTotal <= float(entry.text.replace("$","")) <= maximumEstimatedTotal

        return True

# ------------------------------------------------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------------------------------------------------#
    def click_on_quote_id(self,Quote_ID):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.quote_ids_list_locator)))
        print("quote is clickable now")
        quote_appeared = self.driver.find_element(By.XPATH,self.quote_ids_list_locator)
        print(quote_appeared.text)
        assert quote_appeared.text == Quote_ID

        action=ActionChains(self.driver)
        return action.move_to_element(quote_appeared).click().perform()

    def click_on_search_under_roundtrip(self):
        roundtripMiles_search=self.driver.find_element(By.XPATH,self.search_button_under_roundtrip)
        return roundtripMiles_search.click()

    def click_on_search_under_estimatedTotal(self):
        estimatedTotal_search=self.driver.find_element(By.XPATH,self.search_button_under_estimatedtotal)
        return estimatedTotal_search.click()

# ------------------------------------------------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------------------------------------------------#

    def get_random_quote_to_search(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, self.quote_ids_list_locator)))
        list_of_quotes = self.driver.find_elements(By.XPATH, self.quote_ids_list_locator)
        most_recent_quote =list_of_quotes[0].text

        action= ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, self.move_to_last_page_button_locator)).click().perform()

        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, self.quote_ids_list_locator)))
        list_of_quotes = self.driver.find_elements(By.XPATH, self.quote_ids_list_locator)
        oldest_quote = list_of_quotes[(len(list_of_quotes)-1)].text

        if int(oldest_quote) < int(most_recent_quote):
            Random_quote = random.randint(int(oldest_quote), int(most_recent_quote))
        else:
            Random_quote= random.randint(int(most_recent_quote),int(oldest_quote))


        return str(Random_quote)

    def get_random_requestor(self):
        Requestor_list= ["Admin","Softocean"]
        requestor= random.choice(Requestor_list)
        return requestor

    def get_random_Origin_destination(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.origin_destination_list_locator)))
        origin_destination_on_page_list = self.driver.find_elements(By.XPATH, self.origin_destination_list_locator)
        origin_destination_names=[]
        for entry in origin_destination_on_page_list:
            if entry.text not in origin_destination_names:
                origin_destination_names.append(entry.text)
        print(origin_destination_names)
        Random_origin_destination= random.choice(origin_destination_names)
        print(Random_origin_destination)
        return Random_origin_destination

    def get_random_min_roundtrip_miles(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, self.roundtrip_miles_list_locator)))
        roundtrip_list_locator = self.driver.find_elements(By.XPATH, self.roundtrip_miles_list_locator)
        roundtrip_miles=[]
        for entry in roundtrip_list_locator:
            roundtrip_miles.append(float(entry.text))
        random_min_roundtrip_value= round(random.uniform(0.00,min(roundtrip_miles)),2)
        return random_min_roundtrip_value

    def get_random_min_estimated_total(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.estimated_total_list_locator)))
        estimated_total_list= self.driver.find_elements(By.XPATH, self.estimated_total_list_locator)
        estimated_totals = []
        for entry in estimated_total_list:
            if entry.text == "N/A":
                estimated_totals.append(float(0))
            else:
                estimated_totals.append(float(entry.text.replace("$","")))
        print(estimated_totals)
        random_min_estimatedTotal_value = round(random.uniform(0.00, min(estimated_totals)), 2)
        return random_min_estimatedTotal_value

    def get_random_max_roundtrip_miles(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, self.roundtrip_miles_list_locator)))
        roundtrip_list_locator = self.driver.find_elements(By.XPATH, self.roundtrip_miles_list_locator)
        roundtrip_miles=[]
        for entry in roundtrip_list_locator:
            roundtrip_miles.append(float(entry.text))
        random_min_roundtrip_value = round(random.uniform(0.00, min(roundtrip_miles)), 2)
        random_max_roundtrip_value= round(random.uniform(random_min_roundtrip_value,max(roundtrip_miles)),2)
        return random_max_roundtrip_value

    def get_random_max_estimated_total(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.estimated_total_list_locator)))
        estimated_total_list= self.driver.find_elements(By.XPATH, self.estimated_total_list_locator)
        estimated_totals = []
        for entry in estimated_total_list:
            if entry.text == "N/A":
                estimated_totals.append(float(0))
            else:
                estimated_totals.append(float(entry.text.replace("$","")))
        print(estimated_totals)

        if all (x== 0.0 for x in estimated_totals ):
            action = ActionChains(self.driver)
            action.move_to_element(self.driver.find_element(By.XPATH, self.move_to_last_page_button_locator)).click().perform()
            WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, self.estimated_total_list_locator)))
            estimated_total_list= self.driver.find_elements(By.XPATH, self.estimated_total_list_locator)
            for entry in estimated_total_list:
                if entry.text == "N/A":
                    estimated_totals.append(float(0))
                else:
                    estimated_totals.append(float(entry.text.replace("$", "")))
        print(estimated_totals)
        random_max_estimatedTotal_value = round(random.uniform(0.00, max(estimated_totals)), 2)
        return random_max_estimatedTotal_value

    def check_selected_quote_is_rated(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.Quote_status_list)))
        Quote_status= self.driver.find_element(By.XPATH, f'{self.Quote_status_list}/p').text
        print(Quote_status)
        return  Quote_status == "Rated"

    def stored_quote_id(self,quote_id):
        global stored_quote
        stored_quote = [quote_id]
        print(quote_id)

    def get_stored_quote(self):
        print("Stored Quote: ", stored_quote[0])
        return stored_quote[0]

    def is_manage_ssl_present_in_settings(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.manage_SSL_sidebar_locator)))
        return True

    def is_fallback_table_present_in_settings(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.fallback_table_sidebar_locator)))
        return True

    def is_manage_market_present_in_settings(self):
        Manage_market =WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.manage_market_sidebar_locator)))
        return Manage_market.is_displayed()

    def is_manage_terminal_present_in_settings(self):
        Manage_terminal =WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.manage_terminal_sidebar_locator)))
        return Manage_terminal.is_displayed()

#----------------------------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------------------------#

    def get_List_of_buttons_on_Quote_details_page(self):
        Buttons_locator = WebDriverWait(self.driver,20, poll_frequency=2, ignored_exceptions=[Exception]).until(EC.visibility_of_all_elements_located((By.XPATH, self.button_on_Quote_details_page_locator)))
        Button_names=[]
        for entry in Buttons_locator:
            Button_names.append(entry.text)
        print("Available buttons on Quote details page",Button_names)
        return Button_names

