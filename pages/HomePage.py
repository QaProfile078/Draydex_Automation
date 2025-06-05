import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class HomePage:
    def __init__(self,context):
        self.driver=context.driver
        # self.homepage_url='https://rms.devtrust.biz/'
        self.homepage_url='https://uat.draydex.com/'
        self.carrier_company_name_sorting_locator='//span[@class="p-column-title" and text()="CARRIER COMPANY NAME"]'
        self.location_sorting_locator='//span[@class="p-column-title" and text()="LOCATION"]'
        self.service_state_sorting_locator='//span[@class="p-column-title" and text()="SERVICE STATE"]'
        self.market_sorting_locator='//span[@class="p-column-title" and text()="MARKET"]'
        self.port_terminal_sorting_locator='//span[@class="p-column-title" and text()="PORT/TERMINAL"]'
        self.phone_sorting_locator='//span[@class="p-column-title" and text()="PHONE"]'
        self.entity_type_sorting_locator='//span[@class="p-column-title" and text()="ENTITY TYPE"]'

        self.carrier_company_name_list_locator= '//a[@class="showmorebutton"]'
        self.location_list_locator='//tr[@role="row"]/td[2]'
        self.phone_list_locator='//tr[@role="row"]/td[6]'
        self.service_states_in_row='//tr[@role="row"]/td[3]'
        self.markets_in_row = '//tr[@role="row"]/td[4]'

        self.list_inside_view_more='//div[contains(@class,"modal-body")]/p'
        self.close_view_more_button='//button[@class="revert"]'
        self.table_row_entries_locator='//tr[@role="row"]/td'


    def open_homepage(self):
        self.driver.get(self.homepage_url)

#--------------------------------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------------------------#

    def click_on_carrier_company_name_sort(self):
        carrier_company_name= self.driver.find_element(By.XPATH, self.carrier_company_name_sorting_locator)
        action= ActionChains(self.driver)
        return  action.move_to_element(carrier_company_name).click().perform()

    def click_on_location_sort(self):
        location = self.driver.find_element(By.XPATH, self.location_sorting_locator)
        action = ActionChains(self.driver)
        return action.move_to_element(location).click().perform()

    def click_on_service_state_sort(self):
        service_state = self.driver.find_element(By.XPATH, self.service_state_sorting_locator)
        action = ActionChains(self.driver)
        return action.move_to_element(service_state).click().perform()

    def click_on_market_sort(self):
        market = self.driver.find_element(By.XPATH, self.market_sorting_locator)
        action = ActionChains(self.driver)
        return action.move_to_element(market).click().perform()

    def click_on_port_terminal_sort(self):
        port_terminal = self.driver.find_element(By.XPATH, self.port_terminal_sorting_locator)
        action = ActionChains(self.driver)
        return action.move_to_element(port_terminal).click().perform()

    def click_on_phone_sort(self):
        phone = self.driver.find_element(By.XPATH, self.phone_sorting_locator)
        action = ActionChains(self.driver)
        return action.move_to_element(phone).click().perform()

    def click_on_entity_type(self):
        entity_type = self.driver.find_element(By.XPATH, self.entity_type_sorting_locator)
        action = ActionChains(self.driver)
        return action.move_to_element(entity_type).click().perform()

#--------------------------------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------------------------#

    def fetch_carrier_company_names_from_datatable(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, self.carrier_company_name_list_locator)))
        carrier_company_name_list= self.driver.find_elements(By.XPATH,self.carrier_company_name_list_locator)
        carrier_company_names=[]
        for element in carrier_company_name_list:
            carrier_company_names.append(element.text)

        return carrier_company_names

