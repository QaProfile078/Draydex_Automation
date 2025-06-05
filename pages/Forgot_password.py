from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ForgotPassword:
    def __init__(self,context):
        self.driver=context.driver
        self.draydex_logo_locator='//img[@id="logo"]'
        self.heading_locator= '//h3'
        self.email_input_field_locator= '//input[@name="email"]'
        self.new_password_input_field_locator='//input[@name="password"]'
        self.confirm_password_input_field_locator='//input[@name="confirm_password"]'
        self.username_input_field_locator='//input[@name="username"]'
        self.customer_and_carrier_radio_button_locator='//input[@type="radio"]'
        self.submit_button_locator= '//button[@type="submit"]'
        self.update_password_button_locator=''
        self.back_to_login_button_locator='//a[contains(@href,"login")]'
        self.popup_message_locator='//div[@role="alert"]/div[2]'


    def is_forgot_password_displayed_in_title(self):
        WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=[Exception]).until(EC.title_contains("Forgot Password"))
        return "Forgot Password" in self.driver.title

    def is_reset_password_displayed_in_title(self):
        WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=[Exception]).until(EC.title_contains("Reset Password"))
        return "Reset Password" in self.driver.title

    def is_draydex_logo_present_on_page(self):
        draydex_logo=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.draydex_logo_locator)))
        return draydex_logo.is_displayed()

    def is_forgot_password_heading_present_on_page(self):
        forgot_password_heading = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.heading_locator)))
        return "Forgot Password" in forgot_password_heading.text

    def is_reset_password_heading_present_on_page(self):
        reset_password_heading = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.heading_locator)))
        return "Reset Password" in reset_password_heading.text

    def is_email_input_field_present_on_page(self):
        email_input_filed = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.email_input_field_locator)))
        return "Enter your email address" in email_input_filed.get_attribute("placeholder")

    def is_new_password_field_present_on_page(self):
        new_password_input_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.new_password_input_field_locator)))
        return "Enter new password" in new_password_input_field.get_attribute("placeholder")

    def enter_new_password(self):
        new_password_input_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.new_password_input_field_locator)))
        return new_password_input_field.send_keys("password")

    def confirm_new_password(self):
        confirm_password_input_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.confirm_password_input_field_locator)))
        return confirm_password_input_field.send_keys("password")

    def is_confirm_password_field_present_on_page(self):
        confirm_password_input_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.confirm_password_input_field_locator)))
        return "Confirm your password" in confirm_password_input_field.get_attribute("placeholder")

    def is_username_input_field_present_on_page(self):
        username_input_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.username_input_field_locator)))
        return "Enter the username" in username_input_field.get_attribute("placeholder")

    def enter_valid_username(self,username):
        username_input_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.username_input_field_locator)))
        return username_input_field.send_keys(username)

    def enter_a_valid_email(self,email_id):
        email_input_filed = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.email_input_field_locator)))
        return email_input_filed.send_keys(email_id)


    def is_customer_and_carrier_radio_button_present_on_page(self):
        customer_and_carrier_radio_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, self.customer_and_carrier_radio_button_locator)))
        radio_buttons=["customer","carrier"]
        for entry_number in range(len(radio_buttons)):
            assert radio_buttons[entry_number] == customer_and_carrier_radio_button[entry_number].get_attribute("value")
        return True

    def select_valid_usertype(self,usertype):
        customer_and_carrier_radio_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, self.customer_and_carrier_radio_button_locator)))
        if usertype == "customer":
            return customer_and_carrier_radio_button[0].click()
        elif usertype == "carrier":
            return customer_and_carrier_radio_button[1].click()
        else:
            return "No Usertype is selected"

    def is_request_reset_link_button_present_on_page(self):
        request_reset_link_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.submit_button_locator)))
        return "REQUEST RESET LINK" in request_reset_link_button.text

    def click_on_request_reset_link_button(self):
        request_reset_link_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.submit_button_locator)))
        return request_reset_link_button.click()

    def is_update_password_button_present_on_page(self):
        update_password_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.submit_button_locator)))
        return "UPDATE PASSWORD" in update_password_button.text

    def is_update_password_button_clickable(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.submit_button_locator)))
            return True
        except:
            return False

    def click_on_update_password_button(self):
        update_password_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.submit_button_locator)))
        return update_password_button.click()

    def is_back_to_login_button_present_on_page(self):
        back_to_login_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.back_to_login_button_locator)))
        return "Back to Login" in back_to_login_button.text

    def has_successful_message_popup_appeared(self):
        popup_message= WebDriverWait(self.driver,10,poll_frequency=1, ignored_exceptions=[Exception]).until(EC.visibility_of_element_located((By.XPATH,self.popup_message_locator)))
        print(popup_message.text)
        if "," in popup_message.text:
            return "If this email exists you will receive a reset email" in popup_message.text.replace(",",'')
        else:
            return "If this email exists you will receive a reset email" in popup_message.text

    def verify_password_changed_success_message(self):
        popup_message= WebDriverWait(self.driver, 10,poll_frequency=1, ignored_exceptions=[Exception] ).until(EC.visibility_of_element_located((By.XPATH,self.popup_message_locator)))
        print(popup_message.text)
        return  popup_message.text