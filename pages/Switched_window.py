

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class SwitchedWindow:
    def __init__(self,context):
        self.driver= context.driver
        self.email_input_field_locator='//input[@class="ycptinput"]'
        self.open_email_button_locator='//button[@class="md"]'
        self.refresh_button_locator='//button[@id="refresh"]'
        self.first_email_locator='//button[@class="lm"]'
        self.quote_id_in_mail_locator='//td/a[contains(text(),"Quote")]'
        self.iframe_locator= '(//iframe[1])'
        self.informationtype_locator='//strong/parent::*'
        self.forgot_password_heading_locator='//td[contains(text(),"Forgot Password")]'
        self.reset_password_button_locator='//a[contains(text(),"Reset Password")]'

    def open_a_new_tab(self):
        self.driver.execute_script("window.open('');")

    def switch_to_yopmail(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get("https://www.yopmail.com")

    def switch_to_reset_password_window(self):
        self.driver.switch_to.window(self.driver.window_handles[2])

    def switch_to_draydex(self):
        self.driver.switch_to.window(self.driver.window_handles[0])


    def open_the_mailbox(self,email):
        email_input_field= WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.email_input_field_locator)))
        email_input_field.send_keys(email)
        open_email_button= self.driver.find_element(By.XPATH,self.open_email_button_locator)
        return open_email_button.click()

    def is_on_inbox_page(self):
        self.driver.implicitly_wait(10)
        WebDriverWait(self.driver, 10).until(
            EC.title_contains("Inbox")
        )
        return "Inbox" in self.driver.title

    def refresh_email_list(self):
        refresh_button= WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.refresh_button_locator)))
        return refresh_button.click()

    def open_first_email(self):
        move_to_mail_list_iframe = self.driver.switch_to.frame(self.driver.find_element(By.XPATH, f'{self.iframe_locator}[1]'))
        first_email = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.XPATH, self.first_email_locator)))
        first_email.click()
        self.driver.switch_to.default_content()

    def is_email_received(self):
        count=0
        while count<5:
            try:
                self.open_first_email()
                break
            except:
                self.driver.switch_to.default_content()
                self.refresh_email_list()
                count=count+1
        return count < 5

    def get_quote_number_from_mail(self):
        move_to_mail_details= self.driver.switch_to.frame(self.driver.find_element(By.XPATH,f'{self.iframe_locator}[2]'))
        Quote_id= WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.quote_id_in_mail_locator)))
        return Quote_id.text

    def is_forgot_password_heading_present_in_mail(self):
        move_to_mail_details= self.driver.switch_to.frame(self.driver.find_element(By.XPATH,f'{self.iframe_locator}[2]'))
        forgot_password_heading= WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.forgot_password_heading_locator)))
        return "Forgot Password" in forgot_password_heading.text

    def is_reset_password_button_present_in_mail(self):
        # move_to_mail_details= self.driver.switch_to.frame(self.driver.find_element(By.XPATH,f'{self.iframe_locator}[2]'))
        reset_password_button= WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.reset_password_button_locator)))
        return "Reset Password" in reset_password_button.text

    def click_on_reset_password(self):
        reset_password_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.reset_password_button_locator)))
        return reset_password_button.click()

    def get_all_info_related_to_quote(self):
        value = []
        all_informationtypes = self.driver.find_elements(By.XPATH, self.informationtype_locator)
        for i in range(len(all_informationtypes)):
            value.append(self.driver.find_element(By.XPATH, f'({self.informationtype_locator})[{i + 1}]').text)

        result = {}
        current_section = None

        for item in value:
            if item in ['Pickup Information', 'Delivery Information', 'Rate Summary', 'Applicable Accessorials']:
                current_section = item
                result[current_section] = {}
            elif ':' in item:
                key, value = item.split(': ', 1)
                if current_section:
                    result[current_section][key] = value
                else:
                    result[key] = value
            else:
                current_section = item
                result[current_section] = {}

        print("\n Data Present in mail under different sections : \n",result)
        return result