# --------------------------------------------------------------------------------------------------------------------------------------------------#
# --------------------------------------------------------------------------------------------------------------------------------------------------#

    def are_carrier_company_names_in_ascending(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, self.carrier_company_name_list_locator)))
        carrier_company_name_list = self.driver.find_elements(By.XPATH, self.carrier_company_name_list_locator)
        carrier_company_names = []
        for element in carrier_company_name_list:
            carrier_company_names.append(element.text.replace(" ","").replace(",",""))
            # carrier_company_names.append(element.text)


        print(carrier_company_names)
        print(sorted(carrier_company_names))
        print(carrier_company_names == sorted(carrier_company_names))

        return carrier_company_names == sorted(carrier_company_names)

    def are_carrier_company_names_in_descending(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.carrier_company_name_list_locator)))
        carrier_company_name_list = self.driver.find_elements(By.XPATH, self.carrier_company_name_list_locator)
        carrier_company_names = []
        for element in carrier_company_name_list:
            carrier_company_names.append(element.text.replace(" ","").replace(",",""))
            # carrier_company_names.append(element.text)

        print(carrier_company_names)
        print(sorted(carrier_company_names,reverse=True))
        print(carrier_company_names == sorted(carrier_company_names, reverse= True))

        return carrier_company_names == sorted(carrier_company_names, reverse= True)

    def are_locations_in_ascending(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, self.location_list_locator)))
        location_list = self.driver.find_elements(By.XPATH, self.location_list_locator)
        locations = []
        for element in location_list:
            print(element.text)
            if "N/A" in element.text:
                continue
            else:
                locations.append(element.text)

        print(locations)
        print(sorted(locations))
        print(locations == sorted(locations))

        return locations == sorted(locations)

    def are_locations_in_descending(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.location_list_locator)))
        location_list = self.driver.find_elements(By.XPATH, self.location_list_locator)
        locations = []
        for element in location_list:
            print(element.text)
            if "N/A" in element.text:
                continue
            else:
                locations.append(element.text)

        print(locations)
        print(sorted(locations, reverse=True))
        print(locations == sorted(locations, reverse=True))

        return locations == sorted(locations, reverse= True)

    def are_phone_numbers_in_ascending(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, self.phone_list_locator)))
        phone_number_list = self.driver.find_elements(By.XPATH, self.phone_list_locator)
        phone_numbers = []
        for element in phone_number_list:
            print(element.text)
            if "N/A" in element.text or element.text=="":
                continue
            else:
                phone_numbers.append(element.text)

        print(phone_numbers)
        print(sorted(phone_numbers))
        print(phone_numbers == sorted(phone_numbers))

        return phone_numbers == sorted(phone_numbers)

    def are_phone_numbers_in_descending(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, self.phone_list_locator)))
        phone_number_list = self.driver.find_elements(By.XPATH, self.phone_list_locator)
        phone_numbers = []
        for element in phone_number_list:
            print(element.text)
            if "N/A" in element.text or element.text == '':
                continue
            else:
                phone_numbers.append(element.text)

        print(phone_numbers)
        print(sorted(phone_numbers, reverse=True))
        print(phone_numbers == sorted(phone_numbers, reverse=True))

        return phone_numbers == sorted(phone_numbers, reverse=True)

    def pick_service_state_from_row_for_ascending(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,self.service_states_in_row)))

        service_states_row = self.driver.find_elements(By.XPATH, self.service_states_in_row)
        try:
            global view_more_in_rows
            self.view_more_in_rows = self.driver.find_elements(By.XPATH, f'{self.service_states_in_row}/a')
            # print(view_more_in_rows)
        except:
            pass
        count=-1
        service_state_list = []
        for entry in service_states_row:

            if "View more" in entry.text:
                count = count + 1
                action=ActionChains(self.driver)
                action.move_to_element(self.view_more_in_rows[count]).click().perform()
                time.sleep(2)
                lst = self.driver.find_elements(By.XPATH, self.list_inside_view_more)
                lst2 = (lst_of_state.text for lst_of_state in lst)
                picked_state = (sorted(lst2)[0])
                # print("Picked state from Multiple states list:", picked_state)
                service_state_list.append(picked_state)
                self.driver.find_element(By.XPATH, self.close_view_more_button).click()
                time.sleep(2)
            else:
                # print("State with no Multiple state List :", entry.text)
                service_state_list.append(entry.text)

        print("Service states in ascending order",service_state_list)
        return service_state_list

    def pick_service_state_from_row_for_descending(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,self.service_states_in_row)))

        service_states_row = self.driver.find_elements(By.XPATH, self.service_states_in_row)
        try:
            global view_more_in_rows
            self.view_more_in_rows = self.driver.find_elements(By.XPATH, f'{self.service_states_in_row}/a')
        except:
            pass
        count=-1
        service_state_list = []
        for entry in service_states_row:

            if "View more" in entry.text:
                count = count + 1
                action=ActionChains(self.driver)
                action.move_to_element(self.view_more_in_rows[count]).click().perform()
                time.sleep(2)
                lst = self.driver.find_elements(By.XPATH, self.list_inside_view_more)
                lst2 = (lst_of_state.text for lst_of_state in lst)
                picked_state = (sorted(lst2, reverse=True)[0])
                # print("Picked state from Multiple states list:", picked_state)
                service_state_list.append(picked_state)
                self.driver.find_element(By.XPATH, self.close_view_more_button).click()
                time.sleep(2)
            else:
                # print("State with no Multiple state List :", entry.text)
                service_state_list.append(entry.text)

        print("Service states in descending order",service_state_list)
        return service_state_list

    def pick_market_from_row_for_ascending(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,self.markets_in_row)))

        markets_row = self.driver.find_elements(By.XPATH, self.markets_in_row)
        try:
            global view_more_in_rows
            self.view_more_in_rows = self.driver.find_elements(By.XPATH, f'{self.markets_in_row}/a')
        except:
            pass
        count=-1
        market_list = []
        for entry in markets_row:

            if "View more" in entry.text:
                count = count + 1
                action=ActionChains(self.driver)
                action.move_to_element(self.view_more_in_rows[count]).click().perform()
                time.sleep(2)
                lst = self.driver.find_elements(By.XPATH, self.list_inside_view_more)
                lst2 = (lst_of_state.text for lst_of_state in lst)
                picked_market = (sorted(lst2)[0])
                # print("Picked state from Multiple states list:", picked_state)
                market_list.append(picked_market)
                self.driver.find_element(By.XPATH, self.close_view_more_button).click()
                time.sleep(2)
            else:
                # print("State with no Multiple state List :", entry.text)
                market_list.append(entry.text)

        print("Service states in ascending order",market_list)
        return market_list

    def pick_market_from_row_for_descending(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,self.markets_in_row)))

        markets_row = self.driver.find_elements(By.XPATH, self.markets_in_row)
        try:
            global view_more_in_rows
            self.view_more_in_rows = self.driver.find_elements(By.XPATH, f'{self.markets_in_row}/a')
        except:
            pass
        count=-1
        market_list = []

        for entry in markets_row:
            if "View more" in entry.text:

                count = count + 1
                action=ActionChains(self.driver)
                action.move_to_element(self.view_more_in_rows[count]).click().perform()
                time.sleep(2)
                lst = self.driver.find_elements(By.XPATH, self.list_inside_view_more)
                lst2 = (lst_of_state.text for lst_of_state in lst)
                picked_market = (sorted(lst2, reverse=True)[0])
                # print("Picked state from Multiple states list:", picked_state)
                market_list.append(picked_market)
                self.driver.find_element(By.XPATH, self.close_view_more_button).click()
                time.sleep(2)
            else:
                # print("State with no Multiple state List :", entry.text)
                market_list.append(entry.text)

        print("Service states in descending order",market_list)
        return market_list
