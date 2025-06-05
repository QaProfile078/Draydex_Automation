import random

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ClientPage:
    def __init__(self,context):
        self.driver= context.driver
        self.ClientTab = '//a[@aria-expanded="false" and @href="/users"]'
        self.client_page_buttons_locator='//div[@class="recent_quote_client"]//button'
        self.edit_view_button_locator='//div[@data-pc-section="label"]'
        self.client_list_column_names_locator='//span[@class="p-column-title"]'
        self.client_names_list='(//div[@class="CustomerCulamnCss"]/a)'
        self.client_type_list='//tbody//tr[@role="row"]/td[7]/p'
        self.profile_options_locator='//div[contains(@class,"profile_heading-general")]'
        self.support_options_locator='//div[@class="adress_box"]/p'


    def move_to_client_page(self):
        clients_page =WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.ClientTab)))
        action = ActionChains(self.driver)
        action.move_to_element(clients_page).click().perform()

    def is_clients_displayed_in_title(self):
        WebDriverWait(self.driver, 10, poll_frequency=2, ignored_exceptions=[Exception]).until(EC.title_contains("Users"))
        print(self.driver.title)
        return "Users" in self.driver.title

    def list_of_buttons_on_client_page(self):
        buttons=[]
        Buttons_list=WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,self.client_page_buttons_locator)))
        for entry in Buttons_list:
            buttons.append(entry.text)
        edit_view_button= WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.edit_view_button_locator)))
        buttons.append(edit_view_button.text)
        print(buttons)
        return buttons

    def list_of_column_names(self):
        clients_list_column_names= WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located((By.XPATH, self.client_list_column_names_locator)))
        column_names=[]
        for entry in clients_list_column_names:
            action=ActionChains(self.driver)
            action.move_to_element(entry).perform()
            column_names.append(entry.text)
        print(column_names)
        return column_names

    def list_of_clients_present(self):
        List_of_clients= WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, self.client_names_list)))
        List_of_client_names=[]
        for entry in List_of_clients:
            ActionChains(self.driver).move_to_element(entry).perform()
            List_of_client_names.append(entry.text)
        print(List_of_client_names)
        return List_of_client_names
    
    def open_and_get_random_client_profile(self):
        List_of_clients= WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, self.client_names_list)))
        List_of_client_types= WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, self.client_type_list)))
        random_client_number = random.randint(0, len(List_of_clients) - 1)
        action = ActionChains(self.driver)

        selected_client_details={}

        selected_client_details["client name"]= List_of_clients[random_client_number].text
        selected_client_details["client type"]= List_of_client_types[random_client_number].text
        action.move_to_element(List_of_clients[random_client_number]).perform()
        List_of_clients[random_client_number].click()
        print(selected_client_details)
        return selected_client_details

    def get_displayed_options_for_client(self):
        profile_options_list= WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, self.profile_options_locator)))
        profile_options=[]
        for entry in profile_options_list:
            profile_options.append(entry.text)
        print(profile_options)
        return profile_options

    def get_support_options_for_client(self):
        support_options_list = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.support_options_locator)))
        support_options = []
        for entry in support_options_list:
            support_options.append(entry.text.strip(":"))
        print(support_options)
        return support_options
